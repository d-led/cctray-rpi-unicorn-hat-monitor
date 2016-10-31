#!/usr/bin/env python

from sink import Sink
from matrix import Matrix
from cctray_status import CCTray
import sys
import time

# USAGE: python poll.py <cctray.xml_url> <poll_wait_s>

url = 'http://localhost:8153/go/cctray.xml'
poll_wait_s = 1

if len(sys.argv) == 1:
    from FakeHat import FakeHat
    hat = FakeHat()

if len(sys.argv) > 1:
    from RealHat import RealHat
    hat = RealHat()
    url = sys.argv[1]

if len(sys.argv) > 2:
    poll_wait_s = int(sys.argv[2])

#################################################################################

led = Matrix(hat)
sink = Sink(led)
cctray = CCTray(url, hat.AREA)

if __name__ == "__main__":
    while True:
        sink.put(cctray.fetch())
        time.sleep(poll_wait_s)
