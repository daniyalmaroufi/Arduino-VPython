import numpy as np

def cpm(r):
    cpm_r=np.array([[0, -r[2], r[1]],
    [r[2], 0, r[0]],
    [-r[1], r[0], 0]])
    return cpm_r

def quat_to_rotMat(r0,r):
    rotmat=(r0**2-np.dot(r,r))*np.eye(3)+2*r@r.T+2*r0*cpm(r)
    return rotmat


