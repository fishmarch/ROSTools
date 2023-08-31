# coding:utf-8

import roslib
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError

path = "/home/xiaoyu/myData/GVINS/sports_field/"
bag_path = '/media/xiaoyu/T7/dataset/GVINS/field.bag'


class ImageCreator():
    def __init__(self):
        left_file = open(path + "left.txt", 'w')
        right_file = open(path + "right.txt", 'w')
        omni_file = open(path + "omni.txt", 'w')
        imu_file = open(path + "imu.txt", 'w')
        encoder_file = open(path + "encoder.txt", 'w')
        self.bridge = CvBridge()
        print("Start!")
        # dim = (640, 360)
        with rosbag.Bag(bag_path, 'r') as bag:
            end_time = bag.get_end_time()
            i = 0
            for topic, msg, t in bag.read_messages():
                print(t)
                print(end_time)
                print("--------------")
                if topic == "/cam0/image_raw":
                    try:
                        # cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
                        cv_image = self.bridge.imgmsg_to_cv2(msg, "mono8")
                    except CvBridgeError as e:
                        print(e)
                    # cv_image_resized = cv2.resize(cv_image, dim)
                    timestr = "%.6f" % msg.header.stamp.to_sec()
                    image_info = timestr + " left/" + timestr + ".png\n"
                    left_file.write(image_info)
                    image_name = path + "left/" + timestr + ".png"
                    cv2.imwrite(image_name, cv_image)

                # elif topic == "/stereo_inertial_publisher/right/image_rect":
                #     try:
                #         # cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
                #         cv_image = self.bridge.imgmsg_to_cv2(msg, "mono8")
                #     except CvBridgeError as e:
                #         print(e)
                #     # cv_image_resized = cv2.resize(cv_image, dim)
                #     timestr = "%.6f" % msg.header.stamp.to_sec()
                #     image_info = timestr + " right/" + timestr + ".png\n"
                #     right_file.write(image_info)
                #     image_name = path + "right/" + timestr + ".png"
                #     cv2.imwrite(image_name, cv_image)
                # elif topic == "/left/image_raw":
                #
                # if topic == "/cam0/image_raw":
                #     # i += 1
                #     # if i > 500 :
                #     #     break
                #     try:
                #         # cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
                #         cv_image = self.bridge.imgmsg_to_cv2(msg, "mono8")
                #     except CvBridgeError as e:
                #         print(e)
                #     # cv_image_resized = cv2.resize(cv_image, dim)
                #     timestr = "%.6f" % msg.header.stamp.to_sec()
                #     image_info = timestr + " omni/" + timestr + ".png\n"
                #     omni_file.write(image_info)
                #     image_name = path + "omni/" + timestr + ".png"
                #     cv2.imwrite(image_name, cv_image)

                elif topic == "/imu0":
                    timestr = "%.6f" % msg.header.stamp.to_sec()
                    imu_info = timestr + " " + str(msg.linear_acceleration.x) + " " + str(
                        msg.linear_acceleration.y) + " " + str(msg.linear_acceleration.z)
                    imu_info = imu_info + " " + str(msg.angular_velocity.x) + " " + str(
                        msg.angular_velocity.y) + " " + str(msg.angular_velocity.z) + "\n"
                    imu_file.write(imu_info)

                # elif topic == "/raw_odom":
                #     timestr = "%.6f" % msg.header.stamp.to_sec()
                #     encoder_info = timestr + " " + str(msg.twist.twist.linear.x) + " " + str(
                #         msg.twist.twist.linear.y) + " " + str(msg.twist.twist.linear.y) \
                #         + " " + str(msg.twist.twist.angular.x) + " " + str(
                #         msg.twist.twist.angular.y) + " " + str(msg.twist.twist.angular.y) + "\n"
                #     encoder_file.write(encoder_info)

        left_file.close()
        right_file.close()
        imu_file.close()
        encoder_file.close()


if __name__ == '__main__':

    # rospy.init_node(PKG)

    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
