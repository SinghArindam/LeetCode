import os
import re
from pathlib import Path
import logging
import json

# Import necessary functions/classes from your provided scripts
# Adjust these imports based on how you want to expose them
# For this example, we'll assume we can import main from automate_notes_v2
# and generate_tree_structure_txt from filetreegen_v1.2
# and relevant traversal functions for JSON data.

# To avoid circular imports or issues with running main directly,
# we'll modify the orchestrator to call the core logic of automate_notes_v2
# and import specific functions from filetreegen_v1.2

# --- Start of modifications to integrate automate_notes_v2 ---
# We'll need to replicate the necessary parts or refactor automate_notes_v2
# to expose its core functionality without running main() directly.
# For simplicity, let's directly import the main function for now
# but in a real scenario, you'd refactor automate_notes_v2 to have a callable
# function that performs the processing without needing to be the entry point.

# Since `automate_notes_v2.py` has a `main()` function, we'll need to
# run it carefully. A better approach would be to refactor `automate_notes_v2.py`
# to expose a function like `run_notes_generation()` that `orchestrator.py` can call.
# For this example, we'll run it as a subprocess or try to import main directly
# and call it (which might have side effects).
# Given the complexity, let's use a subprocess for `automate_notes_v2.py` for isolation.

import subprocess

# --- End of modifications to integrate automate_notes_v2 ---

# --- Import from filetreegen_v1.2.py ---
# We need to import generate_tree_structure_txt and the traversal functions
# and the Config class from filetreegen_v1.2
try:
    from filetreegen_v1_2 import generate_tree_structure_txt, traverse_directory_enhanced, FileStructureConfig
except ImportError:
    print("Error: Could not import from filetreegen_v1_2.py. Make sure the file is in the same directory.")
    exit(1)


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

CURRENT_DIR = Path(__file__).parent
NOTES_DIR = CURRENT_DIR / "Notes"
SUBMISSIONS_DIR = CURRENT_DIR / "submissions"
TREE_FILE_PATH = CURRENT_DIR / "TREE_FILE.txt"
FILE_STRUCTURE_JSON_PATH = CURRENT_DIR / "file_structure.json"
README_FILE_PATH = CURRENT_DIR / "README.md"

def run_notes_generation():
    """
    Executes the automate_notes_v2.py script to generate notes.
    """
    logger.info("Starting notes generation using automate_notes_v2.py...")
    try:
        # Assuming automate_notes_v2.py is a standalone script that runs and exits
        # and it creates/updates notes in the 'Notes' directory.
        result = subprocess.run(
            ["python", str(CURRENT_DIR / "automate_notes_v2.py")],
            capture_output=True,
            text=True,
            check=True
        )
        logger.info("Notes generation completed successfully.")
        logger.debug(f"Notes generation stdout:\n{result.stdout}")
        if result.stderr:
            logger.warning(f"Notes generation stderr:\n{result.stderr}")

    except subprocess.CalledProcessError as e:
        logger.error(f"Error during notes generation: {e}")
        logger.error(f"Stdout: {e.stdout}")
        logger.error(f"Stderr: {e.stderr}")
        raise
    except FileNotFoundError:
        logger.error("Python executable not found. Make sure Python is installed and in your PATH.")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred during notes generation: {e}")
        raise

def generate_file_tree():
    """
    Generates the file tree structure using filetreegen_v1.2.py's logic.
    """
    logger.info("Generating file tree structure...")
    try:
        config = FileStructureConfig()
        config.target_directory = str(CURRENT_DIR)
        config.save_json = True
        config.json_filename = str(FILE_STRUCTURE_JSON_PATH)
        config.save_tree_txt = True
        config.tree_filename = str(TREE_FILE_PATH)
        config.show_preview = False # Don't show preview during automation
        config.verbose_output = False # Keep quiet
        config.include_summary = True # Ensure summary is included

        # Use the enhanced traversal to get data for JSON and tree
        file_data = traverse_directory_enhanced(config.target_directory, config.ignore_hidden_files)

        # Save to JSON file
        with open(config.json_filename, 'w', encoding='utf-8') as f:
            json.dump(file_data, f, indent=config.json_indent)

        # Generate and save the tree text file
        generate_tree_structure_txt(file_data, config, output_file=str(TREE_FILE_PATH))

        logger.info(f"File tree generated successfully and saved to {TREE_FILE_PATH} and {FILE_STRUCTURE_JSON_PATH}")
    except Exception as e:
        logger.error(f"Error generating file tree: {e}")
        raise

# def generate_readme():
#     """
#     Generates the README.md file with links to notes and embeds the file tree.
#     """
#     logger.info("Generating README.md...")

#     readme_content = []
#     readme_content.append("# LeetCode\n")

#     # Embed the directory structure from TREE_FILE.txt
#     if TREE_FILE_PATH.exists():
#         readme_content.append("```txt")
#         with open(TREE_FILE_PATH, 'r', encoding='utf-8') as f:
#             tree_content = f.read()
#             # Remove the "Directory Structure" and "Summary" headers already generated by filetreegen
#             # as they are re-added by the custom README generation logic.
#             tree_content = re.sub(r"Directory Structure\n=+\n\n", "", tree_content)
#             tree_content = re.sub(r"Summary\n=+\n", "", tree_content)
#             readme_content.append(tree_content.strip())
#         readme_content.append("```\n")
#     else:
#         logger.warning(f"{TREE_FILE_PATH} not found. File tree will not be included in README.")

#     readme_content.append("## Problems\n")

#     # Group notes by problem number
#     problems_notes = {}
#     for note_type_dir in ["", "Short_Notes", "Atomic_Notes"]:
#         current_notes_path = NOTES_DIR / note_type_dir
#         if not current_notes_path.exists():
#             continue

#         for note_file in current_notes_path.glob("*.md"):
#             match = re.match(r"(\d+)-.*_(Atomic_Notes|Short_Notes|Notes)\.md", note_file.name)
#             if match:
#                 problem_number = match.group(1)
#                 note_category = match.group(2) # e.g., 'Notes', 'Short_Notes', 'Atomic_Notes'

#                 if problem_number not in problems_notes:
#                     problems_notes[problem_number] = {
#                         "complete_notes": None,
#                         "short_notes": None,
#                         "atomic_notes": None,
#                         "problem_name": ""
#                     }

#                 # Extract a more readable problem name from the file name
#                 # e.g., "1160-letter-tile-possibilities_Notes.md" -> "letter-tile-possibilities"
#                 name_parts = note_file.stem.split('-')
#                 if len(name_parts) > 1:
#                     problem_name_raw = '-'.join(name_parts[1:]).replace(f"_{note_category}", "").replace('_', ' ').strip()
#                     problems_notes[problem_number]["problem_name"] = problem_name_raw.title() # Capitalize words

#                 if note_category == "Notes":
#                     problems_notes[problem_number]["complete_notes"] = note_file.relative_to(CURRENT_DIR).as_posix()
#                 elif note_category == "Short_Notes":
#                     problems_notes[problem_number]["short_notes"] = note_file.relative_to(CURRENT_DIR).as_posix()
#                 elif note_category == "Atomic_Notes":
#                     problems_notes[problem_number]["atomic_notes"] = note_file.relative_to(CURRENT_DIR).as_posix()

#     # Sort problems by number
#     sorted_problem_numbers = sorted(problems_notes.keys(), key=int)

#     for p_num in sorted_problem_numbers:
#         problem_info = problems_notes[p_num]
#         problem_title = problem_info["problem_name"] if problem_info["problem_name"] else f"Problem {p_num}"
#         readme_content.append(f"### [{p_num}] {problem_title}\n")
        
#         if problem_info["complete_notes"]:
#             readme_content.append(f"- [Complete Notes]({problem_info['complete_notes']})\n")
#         if problem_info["short_notes"]:
#             readme_content.append(f"- [Short Notes]({problem_info['short_notes']})\n")
#         if problem_info["atomic_notes"]:
#             readme_content.append(f"- [Atomic Notes]({problem_info['atomic_notes']})\n")
#         readme_content.append("\n") # Add a newline for separation

#     try:
#         with open(README_FILE_PATH, 'w', encoding='utf-8') as f:
#             f.write("".join(readme_content))
#         logger.info(f"README.md generated successfully at {README_FILE_PATH}")
#     except Exception as e:
#         logger.error(f"Error writing README.md: {e}")
#         raise

def generate_readme():
    """
    Generates the README.md file with links to notes and embeds the file tree.
    Links for each problem are separated by '|'.
    """
    logger.info("Generating README.md...")

    readme_content = []
    readme_content.append("# LeetCode\n")

    readme_content.append("\n## Problems\n")

    # Group notes by problem number
    problems_notes = {}
    for note_type_dir in ["", "Short_Notes", "Atomic_Notes"]:
        current_notes_path = NOTES_DIR / note_type_dir
        if not current_notes_path.exists():
            continue

        for note_file in current_notes_path.glob("*.md"):
            # Adjusted regex to correctly capture the problem number and name without the suffix
            # Example: 1160-letter-tile-possibilities_Notes.md
            # Group 1: 1160
            # Group 2: letter-tile-possibilities
            # Group 3: Notes|Short_Notes|Atomic_Notes
            match = re.match(r"(\d+)-(.*?)_(Notes|Short_Notes|Atomic_Notes)\.md", note_file.name)
            if match:
                problem_number = match.group(1)
                problem_name_raw = match.group(2) # e.g., "letter-tile-possibilities"
                note_category = match.group(3) # e.g., 'Notes', 'Short_Notes', 'Atomic_Notes'

                if problem_number not in problems_notes:
                    problems_notes[problem_number] = {
                        "complete_notes": None,
                        "short_notes": None,
                        "atomic_notes": None,
                        "problem_name": ""
                    }

                # Capitalize words and replace hyphens with spaces for readability
                problems_notes[problem_number]["problem_name"] = problem_name_raw.replace('-', ' ').title()

                if note_category == "Notes":
                    problems_notes[problem_number]["complete_notes"] = note_file.relative_to(CURRENT_DIR).as_posix()
                elif note_category == "Short_Notes":
                    problems_notes[problem_number]["short_notes"] = note_file.relative_to(CURRENT_DIR).as_posix()
                elif note_category == "Atomic_Notes":
                    problems_notes[problem_number]["atomic_notes"] = note_file.relative_to(CURRENT_DIR).as_posix()

    # Sort problems by number
    sorted_problem_numbers = sorted(problems_notes.keys(), key=int)

    for p_num in sorted_problem_numbers:
        problem_info = problems_notes[p_num]
        problem_title = problem_info["problem_name"] if problem_info["problem_name"] else f"Problem {p_num}"
        readme_content.append(f"### [{p_num}] {problem_title}\n")
        
        links = []
        if problem_info["complete_notes"]:
            links.append(f"[Complete Notes]({problem_info['complete_notes']})")
        if problem_info["short_notes"]:
            links.append(f"[Short Notes]({problem_info['short_notes']})")
        if problem_info["atomic_notes"]:
            links.append(f"[Atomic Notes]({problem_info['atomic_notes']})")
        
        if links:
            readme_content.append(f"- {' | '.join(links)}\n") # MODIFIED LINE
        readme_content.append("\n") # Add a newline for separation
        
    readme_content.append("\n## File Structure\n")
    # Embed the directory structure from TREE_FILE.txt
    if TREE_FILE_PATH.exists():
        readme_content.append("```txt")
        with open(TREE_FILE_PATH, 'r', encoding='utf-8') as f:
            tree_content = f.read()
            # Remove the "Directory Structure" and "Summary" headers already generated by filetreegen
            # as they are re-added by the custom README generation logic.
            tree_content = re.sub(r"Directory Structure\n=+\n\n", "", tree_content)
            tree_content = re.sub(r"Summary\n=+\n", "", tree_content)
            readme_content.append(tree_content.strip())
        readme_content.append("\n```\n")
    else:
        logger.warning(f"{TREE_FILE_PATH} not found. File tree will not be included in README.")

    try:
        with open(README_FILE_PATH, 'w', encoding='utf-8') as f:
            f.write("".join(readme_content))
        logger.info(f"README.md generated successfully at {README_FILE_PATH}")
    except Exception as e:
        logger.error(f"Error writing README.md: {e}")
        raise

def main():
    """
    Orchestrates the notes generation, file tree generation, and README creation.
    """
    try:
        # Step 1: Run notes generation
        run_notes_generation()

        # Step 2: Generate file tree
        generate_file_tree()

        # Step 3: Generate README.md
        generate_readme()

        logger.info("Automation script finished successfully!")
    except Exception as e:
        logger.critical(f"Automation script failed: {e}")
        # Optionally re-raise the exception if you want the script to exit with an error code
        # raise

if __name__ == "__main__":
    main()