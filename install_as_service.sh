#!/bin/bash
# run as sudo from the source directory
set -euo pipefail
IFS=$'\n\t'

# customize these
wait_s=30
urls="\
https://api.travis-ci.org/repos/d-led.xml \
https://api.travis-ci.org/repos/cucumber.xml \
"

if [ ! -f poll_hd.py ]; then
    echo "Please run from the checked out source directory"
    exit 1
fi

service_name=cctray_poller.service
target_file=/lib/systemd/system/${service_name}
# target_file=${service_name}
origin=`pwd`

cat >$target_file<< EOF
[Unit]
Description=Unicorn Hat HD CCTray poller
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python ${wait_s} ${origin}/poll_hd.py ${urls} > $origin/cctray.log 2>&1

[Install]
WantedBy=multi-user.target
EOF

chmod 644 $target_file
sudo systemctl daemon-reload
sudo systemctl enable ${service_name}
