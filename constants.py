"""Contains the constants that are required for password generation files."""

import string

from english_words import get_english_words_set

MIN_LENGTH: int = 6
MAX_LENGTH: int = 15
RANGE_LENGTH: tuple[int, int] = (MIN_LENGTH, MAX_LENGTH)


MIN_PASSWORD_CHAR: int = 8
MAX_PASSWORD_CHAR: int = 128
RANGE_PASSWORD_CHAR: tuple[int, int] = (MIN_PASSWORD_CHAR, MAX_PASSWORD_CHAR)


MIN_PASSPHRASE_WORDS: int = 4
MAX_PASSPHRASE_WORDS: int = 20
RANGE_PASSPHRASE_WORDS: tuple[int, int] = (MIN_PASSPHRASE_WORDS, MAX_PASSPHRASE_WORDS)


MAX_SEPARATOR_LENGTH: int = 3
DEFAULT_SEPARATOR: str = "_"


RANDOM_CAPS_DISPLAY: list[str] = ["first", "last", "any-one", "all"]


CHARACTERS: dict[str, str] = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "numbers": string.digits,
    "special characters": string.punctuation,
}

WORDS: list[str] = sorted(get_english_words_set(sources=["web2"]))
