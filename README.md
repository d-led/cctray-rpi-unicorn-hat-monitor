# gocd-rpi-unicorn-hat-monitor

show GoCD status on a Raspberry Pi + a Unicorn HAT

## Usage

```
python poll.py <cctray.xml_url> <poll_wait_s>
```

## Prerequisites

- `pip install unicornhat`

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
