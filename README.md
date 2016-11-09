# GoCD Raspberry Pi + Unicorn HAT Monitor

show [GoCD](https://www.go.cd/) status on a Raspberry Pi + a Unicorn HAT

[![Build Status](https://snap-ci.com/d-led/gocd-rpi-unicorn-hat-monitor/branch/master/build_image)](https://snap-ci.com/d-led/gocd-rpi-unicorn-hat-monitor/branch/master)

![LEDs](img/leds.jpg)

## Prerequisites

- Raspberry Pi, i.e. [3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
- [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
- [Unicorn HAT](https://shop.pimoroni.de/products/unicorn-hat)
- `pip install unicornhat`
- this project
- A `cctray.xml` url ([Snap CI](https://snap-ci.com/) or other CC* tools are expected to work as well. Open an issue if not)

## Usage

```
sudo python poll.py <cctray.xml_url> <poll_wait_s>
```

- if the number of status entries exceeds the number of LEDs on the LED matrix (64, here), only the top level entries will be used.
- after the number of top level exceeds the number of LEDs, the input will be trimmed

![quick feedback](img/quick_feedback.jpg)

## If you don't use GoCD / can't access cctray.xml

Use a small HTTP server (based on [Flask](http://flask.pocoo.org)) listening to incoming arrays of status:

```python
sudo python server.py
```

i.e. with [httpie](https://httpie.org): `http post http://127.0.0.1:5500/update status:='["NONE","BUILDING","OK","ERROR","NONE","WHAT?"]' --auth ...`

or write your own polling script taking poll.py as an example.

## GoCD pipeline as code

The project can be built on GoCD using the new feature: [pipeline configuration from source control #1133](https://github.com/gocd/gocd/issues/1133). For this, use:

- the gocd [yaml config plugin](https://github.com/tomzo/gocd-yaml-config-plugin/releases)
- this repository as primary material and as the pipeline definition

The pipeline configuration can be seen in [ci.gocd.yaml](ci.gocd.yaml)

The GoCD XML config needs the following addition:

```xml
  <config-repos>
    <config-repo plugin="yaml.config.plugin">
      <git url="https://github.com/d-led/gocd-rpi-unicorn-hat-monitor.git" />
    </config-repo>
  </config-repos>
```
