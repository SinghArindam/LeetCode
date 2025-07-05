import os
from dataclasses import dataclass
from enum import Enum
from typing import Optional, List, Dict, Any
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
class Config:
    """Configuration class for the notes generator."""
    gemini_api_key: str
    gemini_model: str = "gemini-2.5-flash"
    submissions_base_path: str = "submissions"
    notes_base_path: str = "Notes"
    encoding: str = "utf-8"
    
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
    
    def read_directory_code(self, directory_path: str) -> str:
        """Read all code from files in a directory."""
        all_code = []
        directory = Path(directory_path)
        
        if not directory.exists():
            logger.warning(f"Directory {directory_path} does not exist")
            return ""
        
        for file_path in directory.rglob("*"):
            if file_path.is_file():
                try:
                    content = file_path.read_text(encoding=self.config.encoding)
                    all_code.append(content)
                except Exception as e:
                    logger.error(f"Error reading file {file_path}: {e}")
        
        return "\n".join(all_code)
    
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
    def get_complete_notes_prompt(problem_number: str, problem_code: str, 
                                 existing_context: str = "") -> str:
        """Generate prompt for complete notes."""
        return f"""
        Given the following Python code for LeetCode problem {problem_number}, generate complete, comprehensive notes.
        The notes should include:
        1. A clear problem statement.
        2. Explanation of all approaches, starting from naive to most optimized.
        3. Detailed explanation of the logic behind each approach.
        4. Time and Space Complexity analysis for each approach.
        5. Discuss any edge cases and how they are handled.
        6. Provide a clean, well-commented code snippet for the most optimized solution.

        {existing_context}

        Problem Code:\n``````
        """
    
    @staticmethod
    def get_short_notes_prompt(problem_number: str, complete_notes: str) -> str:
        """Generate prompt for short notes."""
        return f"""
        Based on the following comprehensive notes for LeetCode problem {problem_number},
        generate concise short notes suitable for quick revision. Focus on:
        1. Key ideas for each approach.
        2. The core concept of the optimal solution.
        3. Important time/space complexity facts.
        4. Any crucial edge cases to remember.

        Comprehensive Notes:\n``````
        """
    
    @staticmethod
    def get_atomic_notes_prompt(problem_number: str, complete_notes: str, 
                               short_notes: str) -> str:
        """Generate prompt for atomic notes."""
        return f"""
        Based on the comprehensive and short notes provided for LeetCode problem {problem_number},
        generate a set of atomic notes. Each atomic note should be a self-contained, single-concept
        idea, fact, or principle. Format each atomic note clearly.

        Comprehensive Notes:\n``````

        Short Notes:\n``````
        """

class ProblemExtractor:
    """Extracts problem information from file paths."""
    
    @staticmethod
    def extract_problem_number(filepath: str) -> Optional[str]:
        """
        Extract problem number from file path.
        Assumes naming convention: "PROBLEM_NUMBER-PROBLEM_NAME"
        """
        parts = Path(filepath).parts
        for part in parts:
            if '-' in part and part[0].isdigit():
                return part.split('-')[0]
        return None

class NotesGenerator:
    """Main class for generating notes."""
    
    def __init__(self, config: Config):
        self.config = config
        self.api_client = APIClient(config)
        self.file_manager = FileManager(config)
        self.prompt_manager = PromptManager()
        self.problem_extractor = ProblemExtractor()
    
    def generate_notes(self, problem_number: str, note_type: NoteType, 
                      **kwargs) -> Optional[str]:
        """Generate notes of a specific type."""
        prompt_methods = {
            NoteType.COMPLETE: self.prompt_manager.get_complete_notes_prompt,
            NoteType.SHORT: self.prompt_manager.get_short_notes_prompt,
            NoteType.ATOMIC: self.prompt_manager.get_atomic_notes_prompt
        }
        
        if note_type not in prompt_methods:
            logger.error(f"Unsupported note type: {note_type}")
            return None
        
        try:
            prompt = prompt_methods[note_type](problem_number, **kwargs)
            response = self.api_client.get_response(prompt)
            if response:
                logger.info(f"Successfully generated {note_type.value} notes for problem {problem_number}")
            return response
        except Exception as e:
            logger.error(f"Error generating {note_type.value} notes for problem {problem_number}: {e}")
            return None
    
    def process_problem(self, problem_number: str, problem_code: str) -> Dict[NoteType, bool]:
        """Process a single problem and generate all types of notes."""
        results = {}
        
        # Generate complete notes
        complete_notes = self.generate_notes(
            problem_number, NoteType.COMPLETE, 
            problem_code=problem_code
        )
        
        if complete_notes:
            results[NoteType.COMPLETE] = self.file_manager.save_notes(
                problem_number, complete_notes, NoteType.COMPLETE
            )
        else:
            logger.error(f"Failed to generate complete notes for problem {problem_number}")
            return results
        
        # Generate short notes
        short_notes = self.generate_notes(
            problem_number, NoteType.SHORT,
            complete_notes=complete_notes
        )
        
        if short_notes:
            results[NoteType.SHORT] = self.file_manager.save_notes(
                problem_number, short_notes, NoteType.SHORT
            )
        else:
            logger.warning(f"Failed to generate short notes for problem {problem_number}")
        
        # Generate atomic notes
        if short_notes:  # Only generate atomic notes if short notes exist
            atomic_notes = self.generate_notes(
                problem_number, NoteType.ATOMIC,
                complete_notes=complete_notes,
                short_notes=short_notes
            )
            
            if atomic_notes:
                results[NoteType.ATOMIC] = self.file_manager.save_notes(
                    problem_number, atomic_notes, NoteType.ATOMIC
                )
            else:
                logger.warning(f"Failed to generate atomic notes for problem {problem_number}")
        
        return results
    
    def process_submissions_directory(self) -> Dict[str, Dict[NoteType, bool]]:
        """Process all submissions in the base directory."""
        submissions_path = Path(self.config.submissions_base_path)
        
        if not submissions_path.exists():
            logger.error(f"Submissions directory '{submissions_path}' not found")
            return {}
        
        results = {}
        
        for folder_path in submissions_path.iterdir():
            if folder_path.is_dir():
                problem_number = self.problem_extractor.extract_problem_number(str(folder_path))
                
                if not problem_number:
                    logger.warning(f"Could not extract problem number from {folder_path.name}")
                    continue
                
                logger.info(f"Processing problem {problem_number} from folder {folder_path.name}")
                
                # Check if notes already exist
                if self.file_manager.notes_exist(problem_number):
                    logger.info(f"Notes for problem {problem_number} already exist. Skipping.")
                    continue
                
                # Read code from directory
                problem_code = self.file_manager.read_directory_code(str(folder_path))
                if not problem_code:
                    logger.warning(f"No code found in {folder_path}. Skipping.")
                    continue
                
                # Process the problem
                results[problem_number] = self.process_problem(problem_number, problem_code)
        
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
