minutes = 0

all_times = ['1h 45m,360s,25m,30m 120s,2h 60s']

times_str = all_times[0]

times_lst = times_str.split(',')

for t in times_lst:
    for part in t.split():
        if 'h' in part:
            num=int(part.replace('h',''))
            minutes += num*60
        elif 'm' in part:
            num=int(part.replace('m',''))
            minutes += num
        elif 's' in part:
            num=int(part.replace('s',''))
            minutes += num/60

 
print(minutes)
