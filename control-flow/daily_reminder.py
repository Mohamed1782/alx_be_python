# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task’s priority
priority = input("Priority (high/medium/low): ").strip().lower()

# Prompt if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task based on priority and time sensitivity
reminder = f"Reminder: '{task}' is a {priority} priority task."

match priority:
    case "high":
        reminder += " This task is very important."
    case "medium":
        reminder += " This task has a moderate level of importance."
    case "low":
        reminder += " This task has a low level of importance."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"
elif time_bound == "no":
    reminder += " Consider completing it when you have free time."
else:
    reminder = "Invalid input for time-bound. Please enter yes or no."

# Provide a customized reminder
print(reminder)
