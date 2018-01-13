#! /usr/bin/env python
import sys
import rospy
import sensor_msgs.msg

if __name__ == '__main__':

    rospy.init_node('tst_jointstate_publishing')
    
    pub = rospy.Publisher("/amigo/joint_states", sensor_msgs.msg.JointState)
    msg = sensor_msgs.msg.JointState()
    msg.header.stamp = rospy.Time.now()
    
    # # Ankle joint
    # msg.name.append("ankle_joint")
    # msg.position = [0.8]
    # msg.velocity = [0]
    # msg.effort   = [0]
    
    # # Knee joint (dummy, not depending on torso)
    # msg.name.append("knee_joint")
    # msg.position.append(1.61)
    # msg.velocity.append(0)
    # msg.effort.append(0)
    
    # # hip joint (dummy, not depending on torso)
    # msg.name.append("hip_joint")
    # msg.position.append(1.8)
    # msg.velocity.append(0)
    # msg.effort.append(0)
    
    ## Left Arm

    # # Shoulder yaw joint
    # msg.name.append("shoulder_yaw_joint_left")
    # msg.position.append(-0.1)
    # msg.velocity.append(0)
    # msg.effort.append(0)
    
    # # Shoulder pitch joint
    # msg.name.append("shoulder_pitch_joint_left")
    # msg.position.append(-0.3)
    # msg.velocity.append(0)
    # msg.effort.append(0)
    
    # # Shoulder roll joint
    # msg.name.append("shoulder_roll_joint_left")
    # msg.position.append(0.2)
    # msg.velocity.append(0)
    # msg.effort.append(0)
    
    # # Elbow pitch joint
    # msg.name.append("elbow_pitch_joint_left")
    # msg.position.append(1.0)
    # msg.velocity.append(0)
    # msg.effort.append(0)
    
    # # Elbow roll joint
    # msg.name.append("elbow_roll_joint_left")
    # msg.position.append(0.0)
    # msg.velocity.append(0)
    # msg.effort.append(0)
    
    # # Wrist pitch joint
    # msg.name.append("wrist_pitch_joint_left")
    # msg.position.append(0.0)
    # msg.velocity.append(0)
    # msg.effort.append(0)
    
    # # Wrist yaw joint
    # msg.name.append("wrist_yaw_joint_left")
    # msg.position.append(0.0)
    # msg.velocity.append(0)
    # msg.effort.append(0)
    
    ## Right Arm

    # Shoulder yaw joint
    msg.name.append("shoulder_yaw_joint_right")
    msg.position.append(-0.1)
    msg.velocity.append(0)
    msg.effort.append(0)
    
    # Shoulder pitch joint
    msg.name.append("shoulder_pitch_joint_right")
    msg.position.append(-0.3)
    msg.velocity.append(0)
    msg.effort.append(0)
    
    # Shoulder roll joint
    msg.name.append("shoulder_roll_joint_right")
    msg.position.append(0.2)
    msg.velocity.append(0)
    msg.effort.append(0)
    
    # Elbow pitch joint
    msg.name.append("elbow_pitch_joint_right")
    msg.position.append(1.0)
    msg.velocity.append(0)
    msg.effort.append(0)
    
    # Elbow roll joint
    msg.name.append("elbow_roll_joint_right")
    msg.position.append(0.0)
    msg.velocity.append(0)
    msg.effort.append(0)
    
    # Wrist pitch joint
    msg.name.append("wrist_pitch_joint_right")
    msg.position.append(0.0)
    msg.velocity.append(0)
    msg.effort.append(0)
    
    # Wrist yaw joint
    msg.name.append("wrist_yaw_joint_right")
    msg.position.append(0.0)
    msg.velocity.append(0)
    msg.effort.append(0)
    
    ## Neck
    
    # # Neck pan joint
    # msg.name.append("neck_pan_joint")
    # msg.position.append(0.0)
    # msg.velocity.append(0)
    # msg.effort.append(0)
    
    # # Neck tilt joint
    # msg.name.append("neck_tilt_joint")
    # msg.position.append(-0.3)
    # msg.velocity.append(0)
    # msg.effort.append(0)
    
    # # Torso laser
    # msg.name.append("torso_laser_joint")
    # msg.position.append(0.3)
    # msg.velocity.append(0)
    # msg.effort.append(0)
    
    rospy.loginfo("Publishing msg {0}".format(msg))    
    
    while (not rospy.is_shutdown()):
        msg.header.stamp = rospy.Time.now()
        pub.publish(msg)
        rospy.sleep(0.1)
    
    rospy.loginfo("Done!")
