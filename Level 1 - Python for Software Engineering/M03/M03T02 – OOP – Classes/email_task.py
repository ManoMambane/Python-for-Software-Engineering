# --- OOP Email Simulator --- #

# --- Email Class --- #
class Email:
    def __init__(self, email_address, subject_line, email_content):
        # Initialize instance variables
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        # Update the read status of the email
        self.has_been_read = True


# --- Lists --- #
# List to store Email objects
inbox = []


# --- Functions --- #
def populate_inbox():
    # Create sample emails and add them to the inbox list
    sample_email_1 = Email(
        "support@hyperiondev.com",
        "Welcome to HyperionDev!",
        "Thank you for joining our bootcamp program!"
    )
    sample_email_2 = Email(
        "mentor@hyperiondev.com",
        "Great work on the bootcamp!",
        "Keep up the momentum on your Object-Oriented Programming tasks."
    )
    sample_email_3 = Email(
        "results@hyperiondev.com",
        "Your excellent marks!",
        "Congratulations on completing your assessment with high scores."
    )

    inbox.extend([sample_email_1, sample_email_2, sample_email_3])


def list_emails():
    # Loop through the inbox and print each email's index and subject line[cite: 11]
    print("\n--- Your Inbox ---")
    for index, email in enumerate(inbox):
        status = "Read" if email.has_been_read else "Unread"
        print(f"{index} {email.subject_line} ({status})")


def read_email(index):
    # Retrieve and display selected email details[cite: 12]
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\n{"="*40}")
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content:\n{email.email_content}")
        print(f"{"="*40}")

        # Mark as read using the class method
        email.mark_as_read()
        print(f"\nEmail from {email.email_address} marked as read.\n")
    else:
        print("\nInvalid email index. Please try again.")


# --- Main Application Logic --- #
# Populate initial inbox items[cite: 11]
populate_inbox()

while True:
    user_choice = input(
        """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
    ).strip()

    if user_choice == "1":
        if not inbox:
            print("\nYour inbox is empty.")
            continue

        list_emails()
        try:
            email_index = int(input("\nEnter the index of the email you would like to read: "))
            read_email(email_index)
        except ValueError:
            print("\nInvalid input. Please enter a valid numerical index.")

    elif user_choice == "2":
        # Access class instance variables directly to show unread email subjects[cite: 12]
        print("\n--- Unread Emails ---")
        unread_found = False
        for index, email in enumerate(inbox):
            if not email.has_been_read:
                print(f"{index} {email.subject_line}")
                unread_found = True

        if not unread_found:
            print("No unread emails in your inbox.")

    elif user_choice == "3":
        print("\nExiting Email Simulator. Goodbye!")
        break

    else:
        print("\nOops - incorrect input. Please select 1, 2, or 3.")