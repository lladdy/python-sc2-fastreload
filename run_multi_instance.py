import subprocess
import time

import sc2


def main():
    portconfig = sc2.portconfig.Portconfig()
    p1 = subprocess.Popen(["python", "./host_multi_instance.py", portconfig.as_json])
    time.sleep(5)
    p2 = subprocess.Popen(["python", "./join_multi_instance.py", portconfig.as_json])

    while p1.poll() is None or p2.poll() is None:
        pass

if __name__ == "__main__":
    main()
