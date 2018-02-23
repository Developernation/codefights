# To prepare his students for an upcoming game, the sports coach decides to try
# some new training drills. To begin with, he lines them up and starts with the
# following warm-up exercise: when the coach says 'L', he instructs the students
# to turn to the left. Alternatively, when he says 'R', they should turn to the
# right. Finally, when the coach says 'A', the students should turn around.
#
# Unfortunately some students (not all of them, but at least one) can't tell left
# from right, meaning they always turn right when they hear 'L' and left when they
# hear 'R'. The coach wants to know how many times the students end up facing the
# same direction.
#
# Given the list of commands the coach has given, count the number of such
# commands after which the students will be facing the same direction.
#
# Example
#
# For commands = "LLARL", the output should be
# lineUp(commands) = 3.
#
# Let's say that there are 4 students, and the second one can't tell left from
# right. In this case, only after the second, third and fifth commands will the
# students face the same direction.

#The number of times which the students are facing the same direction given the
#full sequence of commands.

def lineUp(cmd):
    cnt = 0
    flag = False
    if cmd == '':
        return 0
    for i in range(len(cmd)):
        temp = cmd[:i] #exclusive
        temp_count = temp.count('L') + temp.count('R') #calcs the number of Ls and Rs
        if cmd[i] is 'A' and i == 0:
            cnt += 1
            flag = True
        elif cmd[i] is 'A': #and 'i' is not 0
            if temp_count % 2 == 0 and temp_count != 0 and temp_count != 0:
                cnt += 1
                flag = True

            elif flag: #If 'A' and 'A':
                cnt += 1

        elif (cmd[i] is 'L') or (cmd[i] is 'R'):
            flag = False
            if temp_count % 2 != 0:
                cnt += 1
    return cnt




#         #Mapping of commands
#         bkw_cmd = ['R' if item =='L' else 'L' if item == 'R' else item for item in cmd]
