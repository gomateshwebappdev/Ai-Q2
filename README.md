# AI-Powered Code Generation and Debugging Assistant

## Project Title
AI-Powered Code Generation and Debugging Assistant

## Objective
Develop a simple Python application that demonstrates how Generative AI can help generate code, explain program logic, identify programming errors, debug faulty code, and validate the corrected solution. This project satisfies the requirements of Q.4 (25 marks) from the MCA Generative Artificial Intelligence Lab practical examination.

## Technology Stack
- **Programming Language**: Python 3.x
- **Code Editor**: Visual Studio Code
- **Generative AI Tool**: ChatGPT or OpenCode
- **Execution Environment**: Python terminal (Windows)
- **Testing**: Python's built-in `unittest` module
- **Documentation**: Markdown and text files
- **Dependencies**: Python standard library only (no external packages)

## Folder Structure
```
ai-code-generation-debugging-assistant/
├── main.py              # Corrected working implementation
├── buggy_version.py     # Deliberately buggy code for debugging exercise
├── test_cases.py        # Unit tests using unittest module
├── AI_prompts.txt       # Three practical AI prompts
├── debugging_report.md  # Debugging report document
├── README.md            # This file - project documentation
└── screenshots/         # Screenshot checklist for practical submission
    └── (store actual screenshots here)
```

### File Purpose Explanation

| File | Purpose |
|------|---------|
| **main.py** | The corrected, working implementation of the String Reversal and Palindrome Checker. Uses functions for modular code and handles edge cases. |
| **buggy_version.py** | Contains the same program with an intentional bug (case-sensitive palindrome comparison). Used for debugging exercise. |
| **test_cases.py** | Unit tests using Python's `unittest` module. Verifies function results with at least 3 test cases plus edge cases. |
| **AI_prompts.txt** | Three practical prompts used with Generative AI for code generation, explanation, and debugging. |
| **debugging_report.md** | Formal debugging report documenting the bug, its cause, the AI-assisted correction, and test results. |
| **README.md** | Project documentation - this file. Contains title, objective, technology stack, folder structure, installation/execution instructions, and testing instructions. |
| **screenshots/** | Directory for storing actual screenshots of program execution for practical submission. |

## Prerequisites
- Python 3.x installed on Windows
- Visual Studio Code (optional, for code editing)
- No external packages required - uses Python standard library only
- Basic understanding of Python input/output, functions, and string slicing

## Installation and Execution Instructions

### Step 1: Open Visual Studio Code
1. Navigate to the project folder:
   ```
   cd C:\Users\<YourUsername>\ai-code-generation-debugging-assistant
   ```

### Step 2: Run the Main Program
**Option A: Using `python` command**
```
python main.py
```

**Option B: Using `py` command (if `python` is unavailable)**
```
py main.py
```

### Step 3: Run the Unit Tests
```
python -m unittest -v test_cases.py
```

**Expected test output:**
```
......................
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```

### Step 3: Run the Buggy Version (for debugging exercise)
```
python buggy_version.py
```

## Sample Output

### Running main.py with input "madam":
```
============================================================
STRING REVERSAL AND PALINDROME CHECKER
============================================================

Enter a string: madam

Original string: 'madam'
Reversed string: 'madam'
'madam' IS a palindrome!

============================================================
Program completed. Thank you for using the assistant!
============================================================
```

### Running main.py with input "hello":
```
============================================================
STRING REVERSAL AND PALINDROME CHECKER
============================================================

Enter a string: hello

Original string: 'hello'
Reversed string: 'olleh'
'hello' is NOT a palindrome!

============================================================
Program completed. Thank you for using the assistant!
============================================================
```

### Running main.py with input "MADAM" (case-insensitive):
```
============================================================
STRING REVERSAL AND PALINDROME CHECKER
============================================================

Enter a string: MADAM

Original string: 'MADAM'
Reversed string: 'MADAM'
'MADAM' IS a palindrome!

============================================================
Program completed. Thank you for using the assistant!
============================================================
```

### Running main.py with empty input:
```
============================================================
STRING REVERSAL AND PALINDROME CHECKER
============================================================

Enter a string: 

Original string: ''
No input provided for reversal.
Cannot check palindrome for empty input.

============================================================
Program completed. Thank you for using the assistant!
============================================================
```

## Testing Instructions

### Run All Unit Tests
```
python -m unittest -v test_cases.py
```

**Test Coverage:**
1. `test_palindrome_madam` - verifies "madam" is recognized as palindrome
2. `test_palindrome_hello` - verifies "hello" is NOT a palindrome
3. `test_palindrome_level` - verifies "level" is recognized as palindrome
4. `test_uppercase_input` - verifies case-insensitive handling (MADAM, Level)
5. `test_empty_input` - verifies empty input returns False
6. `test_single_character` - verifies single char "a" is palindrome
7. `test_reversal_madam` - verifies reverse of "madam" is "madam"
8. `test_reversal_hello` - verifies reverse of "hello" is "olleh"

### Individual Test Run
To run a specific test:
```
python -m unittest -v test_cases.py TestStringReversalAndPalindrome.test_palindrome_madam
```

## Expected Test Summary
When all 8 tests are run, the output should show:
- All 8 tests pass
- `Ran 8 tests in 0.001s`
- `OK`
- This verifies that the implementation correctly handles palindromes,
  non-palindromes, uppercase input, empty input, and string reversal.

## Conclusion
This project demonstrates how a simple Python program can be created to reverse
a string and check for palindromes, with proper handling of edge cases like
empty input and case-insensitive comparison. The integration of Generative AI
prompts shows how AI assistants can help generate code, explain program logic,
and assist in debugging. The project is suitable for a 30-minute MCA practical
examination and uses only Python standard library, making it accessible without
requiring package installation or API keys.

---

**Generated for**: MCA Generative Artificial Intelligence Lab Practical Examination  
**Course Code**: Q.4 (25 marks)  
**Date**: 2026