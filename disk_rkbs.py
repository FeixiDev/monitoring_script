#!/usr/bin/python3
import subprocess
import sys


def get_iops(device):
    cmd = ['iostat', '-dxk', '1', '2']
    output = subprocess.check_output(cmd).decode()
    lines = output.strip().split('\n')

    header_line = [line for line in lines if 'Device' in line][0]
    headers = header_line.split()
    try:
        rkbs_index = headers.index('rkB/s')
    except ValueError:
        print("Could not find 'rkB/s' column in iostat output")
        return None

    for line in lines:
        if device in line:
            values = line.split()
            rkbs = float(values[rkbs_index])
            return rkbs
    print(f"Could not find device {device} in iostat output")
    return None


if __name__ == '__main__':
    device = sys.argv[1]
    iops = get_iops(device)
    if iops is not None:
        print(iops)
