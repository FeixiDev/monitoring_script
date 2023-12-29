#!/usr/bin/python3
import sys
import subprocess


def get_disk_free_space(disk_name):
    cmd = f"df {disk_name} --output=avail | tail -n 1"
    try:
        result = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError:
        return None
    return round(int(result.strip()) / (1024 * 1024), 2)


if __name__ == "__main__":
    disk_name = sys.argv[1]
    free_space = get_disk_free_space(disk_name)
    print(free_space)
