import logging
import json
import socket
import platform
import uuid
import re
import os

import psutil


def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info, indent=4)
    except Exception as e:
        logging.exception(e)


def getCpuInfo():
    cpuUsage = psutil.cpu_percent(4)

    return cpuUsage


def getRamInfo():
    # Getting all memory using os.popen()
    total_memory, used_memory, free_memory = map(
        int, os.popen('free -t -m').readlines()[-1].split()[1:])
    # Memory usage
    ramUsage = round((used_memory/total_memory) * 100, 2)
    print("RAM memory % used:", ramUsage)

    return ramUsage


def getDiskInfo():
        for disk in psutil.disk_partitions():
            if disk.fstype:
                total = int(psutil.disk_usage(disk.mountpoint).total)
                used  = int(psutil.disk_usage(disk.mountpoint).used)
                free  = int(psutil.disk_usage(disk.mountpoint).free)

        return(f'''
:floppy_disk: TOTAL DISK SPACE : {round(total / (1024.0 ** 3), 4)} GiB
:floppy_disk: USED DISK SPACE  : {round(used / (1024.0 ** 3), 4)} GiB
:floppy_disk: FREE DISK SPACE  : {round(free / (1024.0 ** 3), 4)} GiB
        ''')