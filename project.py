"""Interface to generate passwords."""

from password_generation import QuitCommand, my_input, get_access_key


def main():
    """Interface to control all other functions."""
    print("\nHello, and welcome to the Password Generator! 🔑")
    print(">>> Press 'quit' or 'exit' to exit the program at any point in time!")
    print()

    while True:
        try:
            access_key = get_access_key()
            print(f"\nThis is your password: {access_key}")

            if my_input("\nGenerate another? (y/n) ").lower() != "y":
                break

        except QuitCommand as e:
            print(f"\n{e}")
            break

    print("\nHave a nice day ahead! 😄")


if __name__ == "__main__":
    main()
