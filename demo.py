# Author: 
# created_time:
import os
import time


def execute(cmd):
    adb_path = '/Users/vincent/TempFolder/MaybeUsefulWithShortTime/platform-tools/'
    adb_str = adb_path + 'adb shell {}'.format(cmd)
    print(adb_str)
    os.system(adb_str)


if __name__ == '__main__':
    execute('am start -n com.supwisdom.sqgxyapp/io.dcloud.feature.sdk.multi.DCUniMPTopActivity0')
    time.sleep(1)
    execute('input tap 500 2275')
