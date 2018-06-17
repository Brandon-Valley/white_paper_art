import os
import psutil
process = psutil.Process(os.getpid())
bytes = process.memory_info().rss
megabytes = bytes / 1000000
gigabytes = megabytes / 1000
print('megabytes: ', megabytes)
print('gigabytes: ', gigabytes)
