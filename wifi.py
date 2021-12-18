import subprocess
import time


SECONDS_WITH_WIFI_DISABLED = 60
# Constants for the command prompt
CMD_BASE = 'cmd /c "{}"'  # first is remain/terminate, then is enable/disable
WIFI_CMD_BASE = 'wmic path win32_networkadapter where NetConnectionID="Wi-fI" call {}'
WIFI_CMD_ENABLE = WIFI_CMD_BASE.format('enable')
WIFI_CMD_DISABLE = WIFI_CMD_BASE.format('disable')
#  run auto-py-to-exe to convert this file to an exe


def main():
    turn_off_wifi()
    time.sleep(SECONDS_WITH_WIFI_DISABLED)
    turn_on_wifi()


def execute_cmd(cmd):
    subprocess.call(cmd, shell=True)


def turn_on_wifi():
    execute_cmd(CMD_BASE.format(WIFI_CMD_ENABLE))


def turn_off_wifi():
    execute_cmd(CMD_BASE.format(WIFI_CMD_DISABLE))

if __name__ == "__main__":
    main()
