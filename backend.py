#Backend processing for the mointoring tool
#Required backend packages
from __future__ import print_function

import json

import psutil


def alert():
    #This function is used to send instant notifications to the endpoint selected.
    #The details for this endpoint are configured in the UserConsole.
    # The data is stored in a local encypted file.d
    print('alert')



def getLocalCPUlevels():
    #CPU data returned in JSON
    #Memory Stats in MB
    data={}
    MemoryUsage=psutil.virtual_memory()
    THRESHOLD = 100 * 1024 * 1024
    CPUAvail = MemoryUsage.available >> 20
    CPUTotal = MemoryUsage.total >>10
    CPUused = MemoryUsage.used >>20
    if MemoryUsage.available <= THRESHOLD:
        alert()
        data['CPU Available'] = CPUAvail
        data['CPU Total'] = CPUTotal
        data['CPU Used'] = CPUused
        data ['CPU Message'] = 'FAIL'
        return data
    else:
        data['CPU Available'] = CPUAvail
        data['CPU Total'] = CPUTotal
        data['CPU Used'] = CPUused
        data['CPU Message'] = 'OK'
        return data

CPU_data = getLocalCPUlevels()
print (json.dumps(CPU_data))

def getApacheLogs():
    return 'OK'