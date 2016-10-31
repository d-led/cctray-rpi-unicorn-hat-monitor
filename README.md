# gocd-rpi-unicorn-hat-monitor

show GoCD status on a Raspberry Pi + a Unicorn HAT

## Prerequisites

- Raspberry Pi, i.e. [3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
- [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
- [Unicorn HAT](https://shop.pimoroni.de/products/unicorn-hat)
- `pip install unicornhat`
- this project

## Usage

```
sudo python poll.py <cctray.xml_url> <poll_wait_s>
```

- if the number of status entries exceeds the number of LEDs on the LED matrix (64, here), only the top level entries will be used.
- after the number of top level exceeds the number of LEDs, the input will be trimmed

## GoCD by example

- gocd [yaml config plugin](https://github.com/tomzo/gocd-yaml-config-plugin/releases)
- this repository as primary material and as the pipeline definition

cruise config addition:

```xml
  <config-repos>
    <config-repo plugin="yaml.config.plugin">
      <git url="https://github.com/d-led/gocd-rpi-unicorn-hat-monitor.git" />
    </config-repo>
  </config-repos>
```
