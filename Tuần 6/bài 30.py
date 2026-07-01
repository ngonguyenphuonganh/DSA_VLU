def round_robin(processes, burst_times, quantum):
    queue = []
    for i in range(len(processes)):
        queue.append([processes[i], burst_times[i]])
    
    time = 0
    completion_times = {}
    
    while queue:
        p, bt = queue.pop(0)
        if bt > quantum:
            time += quantum
            queue.append([p, bt - quantum])
        else:
            time += bt
            completion_times[p] = time
            
    return completion_times