# Personal Daily Reminder

task = input("Input the task description: ")
priority = input(
    "What is the priority level for the task? (high, medium, low): ")
time_bound = input("Is the task time bound? (yes or no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(
                f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(
                f"Reminder: '{task}' is a high priority task that requires your completion!")

    case "medium":
        if time_bound == "yes":
            print(
                f"Note: '{task}' is a medium priority task that requires your action soon!")
        else:
            print(
                f"Note: '{task}' is a task. Consider completing it in your free time.")

    case "low":
        if time_bound == "yes":
            print(
                f"Note: '{task}' is a low priority task, but since it's time-bound, try to handle it today.")
        else:
            print(
                f"Note: '{task}' is a low priority task. You can complete it whenever possible.")

    case _:
        print("Invalid priority level entered.")
