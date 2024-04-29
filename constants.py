"""Contains the constants that are required for password generation files."""

import string

from english_words import get_english_words_set


QUIT_COMMANDS = ("quit", "q", "exit", "e")


MIN_LENGTH = 6
MAX_LENGTH = 15
RANGE_LENGTH = (MIN_LENGTH, MAX_LENGTH)


MIN_PASSWORD_CHAR = 8
MAX_PASSWORD_CHAR = 128
RANGE_PASSWORD_CHAR = (MIN_PASSWORD_CHAR, MAX_PASSWORD_CHAR)


MIN_PASSPHRASE_WORDS = 4
MAX_PASSPHRASE_WORDS = 20
RANGE_PASSPHRASE_WORDS = (MIN_PASSPHRASE_WORDS, MAX_PASSPHRASE_WORDS)


MAX_SEPARATOR_LENGTH = 3
DEFAULT_SEPARATOR = "_"


RANDOM_CAPS_DISPLAY = ("first", "last", "any-one", "all")


CHARACTERS = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "numbers": string.digits,
    "special characters": string.punctuation,
}

WORDS = sorted(get_english_words_set(sources=["web2"]))
