import os
import json
import argparse
from datetime import datetime
from collections import defaultdict


class FileStructureConfig:
    """Configuration class for all toggleable options"""
    def __init__(self):
        # Directory traversal options
        self.ignore_hidden_files = True
        self.use_enhanced_traversal = True
        self.target_directory = '.'
        
        # Output options
        self.save_json = True
        self.json_filename = 'file_structure.json'
        self.save_tree_txt = True
        self.tree_filename = 'folder_tree.txt'
        
        # Tree generation options
        self.show_sizes = True
        self.include_summary = True
        self.show_errors = True
        self.show_extensions = True
        self.show_modified_dates = False
        self.show_created_dates = False
        
        # Display options
        self.show_preview = True
        self.preview_count = 3
        self.verbose_output = True
        
        # Formatting options
        self.indent_json = True
        self.json_indent = 2


def get_size_in_units(size_bytes):
    """Convert bytes to KB, MB, GB with proper rounding"""
    kb = size_bytes / 1024
    mb = size_bytes / (1024 ** 2)
    gb = size_bytes / (1024 ** 3)
    return {
        'bytes': size_bytes,
        'kb': round(kb, 2),
        'mb': round(mb, 2),
        'gb': round(gb, 2)
    }


def get_file_info(file_path):
    """Get comprehensive file information"""
    try:
        stat = os.stat(file_path)
        size = stat.st_size
        
        return {
            'size': get_size_in_units(size),
            'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
            'created': datetime.fromtimestamp(stat.st_ctime).isoformat(),
            'extension': os.path.splitext(file_path)[1].lower()
        }
    except (OSError, IOError):
        return {
            'size': get_size_in_units(0),
            'modified': None,
            'created': None,
            'extension': None,
            'error': 'Could not access file'
        }


def traverse_directory_basic(path, ignore_hidden=True):
    """Basic directory traversal with minimal file information"""
    structure = []
    
    for root, dirs, files in os.walk(path):
        # Filter out hidden directories if ignore_hidden is True
        if ignore_hidden:
            dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        # Get relative path from starting directory
        rel_root = os.path.relpath(root, path)
        
        # Process each file
        for file in files:
            # Skip hidden files if ignore_hidden is True
            if ignore_hidden and file.startswith('.'):
                continue
                
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
            except (OSError, IOError):
                # Handle files that can't be accessed
                size = 0
            
            structure.append({
                'relative_path': os.path.join(rel_root, file),
                'size': get_size_in_units(size),
                'extension': os.path.splitext(file)[1].lower()
            })
    
    return structure


def traverse_directory_enhanced(path, ignore_hidden=True):
    """Enhanced version with more file details"""
    structure = []
    
    for root, dirs, files in os.walk(path):
        # Filter out hidden directories if ignore_hidden is True
        if ignore_hidden:
            dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        rel_root = os.path.relpath(root, path)
        
        for file in files:
            # Skip hidden files if ignore_hidden is True
            if ignore_hidden and file.startswith('.'):
                continue
                
            file_path = os.path.join(root, file)
            rel_path = os.path.join(rel_root, file)
            
            file_info = get_file_info(file_path)
            structure.append({
                'relative_path': rel_path,
                **file_info
            })
    
    return structure

def generate_tree_structure_txt(json_data, config, output_file=None):
    """
    Generate visual tree structure text from JSON file data
    
    Args:
        json_data: List of file dictionaries or path to JSON file
        config: FileStructureConfig object with all options
        output_file: Optional path to save the tree structure (if None, returns string)
    
    Returns:
        String containing the formatted tree structure
    """
    
    def build_tree_structure(data):
        """Build a nested tree structure from flat JSON data"""
        
        def create_folder_structure():
            """Create a new folder structure with correct types"""
            return {
                'files': [],
                'folders': {}
            }
        
        tree = create_folder_structure()
        
        for item in data:
            path = item['relative_path']
            # Normalize path separators and remove leading './'
            path = path.replace('\\', '/').lstrip('./')
            
            if not path:  # Skip empty paths
                continue
                
            parts = path.split('/')
            current = tree
            
            # Navigate/create folder structure
            for part in parts[:-1]:
                if part not in current['folders']:
                    current['folders'][part] = create_folder_structure()
                current = current['folders'][part]
            
            # Add file to the current folder
            filename = parts[-1]
            file_info = {
                'name': filename,
                'size': item['size'],
                'extension': item.get('extension', ''),
                'modified': item.get('modified', ''),
                'created': item.get('created', ''),
                'error': item.get('error', None)
            }
            current['files'].append(file_info)
        
        return tree
    
    def format_size(size_dict):
        """Format file size for display"""
        if size_dict['gb'] >= 1:
            return f"{size_dict['gb']} GB"
        elif size_dict['mb'] >= 1:
            return f"{size_dict['mb']} MB"
        elif size_dict['kb'] >= 1:
            return f"{size_dict['kb']} KB"
        else:
            return f"{size_dict['bytes']} bytes"
    
    def generate_tree_text(tree, prefix="", is_last=True):
        """Generate visual tree structure as text"""
        lines = []
        
        # Sort folders and files for consistent output
        folders = sorted(tree['folders'].items())
        files = sorted(tree['files'], key=lambda x: x['name'])
        
        # Process folders first
        for i, (folder_name, folder_data) in enumerate(folders):
            is_last_folder = (i == len(folders) - 1) and len(files) == 0
            
            # Folder line
            connector = "└── " if is_last_folder else "├── "
            lines.append(f"{prefix}{connector}{folder_name}/")
            
            # Recursive call for folder contents
            extension = "    " if is_last_folder else "│   "
            lines.extend(generate_tree_text(
                folder_data, 
                prefix + extension, 
                is_last_folder
            ))
        
        # Process files
        for i, file_info in enumerate(files):
            is_last_file = (i == len(files) - 1)
            connector = "└── " if is_last_file else "├── "
            
            # Build file line with optional components
            file_line = f"{prefix}{connector}{file_info['name']}"
            
            # Add size if enabled
            if config.show_sizes:
                file_line += f" ({format_size(file_info['size'])})"
            
            # Add extension if enabled and available
            if config.show_extensions and file_info['extension']:
                file_line += f" [{file_info['extension']}]"
            
            # Add modified date if enabled and available
            if config.show_modified_dates and file_info['modified']:
                file_line += f" (Modified: {file_info['modified'][:10]})"
            
            # Add created date if enabled and available
            if config.show_created_dates and file_info['created']:
                file_line += f" (Created: {file_info['created'][:10]})"
            
            # Add error if enabled and present
            if config.show_errors and file_info['error']:
                file_line += f" [ERROR: {file_info['error']}]"
            
            lines.append(file_line)
        
        return lines
    
    # Main function logic
    try:
        # Handle input - either JSON data or file path
        if isinstance(json_data, str):
            # It's a file path
            with open(json_data, 'r') as f:
                data = json.load(f)
        else:
            # It's already parsed JSON data
            data = json_data
        
        # Build tree structure
        tree = build_tree_structure(data)
        
        # Generate tree text
        tree_lines = []
        tree_lines.append("Directory Structure")
        tree_lines.append("=" * 50)
        tree_lines.append("")
        tree_lines.append("./")
        
        # Generate the tree
        tree_content = generate_tree_text(tree, "", True)
        tree_lines.extend(tree_content)
        
        # Add summary if requested
        if config.include_summary:
            tree_lines.append("")
            tree_lines.append("=" * 50)
            tree_lines.append("Summary")
            tree_lines.append("=" * 50)
            
            # Calculate totals
            total_files = len(data)
            total_size = sum(item['size']['bytes'] for item in data)
            
            total_size_formatted = format_size(get_size_in_units(total_size))
            
            # Count by extension
            extensions = {}
            for item in data:
                ext = item.get('extension', '')
                if not ext:
                    ext = 'no extension'
                extensions[ext] = extensions.get(ext, 0) + 1
            
            tree_lines.append(f"Total Files: {total_files}")
            tree_lines.append(f"Total Size: {total_size_formatted}")
            tree_lines.append("")
            tree_lines.append("Files by Extension:")
            for ext, count in sorted(extensions.items()):
                tree_lines.append(f"  {ext}: {count} files")
        
        # Join all lines
        result = '\n'.join(tree_lines)
        
        # Write to file if specified
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result)
            if config.verbose_output:
                print(f"Tree structure saved to '{output_file}'")
        
        return result
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find JSON file '{json_data}'")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in '{json_data}'")
    except Exception as e:
        raise Exception(f"Error generating tree structure: {str(e)}")



def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Generate file structure tree')
    
    # Directory options
    parser.add_argument('--directory', '-d', default='.', help='Target directory (default: current)')
    parser.add_argument('--include-hidden', action='store_true', help='Include hidden files and directories')
    parser.add_argument('--basic-traversal', action='store_true', help='Use basic traversal (faster, less info)')
    
    # Output options
    parser.add_argument('--no-json', action='store_true', help='Skip JSON file generation')
    parser.add_argument('--no-tree', action='store_true', help='Skip tree text file generation')
    parser.add_argument('--json-file', default='file_structure.json', help='JSON output filename')
    parser.add_argument('--tree-file', default='folder_tree.txt', help='Tree output filename')
    
    # Display options
    parser.add_argument('--no-sizes', action='store_true', help='Hide file sizes')
    parser.add_argument('--no-summary', action='store_true', help='Hide summary statistics')
    parser.add_argument('--no-errors', action='store_true', help='Hide error messages')
    parser.add_argument('--no-extensions', action='store_true', help='Hide file extensions')
    parser.add_argument('--show-modified', action='store_true', help='Show modified dates')
    parser.add_argument('--show-created', action='store_true', help='Show created dates')
    parser.add_argument('--no-preview', action='store_true', help='Skip preview output')
    parser.add_argument('--preview-count', type=int, default=3, help='Number of files to preview')
    parser.add_argument('--quiet', action='store_true', help='Minimal output')
    
    return parser.parse_args()


def main():
    """Main execution function with configurable options"""
    # Parse command line arguments
    args = parse_arguments()
    
    # Create configuration object
    config = FileStructureConfig()
    
    # Apply command line arguments to config
    config.target_directory = args.directory
    config.ignore_hidden_files = not args.include_hidden
    config.use_enhanced_traversal = not args.basic_traversal
    config.save_json = not args.no_json
    config.save_tree_txt = not args.no_tree
    config.json_filename = args.json_file
    config.tree_filename = args.tree_file
    config.show_sizes = not args.no_sizes
    config.include_summary = not args.no_summary
    config.show_errors = not args.no_errors
    config.show_extensions = not args.no_extensions
    config.show_modified_dates = args.show_modified
    config.show_created_dates = args.show_created
    config.show_preview = not args.no_preview
    config.preview_count = args.preview_count
    config.verbose_output = not args.quiet
    
    try:
        # Traverse directory using selected method
        if config.use_enhanced_traversal:
            if config.verbose_output:
                print("Using enhanced traversal (with detailed file info)...")
            result = traverse_directory_enhanced(config.target_directory, config.ignore_hidden_files)
        else:
            if config.verbose_output:
                print("Using basic traversal (faster, minimal info)...")
            result = traverse_directory_basic(config.target_directory, config.ignore_hidden_files)
        
        # Save to JSON file if enabled
        if config.save_json:
            indent = config.json_indent if config.indent_json else None
            with open(config.json_filename, 'w') as f:
                json.dump(result, f, indent=indent)
            if config.verbose_output:
                print(f"File structure saved to '{config.json_filename}'")
        
        # Display results
        if config.verbose_output:
            print(f"Found {len(result)} files")
            print(f"Hidden files ignored: {config.ignore_hidden_files}")
        
        # Preview first few entries if enabled
        if config.show_preview and result:
            print(f"\nFirst {min(config.preview_count, len(result))} entries:")
            for entry in result[:config.preview_count]:
                size_info = f": {entry['size']['mb']} MB" if config.show_sizes else ""
                print(f"- {entry['relative_path']}{size_info}")
        
        # Generate tree structure if enabled
        if config.save_tree_txt:
            if config.save_json:
                # Generate from JSON file
                tree_text = generate_tree_structure_txt(config.json_filename, config, config.tree_filename)
            else:
                # Generate from data directly
                tree_text = generate_tree_structure_txt(result, config, config.tree_filename)
            
            if config.verbose_output:
                print("Tree structure generated successfully.")
        
        # Option to display tree to console
        if config.verbose_output:
            print("\nTree structure preview:")
            print("-" * 30)
            if config.save_json:
                preview_tree = generate_tree_structure_txt(config.json_filename, config, output_file=None)
            else:
                preview_tree = generate_tree_structure_txt(result, config, output_file=None)
            
            # Show first 20 lines of tree
            tree_lines = preview_tree.split('\n')
            for line in tree_lines[:20]:
                print(line)
            if len(tree_lines) > 20:
                print(f"... ({len(tree_lines) - 20} more lines)")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
