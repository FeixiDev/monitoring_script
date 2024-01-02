#!/usr/bin/python3
import psutil
import time
import sys


def calculate_write_iops(device, interval=1):
    initial_io = psutil.disk_io_counters(perdisk=True)
    initial_write_count = initial_io[device].write_count

    time.sleep(interval)

    current_io = psutil.disk_io_counters(perdisk=True)
    current_write_count = current_io[device].write_count

    write_iops = int((current_write_count - initial_write_count) / interval)

    return write_iops


if __name__ == '__main__':
    device = sys.argv[1]
    write_iops = calculate_write_iops(device)
    print(write_iops)
