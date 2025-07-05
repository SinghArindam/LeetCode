import os
from google import genai
from dotenv import load_dotenv
import shutil

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_gemini_response(prompt: str) -> str:
    """
    Get a response from the Gemini API for a given prompt.
    
    Args:
        prompt (str): The input prompt to send to the Gemini API.
    
    Returns:
        str: The response text from the Gemini API.
    """
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    return response.text

def get_problem_number_from_path(filepath):
    """
    Extracts the LeetCode problem number from a file path within a submission folder.
    Assumes the folder naming convention is "PROBLEM_NUMBER-PROBLEM_NAME".
    """
    parts = filepath.split(os.sep)
    for part in parts:
        if '-' in part and part[0].isdigit():
            return part.split('-')[0]
    return None

def check_existing_notes(problem_number):
    """
    Checks if complete, short, and atomic notes already exist for a given problem number.
    """
    base_path = "Notes"
    complete_notes_path = os.path.join(base_path, f"{problem_number}_Notes.md")
    short_notes_path = os.path.join(base_path, "Short_Notes", f"{problem_number}_Short_Notes.md")
    atomic_notes_path = os.path.join(base_path, "Atomic_Notes", f"{problem_number}_Atomic_Notes.md")

    return (os.path.exists(complete_notes_path) and
            os.path.exists(short_notes_path) and
            os.path.exists(atomic_notes_path))

def read_code_from_directory(directory_path):
    """
    Reads all code from all files in the specified directory and concatenates them into a single string.
    """
    all_code = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    all_code.append(f.read())
            except Exception as e:
                print(f"Error reading file {filepath}: {e}")
    return "\n".join(all_code)

def generate_notes_with_gemini(problem_number, problem_code, existing_notes_context=""):
    """
    Generates complete comprehensive notes for a LeetCode problem using Gemini.
    Includes all approaches and optimized solutions.
    """
    prompt = f"""
    Given the following Python code for LeetCode problem {problem_number}, generate complete, comprehensive notes.
    The notes should include:
    1. A clear problem statement.
    2. Explanation of all approaches, starting from naive to most optimized.
    3. Detailed explanation of the logic behind each approach.
    4. Time and Space Complexity analysis for each approach.
    5. Discuss any edge cases and how they are handled.
    6. Provide a clean, well-commented code snippet for the most optimized solution.

    {existing_notes_context}

    Problem Code:\n```python\n{problem_code}\n```
    """

    try:
        response = get_gemini_response(prompt)
        return response
    except Exception as e:
        print(f"Error generating complete notes for problem {problem_number}: {e}")
        return None

def generate_short_notes_with_gemini(problem_number, complete_notes_context):
    """
    Generates short revision notes from the comprehensive notes using Gemini.
    """
    prompt = f"""
    Based on the following comprehensive notes for LeetCode problem {problem_number},
    generate concise short notes suitable for quick revision. Focus on:
    1. Key ideas for each approach.
    2. The core concept of the optimal solution.
    3. Important time/space complexity facts.
    4. Any crucial edge cases to remember.

    Comprehensive Notes:\n```\n{complete_notes_context}\n```
    """

    try:
        response = get_gemini_response(prompt)
        return response
    except Exception as e:
        print(f"Error generating short notes for problem {problem_number}: {e}")
        return None

def generate_atomic_notes_with_gemini(problem_number, complete_notes_context, short_notes_context):
    """
    Generates atomic notes from the comprehensive and short notes using Gemini.
    Atomic notes should be highly focused, single-concept notes.
    """
    prompt = f"""
    Based on the comprehensive and short notes provided for LeetCode problem {problem_number},
    generate a set of atomic notes. Each atomic note should be a self-contained, single-concept
    idea, fact, or principle. Format each atomic note clearly.

    Comprehensive Notes:\n```\n{complete_notes_context}\n```

    Short Notes:\n```\n{short_notes_context}\n```
    """

    try:
        response = get_gemini_response(prompt)
        return response
    except Exception as e:
        print(f"Error generating atomic notes for problem {problem_number}: {e}")
        return None

def store_notes(problem_number, notes_content, notes_type="complete"):
    """
    Stores the generated notes in the appropriate directory.
    notes_type can be 'complete', 'short', or 'atomic'.
    """
    base_path = "Notes"
    os.makedirs(base_path, exist_ok=True)

    if notes_type == "complete":
        filepath = os.path.join(base_path, f"{problem_number}_Notes.md")
    elif notes_type == "short":
        short_notes_dir = os.path.join(base_path, "Short_Notes")
        os.makedirs(short_notes_dir, exist_ok=True)
        filepath = os.path.join(short_notes_dir, f"{problem_number}_Short_Notes.md")
    elif notes_type == "atomic":
        atomic_notes_dir = os.path.join(base_path, "Atomic_Notes")
        os.makedirs(atomic_notes_dir, exist_ok=True)
        filepath = os.path.join(atomic_notes_dir, f"{problem_number}_Atomic_Notes.md")
    else:
        print(f"Invalid notes type: {notes_type}")
        return

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(notes_content)
        print(f"Successfully stored {notes_type} notes for problem {problem_number} at {filepath}")
    except Exception as e:
        print(f"Error storing {notes_type} notes for problem {problem_number}: {e}")

def process_submission_folders(submissions_base_path="submissions"):
    """
    Iterates through all folders in the 'submissions' directory, processes each,
    generates notes, and stores them.
    """
    if not os.path.exists(submissions_base_path):
        print(f"Error: Submissions directory '{submissions_base_path}' not found.")
        return

    for folder_name in os.listdir(submissions_base_path):
        folder_path = os.path.join(submissions_base_path, folder_name)
        if os.path.isdir(folder_path):
            problem_number = get_problem_number_from_path(folder_path)
            if problem_number:
                print(f"Processing problem: {problem_number} from folder: {folder_name}")

                if check_existing_notes(problem_number):
                    print(f"Notes for problem {problem_number} already exist. Skipping.")
                    continue

                problem_code = read_code_from_directory(folder_path)
                if not problem_code:
                    print(f"No code found in {folder_path}. Skipping problem {problem_number}.")
                    continue

                # Generate complete notes
                complete_notes = generate_notes_with_gemini(problem_number, problem_code)
                if complete_notes:
                    store_notes(problem_number, complete_notes, "complete")
                    # Add complete notes to context for subsequent generations
                    complete_notes_context = f"Complete Notes for Problem {problem_number}:\n{complete_notes}"
                else:
                    complete_notes_context = ""
                    print(f"Failed to generate complete notes for problem {problem_number}. Skipping further note generation for this problem.")
                    continue

                # Generate short notes
                short_notes = generate_short_notes_with_gemini(problem_number, complete_notes_context)
                if short_notes:
                    store_notes(problem_number, short_notes, "short")
                    # Add short notes to context for atomic notes
                    short_notes_context = f"Short Notes for Problem {problem_number}:\n{short_notes}"
                else:
                    short_notes_context = ""
                    print(f"Failed to generate short notes for problem {problem_number}.")

                # Generate atomic notes
                atomic_notes = generate_atomic_notes_with_gemini(problem_number, complete_notes_context, short_notes_context)
                if atomic_notes:
                    store_notes(problem_number, atomic_notes, "atomic")
                else:
                    print(f"Failed to generate atomic notes for problem {problem_number}.")
            else:
                print(f"Could not determine problem number from folder: {folder_name}. Skipping.")

# Example Usage:
if __name__ == "__main__":
    # Create dummy submission folders and files for testing
    # In a real scenario, these would be your actual LeetCode submission folders
#     os.makedirs("submissions/1-TwoSum", exist_ok=True)
#     with open("submissions/1-TwoSum/solution.py", "w") as f:
#         f.write("""
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # Hash map approach
#         num_map = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_map:
#                 return [num_map[complement], i]
#             num_map[num] = i
#         return []
# """)

#     os.makedirs("submissions/2-AddTwoNumbers", exist_ok=True)
#     with open("submissions/2-AddTwoNumbers/solution.py", "w") as f:
#         f.write("""
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummyHead = ListNode(0)
#         curr = dummyHead
#         carry = 0
#         while l1 is not None or l2 is not None or carry != 0:
#             val1 = l1.val if l1 is not None else 0
#             val2 = l2.val if l2 is not None else 0

#             sum_vals = val1 + val2 + carry
#             carry = sum_vals // 10
#             new_node = ListNode(sum_vals % 10)
#             curr.next = new_node
#             curr = new_node

#             l1 = l1.next if l1 is not None else None
#             l2 = l2.next if l2 is not None else None
#         return dummyHead.next
# """)
    # Ensure the Notes directories exist
    os.makedirs("Notes/Short_Notes", exist_ok=True)
    os.makedirs("Notes/Atomic_Notes", exist_ok=True)

    process_submission_folders()

    # Clean up dummy folders and files after execution (optional)
    # shutil.rmtree("submissions")
    # shutil.rmtree("Notes")