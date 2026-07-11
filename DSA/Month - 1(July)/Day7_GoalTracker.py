# Problem - Calculate average steps per day to reach goal
G = int(input("Enter your Goal: "))
D = int(input("Enter the work done: "))
N = int(input("Enter the number of days remaining to complete the goal: "))

# Average steps per day
average_steps = (G-D)//N
print(f"Average steps Needed per day to complete the goal in {N} remaining days are {average_steps} ")