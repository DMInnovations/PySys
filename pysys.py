import os
import platform
import psutil
import numpy as np


class CPU:
    # CPU Core Count
    def cpuCoreCount():
        print(f"Core Count: {os.cpu_count()}")

    # Processor/CPU Type  
    def processorType():
        print(f"Processor: {platform.processor()}")
        
    # Computer Architecture
    def computerArchitecture():
        print(f"Architecture: {platform.architecture()}")
    
    # Physcial CPU Cores 
    def phyicalCoresCPU():
        print(psutil.cpu_count(True))

    # Logical CPU Cores 
    def logicalCoresCPU():
        print(psutil.cpu_count(False))

    # Overall CPU Usage
    def CPUsage():
        print(f"CPU Usage: {psutil.cpu_percent()}%")
        
class OSType:
    def OS():
        print(f"OS: {platform.system()}")

class RAM:
    # Overall RAM Usage   
    def RAMUsage():
        ram = np.round(psutil.virtual_memory().used/1000000000, 1)
        totalRAM = np.round(psutil.virtual_memory().total/1000000000, 2)
        swap = np.round(psutil.swap_memory().used/1000000000, 1)
        print(f"RAM Usage: {ram} GB / {totalRAM} GB\nSwap Memory: {swap} GB")
        
    def swapMemory():
        swap = np.round(psutil.swap_memory().used/1000000000, 1)
        print(f"Swap Memory: {swap} GB")
        
    def totalRAM():
        totalRAM = np.round(psutil.virtual_memory().total/1000000000, 2)
        print(f"Total RAM: {totalRAM} GB")
        
    def usedRAM():
        usedRAM = np.round(psutil.virtual_memory().used/1000000000, 1)
        print(f"Used RAM: {usedRAM} GB")