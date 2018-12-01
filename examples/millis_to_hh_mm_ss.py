def print_time(millis):
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))

    print ("%02d:%02d:%02d" % (hours, minutes, seconds))

try:
    millisFile = open("/home/rbozzini/workspaces/python/esamples/millis.txt", "r")
    
    for millis in millisFile:
        print_time(int(millis.strip()) * 10)

except IOError:
    print ('cannot open millis.txt')    
