#! /bin/bash

ROBOT_DESCRIPTION_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/.."

rosrun xacro xacro.py -o $ROBOT_DESCRIPTION_DIR/urdf/amigo.urdf $ROBOT_DESCRIPTION_DIR/urdf/xacro/amigo.urdf.xacro


