storage = 1000
usage = 2000
change = [-10, 25, -33]
total_usage = 0

    for i in range(5):
        usage = total_usage * change[i]/100
        total_usage += usage
        if total_usage > storage:
            return i
    
    return -1