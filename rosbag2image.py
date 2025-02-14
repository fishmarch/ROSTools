# coding:utf-8

import rosbag
import rospy
import cv2
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
from tqdm import tqdm

path = "/home/hkclr/myData/VBR/campus_train0/"
bag_list = [
    '/home/hkclr/myData/VBR/campus_train0/campus_train0_00.bag',
    '/home/hkclr/myData/VBR/campus_train0/campus_train0_01.bag',
    '/home/hkclr/myData/VBR/campus_train0/campus_train0_02.bag',
    '/home/hkclr/myData/VBR/campus_train0/campus_train0_03.bag',
    '/home/hkclr/myData/VBR/campus_train0/campus_train0_04.bag',
    ]

class ImageCreator():
    def __init__(self):
        left_file = open(path + "left.txt", 'w')
        right_file = open(path + "right.txt", 'w')
        imu_file = open(path + "imu.txt", 'w')
        self.bridge = CvBridge()
        print("Start!")
        # dim = (640, 360)
        for bag_path in bag_list:
            with rosbag.Bag(bag_path, 'r') as bag:
                total_messages = bag.get_message_count(topic_filters=["/camera_left/image_raw",
                                                                      "/camera_right/image_raw",
                                                                      "/imu/data"])
                with tqdm(total=total_messages) as pbar:
                    for topic, msg, t in bag.read_messages():
                        if topic == "/camera_left/image_raw":
                            try:
                                cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
                                # cv_image = self.bridge.imgmsg_to_cv2(msg, "mono8")
                                # cv_image = self.bridge.compressed_imgmsg_to_cv2(msg, "bgr8")
                            except CvBridgeError as e:
                                print(e)
                            # cv_image_resized = cv2.resize(cv_image, dim)
                            timestr = str(msg.header.stamp.to_sec())
                            image_info = timestr + " left/" + timestr + ".png\n"
                            left_file.write(image_info)
                            image_name = path + "left/" + timestr + ".png"
                            cv2.imwrite(image_name, cv_image)
                            pbar.update(1)

                        elif topic == "/camera_right/image_raw":
                            try:
                                cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
                                # cv_image = self.bridge.imgmsg_to_cv2(msg, "mono8")
                                # cv_image = self.bridge.compressed_imgmsg_to_cv2(msg, "bgr8")
                            except CvBridgeError as e:
                                print(e)
                            # cv_image_resized = cv2.resize(cv_image, dim)
                            timestr = str(msg.header.stamp.to_sec())
                            image_info = timestr + " right/" + timestr + ".png\n"
                            right_file.write(image_info)
                            image_name = path + "right/" + timestr + ".png"
                            cv2.imwrite(image_name, cv_image)
                            pbar.update(1)

                        elif topic == "/imu/data":
                            timestr = str(msg.header.stamp.to_sec())
                            imu_info = timestr + " " + str(msg.linear_acceleration.x) + " " + str(
                                msg.linear_acceleration.y) + " " + str(msg.linear_acceleration.z)
                            imu_info = imu_info + " " + str(msg.angular_velocity.x) + " " + str(
                                msg.angular_velocity.y) + " " + str(msg.angular_velocity.z) + "\n"
                            imu_file.write(imu_info)
                            pbar.update(1)

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


if __name__ == '__main__':

    # rospy.init_node(PKG)

    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
