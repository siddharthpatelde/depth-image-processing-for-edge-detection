#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class FrameGrabber:
    def __init__(self):
        self.bridge = CvBridge()
        self.depth_image_original = None

        rospy.Subscriber("/ascamera/depth0/image_raw", Image, self.depth_callback)


    def depth_callback(self, msg):
        self.depth_image_original = self.bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")

    def show_loop(self):
        rate = rospy.Rate(30)
        while not rospy.is_shutdown():
            
            if self.depth_image_original is not None:
                depth_gray = cv2.normalize(self.depth_image_original, None, 0, 255, cv2.NORM_MINMAX)
                depth_gray = cv2.convertScaleAbs(depth_gray)
                depth_colored = cv2.applyColorMap(depth_gray, cv2.COLORMAP_JET)
                cv2.imshow("Depth Original", self.depth_image_original)
                cv2.imshow("Depth Gray", depth_gray)
                cv2.imshow("Depth Colored", depth_colored)
                
            key = cv2.waitKey(1) & 0xFF
            if key == ord('1'):
                print("Key '1' pressed. Exiting...")
                break

            rate.sleep()

        cv2.destroyAllWindows()

if __name__ == "__main__":
    rospy.init_node("rgb_depth_filters_viewer")
    grabber = FrameGrabber()
    grabber.show_loop()