# Remarks

This project took months to make despite being a simple password generator. Most of the work done was through refactoring to make the code more readable and maintainable, as well as providing good user experience via the terminal.

## Lessons learnt

- `Type annotations` can really help one spot bugs in intended program flow, especially as python is dynamically typed.
  - Marking it for empty lists, tuples, dictionaries etc. is also very useful for explaining what those variables intend to contain.
- Organising functions in the `logical order of dependence` really helps build a reliable mental model of how everything works, with reliable speed.
- Spliting workload into `modular functions` makes it easier to do isolated testing, and helps mark out logical steps to the end goal.
- User of python linters and formatters to easily make code pretty and catch errors (Pylint, Black, Flake8, Pyright)
  - Recently switched to [Ruff](https://github.com/astral-sh/ruff), since it is extremely fast and is compatible with Black.
- Use of `CONSTANTS` to further improve code logic.
- Use of docstrings to improve quick understanding of code.
- Use of `wrapper functions` and `decorators` to extend the functionality of built-in functions, in this case: input()
  - On the same note, reducing additional complexity of code for my simple use-case makes the code much more readable and less so unnecessarily complex
- Use of custom `Exceptions` to handle the specific exception in my program, in this case: quitting prematurely
- Giving `clear prompts and instructions` to users help improve user experience
- Not abstracting too early as it introduces too much _complexity_ that slows development, add it when its needed.

## Further Research and Improvements

- Parallelism (Attempted to use threading to implement the quitting feature but I could not make it work)
- Virtual Environments
- Using branches to modify instead of the main branch, especially useful if collaborating, but still a good practice to easily go back to the unedited version for comparison
