import os

def generate_student_register() -> None:
    """Prompts for student IDs and generates an attendance signature register."""
    # Determine the folder where this script is saved
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "reg_form.txt")

    # Prompt user for the number of registering students
    while True:
        try:
            num_students = int(input("How many students are registering? "))
            if num_students > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Write registration form with ID numbers and signature lines
    with open(file_path, "w", encoding="utf-8") as file:
        for i in range(1, num_students + 1):
            student_id = input(f"Enter ID number for student {i}: ").strip()
            file.write(f"{student_id} ...................................\n")

    print(f"\nRegistration form successfully created at: {file_path}")


if __name__ == "__main__":
    generate_student_register()