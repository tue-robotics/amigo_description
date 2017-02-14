cmake_minimum_required(VERSION 2.8.3)
project(amigo_description)
find_package(catkin REQUIRED)
catkin_package()

find_package(xacro REQUIRED)

# Xacro files
file(GLOB xacro_files ${CMAKE_CURRENT_SOURCE_DIR}/urdf/*.urdf.xacro)

foreach(it ${xacro_files})
    # remove .xacro extension
    string(REGEX MATCH "(.*)[.]xacro$" unused ${it})
    set(output_filename ${CMAKE_MATCH_1})

    # create a rule to generate ${output_filename} from {it}
    xacro_add_xacro_file(${it} ${output_filename} INORDER)

    list(APPEND robot_files ${output_filename})
endforeach(it)

# add an abstract target to actually trigger the builds
add_custom_target(amigo_media_files ALL DEPENDS ${robot_files})
