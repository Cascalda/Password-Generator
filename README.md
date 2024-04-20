## CS50 Final Project: Password Generator

### Description
A simple terminal-based password generator that gives you a fair bit of customisation. You can also make a passphrase with this one.

**Getting Started**
To get started, run [`project.py`](project.py)

### Contains
#### [**Interface**](project.py)
Where you can call the password generators, to provide a password/passphrase for your use.

- **`main()` function:**
- Contains a welcome and farewell message. A while loop that gets and provides your password, with another prompt to end the program after generation, or to catch the `QuitCommand` Exception to end it prematurely.

#### [**Password Generator**](password_generation.py)
Functions grouped according to their categories.

**Wrapper:**
- Contains the `handle_quit` wrapper for built-in function `input()` via `my_input()` self-declared function. Used to raise `QuitCommand` custom Exception.

**Helper functions:**
- `validate_length`: Provide simple input validation for password/passphrase length for `get_valid_length`.
- `get_valid_length`: Gets the valid length from the user according to `access_key_range` variable.
- `get_character_pool`: Asks the user for characters to include in their password and include them into the character pool.
- `get_separator`: Gets a simple separator up to 3 characters in length. Defaults to "_".
- `get_random_uppercase_flag`: Gets flags from the user for the Random Capitalisation feature for passphrases.
- `randomly_capitalise`: Randomly capitalises each word according to `get_random_uppercase_flag`.

**Main functions:**
- `generate_password`: Prompts the user for features to include in their password and provides them with one.
- `generate_passphrase`: Prompts the user for features to include in their passphrase and provides them with one.
- `get_access_key`: Prompts the user to choose between generating a password and a passphrase.

**Entry Point:**
- Contains `main()` that runs only if we are running the library itself. Right now it is the same as `main()` in `project.py`.

#### [**Constants**](constants.py)
- Contains all the CONSTANTS that I've factored out to use across multiple files.

#### [**Exceptions:**](exceptions.py)
- `QuitCommand`, meant to signal that the user wants to quit the program.
- `InvalidInputError`, meant to signal that an input has an invalid value.
    - `InvalidLengthError`, meant to signal that an input has an invalid length.
    - `InvalidTypeError`, meant to signal that an input has an invalid type.

#### [**Tests**](test_password_generation.py)
- Contains some tests, not fully comprehensive as I do not know how to test password generation.
- Therefore it only contains length validation checks
- Uses pytest with parametrisation

## Remarks
This project took months to make despite being a simple password generator. Most of the work done was through refactoring to make the code more readable and maintainable, as well as providing good user experience via the terminal.

Lessons learnt:
- `Type annotations` can really help one spot bugs in intended program flow, especially as python is dynamically typed.
- Organising functions in the `logical order of dependence` really helps build a reliable mental model of how everything works, with reliable speed.
- Spliting workload into `modular functions` makes it easier to do isolated testing, and helps mark out logical steps to the end goal.
- User of python linters and formatters to easily make code pretty and catch errors (Pylint, Black, Flake8, Pyright)
- Use of `CONSTANTS` to further improve code logic.
- Use of docstrings to improve quick understanding of code.
- Use of `wrapper functions` and `decorators` to extend the functionality of built-in functions, in this case: input()
- Use of custom `Exceptions` to handle the specific exception in my program, in this case: quitting prematurely
- Giving `clear prompts and instructions` to users help improve user experience

Further research required:
- Parallelism  (Attempted to use threading to implement the quitting feature but I could not make it work)
- Virtual Environments
