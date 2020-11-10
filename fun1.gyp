import psutil
  
# Path 
path = "/"
  
# Get the disk usage statistics 
# about the given path 
total, used, free, percent = psutil.disk_usage(path) 

# Converting to GB
gb_used = used / 1000000000

#Monitoring function
def disk_usage():
    if gb_used > 100:
        print("STORAGE NEAR CAPACITY")
        print("CURRENT USED STORAGE: %sGB" % (gb_used))
    
    else: 
        print("STORAGE OK")
        print("CURRENT USED STORAGE: %sGB" % (gb_used))

    return

disk_usage()