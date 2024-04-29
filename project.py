"""Interface to generate passwords."""

from constants import QUIT_COMMANDS
from exceptions import QuitCommand
from password_generation import get_access_key, my_input


def main():
    """Interface to control all other functions.

    Serves as the main entry-point to the program. It presents a welcome message,
    provides instructions on how to quit, and enters loop where it generates passwords
    and prompts the user to generate another. The loop continues until the user chooses
    to quit the program.
    """

    print("\nHello, and welcome to the Password Generator! 🔑")
    print(
        f">>> To quit at any point, type: {", ".join(
            f'"{command}"' for command in QUIT_COMMANDS
            )}"
    )
    print()

    while True:
        try:
            access_key = get_access_key()
            print(f"\nThis is your password: {access_key}")

            if my_input("\nGenerate another? (y/n) ").lower() != "y":
                raise QuitCommand

        except QuitCommand as e:
            print(f"\n{e}")
            break

    print("\nHave a nice day ahead! 😄")


if __name__ == "__main__":
    main()
