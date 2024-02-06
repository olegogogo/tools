#!/usr/bin/env python3
# This software is distributed under the terms of the MIT License.
# Copyright (c) 2024 Dmitry Ponomarev.
import dronecan
from raccoonlab_tools.dronecan.utils import ParametersInterface, NodeFinder

def main():
    node = dronecan.make_node('slcan:/dev/ttyACM0', node_id=100, bitrate=1000000, baudrate=1000000)
    target_node_id = NodeFinder(node).find_online_node()
    params_interface = ParametersInterface(node=node, target_node_id=target_node_id)
    all_params = params_interface.get_all()
    for param in all_params:
        print(param)

if __name__ =="__main__":
    main()
