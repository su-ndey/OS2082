pid = [0] * 100
bt = [0] * 100
wt = [0] * 100
tat = [0] * 100

n = int(input("Enter the number of processes: "))

for i in range(n):
    pid[i] = int(input(f"Enter Process ID for process {i + 1}: "))
    bt[i] = int(input(f"Enter Burst Time for process {i + 1}: "))

# Calculate waiting time of the processes
wt[0] = 0
for i in range(1, n):
    wt[i] = wt[i - 1] + bt[i - 1]

# Calculate turnaround time
for i in range(n):
    tat[i] = bt[i] + wt[i]

print("\nProcess ID\tBurst Time\tWaiting Time\tTurnaround Time")
print("-" * 70)

twt = 0
ttat = 0

for i in range(n):
    print(f"{pid[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")
    twt += wt[i]
    ttat += tat[i]

avg_wt = twt / n
avg_tat = ttat / n

print("\nAverage Waiting Time:", avg_wt)
print("Average Turnaround Time:", avg_tat)
