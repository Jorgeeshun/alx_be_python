# daily_reminder.py

def main():
    # Prompt for a single task
    task = input("Enter your task: ").strip()
    
    # Prompt for the task's priority
    priority = input("Priority (high/medium/low): ").strip().lower()
    
    # Prompt to check if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    
    # Provide a customized reminder based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task."
        case _:
            reminder = f"'{task}' has an unspecified priority."
    
    # Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " It requires immediate attention today!"
    elif time_bound == "no":
        reminder += " Consider completing it at your convenience."
    else:
        reminder += " (Time-bound status unknown.)"
    
    # Print the reminder
    print("Reminder:", reminder)

if __name__ == "__main__":
    main()
