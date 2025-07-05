import os
from dataclasses import dataclass
from enum import Enum
from typing import Optional, List, Dict, Any, Tuple
from pathlib import Path
import logging
from google import genai
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

class NoteType(Enum):
    """Enum for different types of notes."""
    COMPLETE = "complete"
    SHORT = "short"
    ATOMIC = "atomic"

@dataclass
class ProblemData:
    """Container for problem statement and solution code."""
    problem_number: str
    problem_statement: str
    solution_code: str
    language: str

@dataclass
class Config:
    """Configuration class for the notes generator."""
    gemini_api_key: str
    gemini_model: str = "gemini-2.5-flash"
    submissions_base_path: str = "submissions"
    notes_base_path: str = "Notes"
    encoding: str = "utf-8"
    supported_code_extensions: List[str] = None
    
    def __post_init__(self):
        if self.supported_code_extensions is None:
            self.supported_code_extensions = ['.py', '.cpp', '.c', '.java', '.js']
    
    @classmethod
    def from_env(cls) -> 'Config':
        """Create configuration from environment variables."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        return cls(gemini_api_key=api_key)

class APIClient:
    """Handles API communications with Gemini."""
    
    def __init__(self, config: Config):
        self.config = config
        self.client = genai.Client(api_key=config.gemini_api_key)
    
    def get_response(self, prompt: str) -> Optional[str]:
        """
        Get a response from the Gemini API for a given prompt.
        
        Args:
            prompt (str): The input prompt to send to the Gemini API.
        
        Returns:
            Optional[str]: The response text from the Gemini API or None if error.
        """
        try:
            response = self.client.models.generate_content(
                model=self.config.gemini_model, 
                contents=prompt
            )
            return response.text
        except Exception as e:
            logger.error(f"Error getting API response: {e}")
            return None

class FileManager:
    """Handles file operations for the notes generator."""
    
    def __init__(self, config: Config):
        self.config = config
        self.notes_paths = {
            NoteType.COMPLETE: Path(config.notes_base_path),
            NoteType.SHORT: Path(config.notes_base_path) / "Short_Notes",
            NoteType.ATOMIC: Path(config.notes_base_path) / "Atomic_Notes"
        }
        self._ensure_directories()
    
    def _ensure_directories(self) -> None:
        """Ensure all required directories exist."""
        for path in self.notes_paths.values():
            path.mkdir(parents=True, exist_ok=True)
    
    def get_note_filepath(self, problem_number: str, note_type: NoteType) -> Path:
        """Get the filepath for a specific note type."""
        filename_map = {
            NoteType.COMPLETE: f"{problem_number}_Notes.md",
            NoteType.SHORT: f"{problem_number}_Short_Notes.md",
            NoteType.ATOMIC: f"{problem_number}_Atomic_Notes.md"
        }
        return self.notes_paths[note_type] / filename_map[note_type]
    
    def notes_exist(self, problem_number: str, note_types: List[NoteType] = None) -> bool:
        """Check if notes exist for a given problem number."""
        if note_types is None:
            note_types = list(NoteType)
        
        return all(
            self.get_note_filepath(problem_number, note_type).exists()
            for note_type in note_types
        )
    
    def read_problem_data(self, problem_folder_path: str) -> Optional[ProblemData]:
        """
        Read both problem statement and solution from a problem folder.
        
        Args:
            problem_folder_path (str): Path to the problem folder
            
        Returns:
            Optional[ProblemData]: Problem data if both files found, None otherwise
        """
        folder_path = Path(problem_folder_path)
        problem_number = folder_path.name
        
        if not folder_path.exists() or not folder_path.is_dir():
            logger.error(f"Problem folder {problem_folder_path} does not exist or is not a directory")
            return None
        
        # Find problem statement (.md file)
        problem_statement = self._read_problem_statement(folder_path)
        if not problem_statement:
            logger.warning(f"No problem statement found in {problem_folder_path}")
            return None
        
        # Find solution code (.py, .cpp, etc.)
        solution_data = self._read_solution_code(folder_path)
        if not solution_data:
            logger.warning(f"No solution code found in {problem_folder_path}")
            return None
        
        solution_code, language = solution_data
        
        return ProblemData(
            problem_number=problem_number,
            problem_statement=problem_statement,
            solution_code=solution_code,
            language=language
        )
    
    def _read_problem_statement(self, folder_path: Path) -> Optional[str]:
        """Read the problem statement from .md file."""
        md_files = list(folder_path.glob("*.md"))
        
        if not md_files:
            return None
        
        if len(md_files) > 1:
            logger.warning(f"Multiple .md files found in {folder_path}. Using the first one: {md_files[0].name}")
        
        try:
            return md_files[0].read_text(encoding=self.config.encoding)
        except Exception as e:
            logger.error(f"Error reading problem statement from {md_files[0]}: {e}")
            return None
    
    def _read_solution_code(self, folder_path: Path) -> Optional[Tuple[str, str]]:
        """Read the solution code and determine language."""
        code_files = []
        
        for ext in self.config.supported_code_extensions:
            code_files.extend(folder_path.glob(f"*{ext}"))
        
        if not code_files:
            return None
        
        if len(code_files) > 1:
            logger.warning(f"Multiple code files found in {folder_path}. Using the first one: {code_files[0].name}")
        
        code_file = code_files[0]
        language = self._get_language_from_extension(code_file.suffix)
        
        try:
            code_content = code_file.read_text(encoding=self.config.encoding)
            return code_content, language
        except Exception as e:
            logger.error(f"Error reading solution code from {code_file}: {e}")
            return None
    
    def _get_language_from_extension(self, extension: str) -> str:
        """Map file extension to programming language."""
        extension_map = {
            '.py': 'python',
            '.cpp': 'cpp',
            '.c': 'c',
            '.java': 'java',
            '.js': 'javascript',
            '.go': 'go',
            '.rs': 'rust'
        }
        return extension_map.get(extension.lower(), 'unknown')
    
    def save_notes(self, problem_number: str, content: str, note_type: NoteType) -> bool:
        """Save notes to file."""
        filepath = self.get_note_filepath(problem_number, note_type)
        
        try:
            filepath.write_text(content, encoding=self.config.encoding)
            logger.info(f"Successfully saved {note_type.value} notes for problem {problem_number}")
            return True
        except Exception as e:
            logger.error(f"Error saving {note_type.value} notes for problem {problem_number}: {e}")
            return False

class PromptManager:
    """Manages prompts for different note types."""
    
    @staticmethod
    def get_complete_notes_prompt(problem_data: ProblemData) -> str:
        """Generate prompt for complete notes using both problem statement and solution."""
        return f"""
        Given the following LeetCode problem {problem_data.problem_number} with its problem statement and solution code, generate complete, comprehensive notes.
        
        The notes should include:
        1. A clear problem summary (based on the provided problem statement).
        2. Explanation of all possible approaches, starting from naive to most optimized.
        3. Detailed explanation of the logic behind the provided solution and any alternative approaches.
        4. Time and Space Complexity analysis for each approach.
        5. Discuss any edge cases and how they are handled.
        6. Provide a clean, well-commented version of the optimal solution.
        7. Key insights and patterns that can be applied to similar problems.

        Problem Statement:
        ```
        {problem_data.problem_statement}
        ```

        Solution Code ({problem_data.language}):
        ```
        {problem_data.solution_code}
        ```
        """
    
    @staticmethod
    def get_short_notes_prompt(problem_data: ProblemData, complete_notes: str) -> str:
        """Generate prompt for short notes."""
        return f"""
        Based on the comprehensive notes for LeetCode problem {problem_data.problem_number},
        generate concise short notes suitable for quick revision. Focus on:
        1. Key problem characteristics and constraints.
        2. Core algorithmic approach used in the solution.
        3. Important time/space complexity facts.
        4. Critical edge cases to remember.
        5. Key patterns or techniques used.

        Problem Statement:
        ```
        {problem_data.problem_statement}
        ```

        Comprehensive Notes:
        ```
        {complete_notes}
        ```
        """
    
    @staticmethod
    def get_atomic_notes_prompt(problem_data: ProblemData, complete_notes: str, 
                               short_notes: str) -> str:
        """Generate prompt for atomic notes."""
        return f"""
        Based on the comprehensive and short notes for LeetCode problem {problem_data.problem_number},
        generate a set of atomic notes. Each atomic note should be a self-contained, single-concept
        idea, fact, or principle that can be used for spaced repetition learning.

        Format each atomic note as:
        - **Concept**: [Single concept or fact]
        - **Context**: [Brief context or application]
        - **Example**: [If applicable]

        Problem Number: {problem_data.problem_number}

        Comprehensive Notes:
        ```
        {complete_notes}
        ```

        Short Notes:
        ```
        {short_notes}
        ```
        """

class NotesGenerator:
    """Main class for generating notes."""
    
    def __init__(self, config: Config):
        self.config = config
        self.api_client = APIClient(config)
        self.file_manager = FileManager(config)
        self.prompt_manager = PromptManager()
    
    def generate_notes(self, problem_data: ProblemData, note_type: NoteType, 
                      **kwargs) -> Optional[str]:
        """Generate notes of a specific type."""
        prompt_methods = {
            NoteType.COMPLETE: lambda: self.prompt_manager.get_complete_notes_prompt(problem_data),
            NoteType.SHORT: lambda: self.prompt_manager.get_short_notes_prompt(
                problem_data, kwargs.get('complete_notes', '')
            ),
            NoteType.ATOMIC: lambda: self.prompt_manager.get_atomic_notes_prompt(
                problem_data, kwargs.get('complete_notes', ''), kwargs.get('short_notes', '')
            )
        }
        
        if note_type not in prompt_methods:
            logger.error(f"Unsupported note type: {note_type}")
            return None
        
        try:
            prompt = prompt_methods[note_type]()
            response = self.api_client.get_response(prompt)
            if response:
                logger.info(f"Successfully generated {note_type.value} notes for problem {problem_data.problem_number}")
            return response
        except Exception as e:
            logger.error(f"Error generating {note_type.value} notes for problem {problem_data.problem_number}: {e}")
            return None
    
    def process_problem(self, problem_data: ProblemData) -> Dict[NoteType, bool]:
        """Process a single problem and generate all types of notes."""
        results = {}
        
        # Generate complete notes
        complete_notes = self.generate_notes(problem_data, NoteType.COMPLETE)
        
        if complete_notes:
            results[NoteType.COMPLETE] = self.file_manager.save_notes(
                problem_data.problem_number, complete_notes, NoteType.COMPLETE
            )
        else:
            logger.error(f"Failed to generate complete notes for problem {problem_data.problem_number}")
            return results
        
        # Generate short notes
        short_notes = self.generate_notes(
            problem_data, NoteType.SHORT,
            complete_notes=complete_notes
        )
        
        if short_notes:
            results[NoteType.SHORT] = self.file_manager.save_notes(
                problem_data.problem_number, short_notes, NoteType.SHORT
            )
        else:
            logger.warning(f"Failed to generate short notes for problem {problem_data.problem_number}")
        
        # Generate atomic notes
        if short_notes:
            atomic_notes = self.generate_notes(
                problem_data, NoteType.ATOMIC,
                complete_notes=complete_notes,
                short_notes=short_notes
            )
            
            if atomic_notes:
                results[NoteType.ATOMIC] = self.file_manager.save_notes(
                    problem_data.problem_number, atomic_notes, NoteType.ATOMIC
                )
            else:
                logger.warning(f"Failed to generate atomic notes for problem {problem_data.problem_number}")
        
        return results
    
    def process_submissions_directory(self) -> Dict[str, Dict[NoteType, bool]]:
        """Process all problem folders in the base directory."""
        submissions_path = Path(self.config.submissions_base_path)
        
        if not submissions_path.exists():
            logger.error(f"Submissions directory '{submissions_path}' not found")
            return {}
        
        results = {}
        
        for folder_path in submissions_path.iterdir():
            if folder_path.is_dir():
                problem_number = folder_path.name
                
                logger.info(f"Processing problem {problem_number} from folder {folder_path.name}")
                
                # Check if notes already exist
                if self.file_manager.notes_exist(problem_number):
                    logger.info(f"Notes for problem {problem_number} already exist. Skipping.")
                    continue
                
                # Read problem data (statement + solution)
                problem_data = self.file_manager.read_problem_data(str(folder_path))
                if not problem_data:
                    logger.warning(f"Could not read problem data from {folder_path}. Skipping.")
                    continue
                
                # Process the problem
                results[problem_number] = self.process_problem(problem_data)
        
        return results

def main():
    """Main function to run the notes generator."""
    try:
        config = Config.from_env()
        generator = NotesGenerator(config)
        results = generator.process_submissions_directory()
        
        # Print summary
        total_problems = len(results)
        successful_problems = sum(1 for r in results.values() if any(r.values()))
        
        logger.info(f"Processing complete. {successful_problems}/{total_problems} problems processed successfully.")
        
    except Exception as e:
        logger.error(f"Application error: {e}")
        raise

if __name__ == "__main__":
    main()
