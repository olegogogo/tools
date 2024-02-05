[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=PonomarevDA_tools&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=PonomarevDA_tools) [![cyphal_init.sh](https://github.com/PonomarevDA/tools/actions/workflows/cyphal_init.yml/badge.svg)](https://github.com/PonomarevDA/tools/actions/workflows/cyphal_init.yml) [![specification_checker.py](https://github.com/PonomarevDA/tools/actions/workflows/specification_checker.yml/badge.svg)](https://github.com/PonomarevDA/tools/actions/workflows/specification_checker.yml)

# Cyphal/DroneCAN nodes tools  

`tools` is a collection of scripts for testing and configuration of Cyphal/CAN and DroneCAN nodes.

## Current status

> This package is under development. It is avaliable in [test.pypi](https://test.pypi.org/project/raccoonlab-tools/) at the moment.

## Usage

Install the package from test.pypi and then run the desired script:

```
pip install -i https://test.pypi.org/simple/ raccoonlab-tools
```

### 1. Test cyphal specification

```bash
rl-test-cyphal-specification
```

### 2. Test dronecan specification

```bash
rl-test-dronecan-specification
```


### 3. Check protocol

rl-check-protocol

return cyphal | dronecan | none

<!--

### UC4. Upload firmware with st-link linux

rl-upload-firmware

### UC5-6. Upload cyphal/dronecan parameters

rl-upload-params

### UC7-8. Check cyphal/dronecan node type by name

rl-give-node-type

### UC9. Check RL firmware version

rl-check-updates

### UC10. Check other (custom) vendors firmware version

...

### UC11-12. Create socketcan linux (real/virtual)

rl-socketcan

### UC13-14. Create slcan linux/windows -->

## License

The scripts are distributed under MIT license. In general, you can do with them whatever you want. If you find a bug, please suggest a PR or an issue.
