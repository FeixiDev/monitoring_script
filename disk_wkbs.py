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
        wkbs_index = headers.index('wkB/s')
    except ValueError:
        print("Could not find 'wkB/s' column in iostat output")
        return None

    for line in lines:
        if device in line:
            values = line.split()
            wkbs = float(values[wkbs_index])
            return wkbs
    print(f"Could not find device {device} in iostat output")
    return None


if __name__ == '__main__':
    device = sys.argv[1]
    iops = get_iops(device)
    if iops is not None:
        print(iops)
