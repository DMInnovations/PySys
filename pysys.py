import os
import platform
import psutil
import numpy as np
import cpuinfo


class CPU:
    # CPU Core Count
    def cpuCoreCount():
        return os.cpu_count()

    # Processor/CPU Type  
    def processorType():
        return platform.processor()
        
    # Computer Architecture
    def computerArchitecture():
        return platform.architecture()
    
    # Physcial CPU Cores 
    def phyicalCoresCPU():
        return psutil.cpu_count(True)

    # Logical CPU Cores 
    def logicalCoresCPU():
        return psutil.cpu_count(False)

    # Overall CPU Usage
    def CPUsage():
       return psutil.cpu_percent()

    # CPU Info
    def CPU():
        return cpuinfo.get_cpu_info()["brand_raw"]
        
class OSType:
    def OS():
        return platform.system()

class RAM:
    # Overall RAM Usage   
    def RAMUsage():
        ram = np.round(psutil.virtual_memory().used/1000000000, 1)
        totalRAM = np.round(psutil.virtual_memory().total/1000000000, 2)
        swap = np.round(psutil.swap_memory().used/1000000000, 1)
        return ram, totalRAM, swap
        
    def swapMemory():
        return np.round(psutil.swap_memory().used/1000000000, 1)
        
    def totalRAM():
        return np.round(psutil.virtual_memory().total/1000000000, 2)
        
    def usedRAM():
        return np.round(psutil.virtual_memory().used/1000000000, 1)
    
class Memory:
    def storageUsage(file = "/"):
        storage = psutil.disk_usage(file)
        return storage
    
    def partitions():
        return psutil.disk_partitions(True)
