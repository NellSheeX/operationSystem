import psutil

cpuPercent = psutil.cpuPercent()
cpuCount = psutil.cpuCount()
cpuFreqCurrent = psutil.cpuFreqCurrent().current
memoryTotal = psutil.virtual_memory().total
memoryUsed = psutil.virtual_memory().used
memoryAvailable = psutil.virtual_memory().available
diskUsage = psutil.diskUsage('/')


result = {
    'cpuPercent': cpuPercent,
    'cpuCount': cpuCount,
    'cpuFreqCurrent': cpuFreqCurrent,
    'memoryTotal': memoryTotal,
    'memoryUsed': memoryUsed,
    'memoryAvailable': memoryAvailable,
    'diskUsage total': diskUsage.total,
    'diskUsage used': diskUsage.used,
    'diskUsage free': diskUsage.free
}


print(result)

