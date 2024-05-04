import random;
n=int(input("enter the number of jobs: "))
time=[]
profit=[]

for i in range(n):
    t=random.randint(1,100)
    p=random.randint(1,100)
    profit.append(p)
    time.append(t)
    
values=[]

for i in range(n):
    value=profit[i]/time[i]
    values.append(value)
sorted_values=sorted(range(n),key=lambda i:values[i],reverse=True)

schedule=[]
total_time=0
for i in sorted_values:
    durations=time[i]
    total_time=durations+total_time
    schedule.append(i+1)
    
print("schedule")
for i in range(n):
    print("job",schedule[i])
print("total Time:",total_time)
