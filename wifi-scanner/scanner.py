#!/usr/bin/env python3

import subprocess

nw = subprocess.check_output(['netsh', 'wlan0', 'show', 'network'])

decoded_nw = nw.decode('ascii')

print(decoded_nw)