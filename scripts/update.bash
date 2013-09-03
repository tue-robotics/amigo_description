#! /bin/bash

ROBOT_DESCRIPTION_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/.."

# Generate urdf from xacro
rosrun xacro xacro.py -o $ROBOT_DESCRIPTION_DIR/urdf/amigo.urdf $ROBOT_DESCRIPTION_DIR/urdf/xacro/amigo.urdf.xacro

# Generate sdf from urdf
gzsdf print $ROBOT_DESCRIPTION_DIR/urdf/amigo.urdf > $ROBOT_DESCRIPTION_DIR/sdf/amigo.sdf

grep 'Error' $ROBOT_DESCRIPTION_DIR/sdf/amigo.sdf
grep 'Warning' $ROBOT_DESCRIPTION_DIR/sdf/amigo.sdf

# Remove warning messages from sdf
sed -i '/Warning/d' $ROBOT_DESCRIPTION_DIR/sdf/amigo.sdf

# Fix media paths
sed -i 's/model:\/\/amigo_description\/media/model:\/\/media/g' $ROBOT_DESCRIPTION_DIR/sdf/amigo.sdf

#copy model to physicless file
cp $ROBOT_DESCRIPTION_DIR/sdf/amigo.sdf $ROBOT_DESCRIPTION_DIR/sdf/amigo_physicless.sdf

#change controllers in physicless file
sed -i 's/libPositionController/libPositionController_simple/g' $ROBOT_DESCRIPTION_DIR/sdf/amigo_physicless.sdf
