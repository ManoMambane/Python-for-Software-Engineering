import os
from datetime import datetime


def load_users(file_path="user.txt"):
    users = {}
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("admin, adm1n\n")

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                username, password = line.split(", ")
                users[username] = password
    return users


def load_tasks(file_path="tasks.txt"):
    tasks = []
    if not os.path.exists(file_path):
        open(file_path, "w").close()
        return tasks

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split("; ")
                if len(parts) == 6:
                    tasks.append({
                        "username": parts[0],
                        "title": parts[1],
                        "description": parts[2],
                        "assigned_date": parts[3],
                        "due_date": parts[4],
                        "completed": parts[5]
                    })
    return tasks


def save_tasks(tasks, file_path="tasks.txt"):
    with open(file_path, "w") as file:
        for t in tasks:
            line = f"{t['username']}; {t['title']}; {t['description']}; {t['assigned_date']}; {t['due_date']}; {t['completed']}\n"
            file.write(line)


def display_task_formatted(index, task):
    print("------------------------------------------------------------------")
    print(f"Task Number:      {index}")
    print(f"Task:             {task['title']}")
    print(f"Assigned to:      {task['username']}")
    print(f"Date assigned:    {task['assigned_date']}")
    print(f"Due date:         {task['due_date']}")
    print(f"Task Completed:   {task['completed']}")
    print(f"Task description:\n {task['description']}")
    print("------------------------------------------------------------------")


def reg_user(users, file_path="user.txt"):
    while True:
        new_username = input("Enter new username: ").strip()
        if new_username in users:
            print("Error: Username already exists. Please choose a different username.")
            continue
        if not new_username:
            print("Error: Username cannot be blank.")
            continue
        break

    while True:
        new_password = input("Enter new password: ").strip()
        confirm_password = input("Confirm new password: ").strip()

        if new_password == confirm_password:
            users[new_username] = new_password
            with open(file_path, "a") as file:
                file.write(f"{new_username}, {new_password}\n")
            print(f"User '{new_username}' successfully registered!")
            break
        else:
            print("Error: Passwords do not match. Please try again.")


def add_task(tasks, users):
    while True:
        assigned_user = input("Enter username of the person assigned to task: ").strip()
        if assigned_user in users:
            break
        print("Error: User does not exist. Please enter a valid registered username.")

    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    
    while True:
        due_date_str = input("Enter due date (e.g., 2026-12-31 or 31 Dec 2026): ").strip()
        if due_date_str:
            break
        print("Error: Due date cannot be empty.")

    assigned_date_str = datetime.now().strftime("%d %b %Y")

    new_task = {
        "username": assigned_user,
        "title": title,
        "description": description,
        "assigned_date": assigned_date_str,
        "due_date": due_date_str,
        "completed": "No"
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("Task successfully added!")


def view_all(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n======================= ALL TASKS =======================")
    for idx, task in enumerate(tasks, 1):
        display_task_formatted(idx, task)


def get_valid_task_number(user_tasks, total_user_tasks):
    user_input = input("\nEnter task number to edit/complete, or '-1' to return to menu: ").strip()

    if user_input == "-1":
        return -1

    try:
        val = int(user_input)
        if 1 <= val <= total_user_tasks:
            return val - 1
        else:
            print("Error: Task number out of range.")
    except ValueError:
        print("Error: Invalid input. Please enter an integer value.")

    return get_valid_task_number(user_tasks, total_user_tasks)


def view_mine(tasks, current_user, users):
    while True:
        user_tasks = [t for t in tasks if t["username"] == current_user]

        if not user_tasks:
            print("\nYou have no assigned tasks.")
            return

        print(f"\n=================== TASKS FOR {current_user.upper()} ===================")
        for idx, task in enumerate(user_tasks, 1):
            display_task_formatted(idx, task)

        selected_index = get_valid_task_number(user_tasks, len(user_tasks))

        if selected_index == -1:
            break

        selected_task = user_tasks[selected_index]

        print("\nTask Options:")
        print("1 - Mark as complete")
        print("2 - Edit task")
        action = input("Select an option (1 or 2): ").strip()

        if action == "1":
            selected_task["completed"] = "Yes"
            save_tasks(tasks)
            print("Task marked as complete!")
        elif action == "2":
            if selected_task["completed"] == "Yes":
                print("Error: Completed tasks cannot be edited.")
            else:
                print("\nEdit Options:")
                print("1 - Edit assigned username")
                print("2 - Edit due date")
                print("3 - Edit both")
                edit_choice = input("Select choice: ").strip()

                if edit_choice in ("1", "3"):
                    new_user = input("Enter new assigned username: ").strip()
                    if new_user in users:
                        selected_task["username"] = new_user
                    else:
                        print("Error: User does not exist. Username update skipped.")

                if edit_choice in ("2", "3"):
                    new_due = input("Enter new due date: ").strip()
                    if new_due:
                        selected_task["due_date"] = new_due

                save_tasks(tasks)
                print("Task updated successfully!")
        else:
            print("Invalid selection.")


def view_completed(tasks):
    completed_tasks = [t for t in tasks if t["completed"] == "Yes"]
    if not completed_tasks:
        print("\nNo completed tasks found.")
        return

    print("\n=================== COMPLETED TASKS ===================")
    for idx, task in enumerate(completed_tasks, 1):
        display_task_formatted(idx, task)


def delete_task(tasks):
    if not tasks:
        print("\nNo tasks available to delete.")
        return

    view_all(tasks)
    try:
        task_num = int(input("\nEnter the Task Number you want to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted successfully!")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")


def generate_reports(tasks, users):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if t["completed"] == "Yes")
    uncompleted_tasks = total_tasks - completed_tasks

    overdue_tasks = 0
    today = datetime.now()
    for t in tasks:
        if t["completed"] == "No":
            try:
                due_dt = datetime.strptime(t["due_date"], "%d %b %Y")
                if due_dt < today:
                    overdue_tasks += 1
            except ValueError:
                pass

    pct_incomplete = (uncompleted_tasks / total_tasks * 100) if total_tasks > 0 else 0
    pct_overdue = (overdue_tasks / total_tasks * 100) if total_tasks > 0 else 0

    with open("task_overview.txt", "w") as file:
        file.write("================ TASK OVERVIEW ================\n")
        file.write(f"Total tasks:                         {total_tasks}\n")
        file.write(f"Completed tasks:                     {completed_tasks}\n")
        file.write(f"Uncompleted tasks:                   {uncompleted_tasks}\n")
        file.write(f"Overdue uncompleted tasks:           {overdue_tasks}\n")
        file.write(f"Percentage incomplete:               {pct_incomplete:.2f}%\n")
        file.write(f"Percentage overdue:                  {pct_overdue:.2f}%\n")

    total_users = len(users)
    with open("user_overview.txt", "w") as file:
        file.write("================ USER OVERVIEW ================\n")
        file.write(f"Total registered users:              {total_users}\n")
        file.write(f"Total tasks tracked:                 {total_tasks}\n\n")

        for user in users:
            u_tasks = [t for t in tasks if t["username"] == user]
            u_count = len(u_tasks)
            u_pct_total = (u_count / total_tasks * 100) if total_tasks > 0 else 0
            
            u_completed = sum(1 for t in u_tasks if t["completed"] == "Yes")
            u_pct_completed = (u_completed / u_count * 100) if u_count > 0 else 0
            
            u_uncompleted = u_count - u_completed
            u_pct_uncompleted = (u_uncompleted / u_count * 100) if u_count > 0 else 0

            u_overdue = 0
            for t in u_tasks:
                if t["completed"] == "No":
                    try:
                        due_dt = datetime.strptime(t["due_date"], "%d %b %Y")
                        if due_dt < today:
                            u_overdue += 1
                    except ValueError:
                        pass
            u_pct_overdue = (u_overdue / u_count * 100) if u_count > 0 else 0

            file.write(f"User: {user}\n")
            file.write(f"  - Tasks assigned:                  {u_count}\n")
            file.write(f"  - % of total tasks:                 {u_pct_total:.2f}%\n")
            file.write(f"  - % assigned tasks completed:       {u_pct_completed:.2f}%\n")
            file.write(f"  - % assigned tasks to complete:     {u_pct_uncompleted:.2f}%\n")
            file.write(f"  - % assigned tasks overdue:         {u_pct_overdue:.2f}%\n")
            file.write("-" * 48 + "\n")

    print("\nReports successfully generated (task_overview.txt & user_overview.txt).")


def display_statistics(tasks, users):
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        generate_reports(tasks, users)

    print("\n" + "=" * 50)
    with open("task_overview.txt", "r") as f:
        print(f.read())

    print("=" * 50)
    with open("user_overview.txt", "r") as f:
        print(f.read())


def main():
    users = load_users()
    tasks = load_tasks()

    print("=================== TASK MANAGER LOGIN ===================")
    logged_in_user = None

    while not logged_in_user:
        username_input = input("Enter username: ").strip()
        password_input = input("Enter password: ").strip()

        if username_input in users and users[username_input] == password_input:
            logged_in_user = username_input
            print(f"\nLogin successful! Welcome, {logged_in_user}.")
        else:
            print("Error: Invalid username or password. Please try again.\n")

    while True:
        print("\nPlease select one of the following options:")
        if logged_in_user == "admin":
            print("r   - register user")
            print("a   - add task")
            print("va  - view all tasks")
            print("vm  - view my tasks")
            print("vc  - view completed tasks")
            print("del - delete a task")
            print("gr  - generate reports")
            print("ds  - display statistics")
            print("e   - exit")
        else:
            print("a   - add task")
            print("va  - view all tasks")
            print("vm  - view my tasks")
            print("e   - exit")

        choice = input(": ").strip().lower()

        if choice == "r" and logged_in_user == "admin":
            reg_user(users)
        elif choice == "a":
            add_task(tasks, users)
        elif choice == "va":
            view_all(tasks)
        elif choice == "vm":
            view_mine(tasks, logged_in_user, users)
        elif choice == "vc" and logged_in_user == "admin":
            view_completed(tasks)
        elif choice == "del" and logged_in_user == "admin":
            delete_task(tasks)
        elif choice == "gr" and logged_in_user == "admin":
            generate_reports(tasks, users)
        elif choice == "ds" and logged_in_user == "admin":
            display_statistics(tasks, users)
        elif choice == "e":
            print("\nGoodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()