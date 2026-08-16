import os

def process_dob_file() -> None:
    """Reads DOB.txt from the script's folder, separates names and birthdates, and prints them."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "DOB.txt")

    names = []
    birthdates = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                tokens = line.strip().split()
                if len(tokens) >= 3:
                    names.append(" ".join(tokens[:2]))
                    birthdates.append(" ".join(tokens[2:]))

        print("Name")
        for name in names:
            print(name)

        print("\nBirthdate")
        for birthdate in birthdates:
            print(birthdate)

    except FileNotFoundError:
        print(f"Error: Could not find '{file_path}'. Check that 'DOB.txt' is saved in that folder.")


if __name__ == "__main__":
    process_dob_file()