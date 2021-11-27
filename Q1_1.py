import numpy as np


def euler_to_rotMat(roll, pitch, yaw):
    Rz = np.array([
        [np.cos(yaw), -np.sin(yaw), 0],
        [np.sin(yaw),  np.cos(yaw), 0],
        [          0,            0, 1]])
    Ry = np.array([
        [ np.cos(pitch), 0, np.sin(pitch)],
        [             0, 1,             0],
        [-np.sin(pitch), 0, np.cos(pitch)]])
    Rx = np.array([
        [1,            0,             0],
        [0, np.cos(roll), -np.sin(roll)],
        [0, np.sin(roll),  np.cos(roll)]])
    # R = RzRyRx
    rotMat=Rz@Ry@Rx
    return rotMat

roll = 2.6335
pitch = 0.4506
yaw = 1.1684

print("roll = ", roll)
print("pitch = ", pitch)
print("yaw = ", yaw)

print(euler_to_rotMat(roll, pitch, yaw))
