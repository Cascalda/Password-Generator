"""Tests password_generation.py."""

import random
import pytest

from constants import MIN_LENGTH, MAX_LENGTH, WORDS
from password_generation import validate_length


# pylint: disable=missing-function-docstring


# ===== Helper Functions Tests =====
@pytest.mark.parametrize("length", (str(_) for _ in range(MIN_LENGTH, MAX_LENGTH + 1)))
def test_validate_length_within_range(length):
    assert validate_length(length, MIN_LENGTH, MAX_LENGTH) == int(length)


@pytest.mark.parametrize(
    "length",
    (
        [str(_) for _ in range(0, MIN_LENGTH)]
        + [str(_) for _ in range(MAX_LENGTH + 1, MAX_LENGTH + 2)]
    ),
)
def test_validate_length_outside_range(length):
    with pytest.raises(ValueError, match="Invalid length. Please try again."):
        validate_length(length, MIN_LENGTH, MAX_LENGTH)


@pytest.mark.parametrize("non_integer", random.choices(WORDS, k=10))
def test_validate_length_with_invalid_input(non_integer):
    with pytest.raises(ValueError, match="Only integers accepted. Please try again."):
        validate_length(non_integer, MIN_LENGTH, MAX_LENGTH)


if __name__ == "__main__":
    pytest.main()
