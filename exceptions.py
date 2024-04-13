"""Exceptions raised when user provides an input."""


class QuitCommand(Exception):
    """Exception raised when the quit command is detected."""

    def __init__(self, message: str = "Exiting Program..."):
        super().__init__(message)


class InvalidInputError(Exception):
    """Exception raised when the user gives an invalid input."""

    def __init__(self, message: str = "Invalid input. Please try again."):
        super().__init__(message)


class InvalidLengthError(InvalidInputError):
    """Exception raised when the user gives invalid length of input."""

    def __init__(self, message: str = "Invalid length. Please try again."):
        super().__init__(message)


class InvalidTypeError(InvalidInputError):
    """Exception raised when the user gives invalid type of input."""

    def __init__(self, message: str = "Only integers accepted. Please try again."):
        super().__init__(message)
