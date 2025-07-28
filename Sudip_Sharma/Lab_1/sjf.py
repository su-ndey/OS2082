pid = [0] * 20
bt = [0] * 20
wt = [0] * 20
tat = [0] * 20

n = int(input("Enter the number of processes: "))

for i in range(n):
    pid[i] = int(input(f"Enter Process ID for process {i+1}: "))
    bt[i] = int(input(f"Enter Burst Time for process {i+1}: "))

for i in range(n):
    for j in range(i + 1, n):
        if bt[i] > bt[j]:
            bt[i], bt[j] = bt[j], bt[i]
            pid[i], pid[j] = pid[j], pid[i]

wt[0] = 0

for i in range(1, n):
    wt[i] = 0
    for j in range(i):
        wt[i] += bt[j]

for i in range(n):
    tat[i] = bt[i] + wt[i]

total = sum(wt[:n])
totalT = sum(tat[:n])

avg_wt = total / n
avg_tat = totalT / n

print("\nProcess ID\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{pid[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
