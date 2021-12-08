# N. told his two teammates that he was going to solve all given problems
# at the subregional contest, even if the teammates wouldn’t show up at the competition.
# The teammates didn’t believe N. so he told them the plan how he was going to do this.
# During the first hour he wants to solve f problems. If there is still some time left
# to the end of the first hour, N. will simply walk along the hall. Beginning
# from the second hour N. wants to spend exactly 45 minutes on each of the problems left.
# If the plan is a success, will N. be able to solve all 12 given problems for 5 hours?

time_h = 5
time_min = time_h * 60
tasks = 12
f = int(input("Enter the number of tasks in the first hour: "))
i = 0
result = ''

while i == 0:
    if f >= 12:
        print("Wrong number. Number must be <= 12.")
    else:
        i = 1
        if (tasks - f) * 45 <= (time_min - 60):
            result ='Yes'
        else:
            result = 'No'
print(result)
