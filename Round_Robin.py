time_quantum = 2
print("Enter burst time of processes as list separated by spaces:")
burst_time = [int(x) for x in input().split()]
rem_bt = burst_time
print(rem_bt)
waiting_time = []
time = 0
i = 0
for i in range(len(rem_bt)):
    while(rem_bt[i]>0):
        if (rem_bt[i] > time_quantum):
            time = time + time_quantum
            rem_bt[i] = rem_bt[i] - time_quantum
            print(rem_bt)
        else:
            time = time + rem_bt[i]
            rem_bt[i] = 0
            waiting_time = time - rem_bt[i]
print(rem_bt)
print(time)

