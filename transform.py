import cv2
import numpy as np

from scipy.spatial.transform import Rotation as R


def quaternion2rot(quaternion):
    r = R.from_quat(quaternion)
    rot = r.as_matrix()
    return rot


quaternion = [0.999962, -0.0050195, -0.00611, 0.003793 ]
rotation = quaternion2rot(quaternion)
print(rotation)
t = np.array([[-0.834949], [-0.004864], [-0.0002959]])
print(t)
trans = np.dot(rotation, t)
print(trans)

# 输出
# [[-0.9754533   0.21902821 -0.02274859]
#  [-0.18783626 -0.88152702 -0.43316008]
#  [-0.11492777 -0.41825442  0.90102988]]