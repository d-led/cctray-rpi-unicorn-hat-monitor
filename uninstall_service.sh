#!/bin/bash
# run as sudo from the source directory
set -euo pipefail
IFS=$'\n\t'

service_name=cctray_poller.service
target_file=/lib/systemd/system/${service_name}

systemctl disable $service_name
rm -f $target_file
