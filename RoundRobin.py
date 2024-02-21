TIME_QUANTUM = 2

def round_robin_process_allocation():
    print("Enter burst time of processes as list separated by spaces:")
    burst_time = [int(x) for x in input().split()]
    rem_bt = burst_time.copy()
    waiting_time = [0] * len(burst_time)
    time = 0

    while(1):
        done = True
        for i in range(len(rem_bt)):
            if (rem_bt[i] > 0):
                done = False
                if rem_bt[i] > TIME_QUANTUM:
                    time = time + TIME_QUANTUM
                    rem_bt[i] = rem_bt[i] - TIME_QUANTUM
                    print(rem_bt)
                else:
                    time = time + rem_bt[i]
                    rem_bt[i] = 0
                    waiting_time[i] = time - burst_time[i]
                    print(rem_bt)
        if done == True:
            break

# round_robin_process_allocation()
