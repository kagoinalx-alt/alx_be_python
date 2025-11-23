task = input("Input the task description: ")
priority = input(
    "What is the priority level for the task?(high, medium, low): ")
time_bound = input("Is the task time bound?(yes or no): ")

match task:
    case t if priority == "high" and time_bound == "yes":
        print(
            "Reminder:", f"{task}", "is a priority task that requires immediate attention today!")
    case t if priority == "high" and time_bound == "no":
        print(
            "Reminder:", f"{task}", "is a priority task that requires your completion!")
    case t if priority == "medium" and time_bound == "yes":
        print(
            "Note:", f"{task}", "is a task that requires your action soon!")
    case t if priority == "medium" and time_bound == "no":
        print(
            "Note:", f"{task}", "is a task. Consider completing it at your free time.")
    case t if priority == "low" and time_bound == "yes":
        print(
            "Note:", f"{task}", "is a task. Consider completing it at your free time.")
    case t if priority == "low" and time_bound == "no":
        print(
            "Note:", f"{task}", "is a task. Consider completing it at your free time.")
