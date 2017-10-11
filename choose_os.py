#!/bin/python
#
import platform
import subprocess
import os, time


def TestPlatform():
    print ("----------Operation System--------------------------")
    # Windows will be : (32bit, WindowsPE)
    # Linux will be : (32bit, ELF)
    print(platform.architecture())

    # Windows will be : Windows-XP-5.1.2600-SP3 or Windows-post2008Server-6.1.7600
    # Linux will be : Linux-2.6.18-128.el5-i686-with-redhat-5.3-Final
    print(platform.platform())

    # Windows will be : Windows
    # Linux will be : Linux
    print(platform.system())

    print ("--------------Python Version-------------------------")
    # Windows and Linux will be : 3.1.1 or 3.1.3
    print(platform.python_version())


def UsePlatform():
    sysstr = platform.system()
    if (sysstr == "Windows"):
        # print ("Call Windows tasks")
        #cmdShell = '"C:\Program Files (x86)\NetSarang\Xshell 4\Xshell.exe"   C:\Users\scheng\AppData\Roaming\NetSarang\Xshell\Sessions\east40-it-pinHole-query.xsh'
        # os.system(cmd)
        p = subprocess.Popen(cmdShell, shell=True)
        time.sleep(10)
        p.terminate()
    elif (sysstr == "Linuxi1"):
        # print ("Call Linux tasks")
        #cmdShell = '/root/AutoTestEnv/UCG_COMMON/TOOLS/auto_excute.sh /root/AutoTestEnv/AutoTestCaseRepo/UAG45/UAG45_SERVER_MODE/UDP/SIPP_REGISTER_MO_RTP_CALL_Pinhole_Query'
        p = subprocess.Popen(cmdShell, shell=True)
        time.sleep(10)
        p.terminate()
    else:
        print ("Other System tasks")
        raise Exception('os is not support')


TestPlatform()
#UsePlatform()
