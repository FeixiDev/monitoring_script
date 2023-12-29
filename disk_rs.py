#!/usr/bin/python3
import psutil
import time
import sys


def calculate_read_iops(device, interval=1):
    initial_io = psutil.disk_io_counters(perdisk=True)
    initial_read_count = initial_io[device].read_count

    time.sleep(interval)

    current_io = psutil.disk_io_counters(perdisk=True)
    current_read_count = current_io[device].read_count

    read_iops = int((current_read_count - initial_read_count) / interval)

    return read_iops


if __name__ == '__main__':
    device = sys.argv[1]
    read_iops = calculate_read_iops(device)
    print(read_iops)
