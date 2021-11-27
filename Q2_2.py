import time
import serial
import numpy as np
from vpython import *

# use_from='quaternion'
use_from='roll_pitch_yaw'

arduinoData = serial.Serial('/dev/ttyACM0', 115200)
time.sleep(1)

scene.range=5
toRad=2*np.pi/360
toDeg=1/toRad
scene.forward=vector(-1,-1,-1)
scene.width=600
scene.height=600

xarrow=arrow(lenght=2, shaftwidth=.1, color=color.red,axis=vector(1,0,0))
yarrow=arrow(lenght=2, shaftwidth=.1, color=color.green,axis=vector(0,1,0))
zarrow=arrow(lenght=4, shaftwidth=.1, color=color.blue,axis=vector(0,0,1))

frontArrow=arrow(length=4,shaftwidth=.1,color=color.purple,axis=vector(1,0,0))
upArrow=arrow(length=1,shaftwidth=.1,color=color.magenta,axis=vector(0,1,0))
sideArrow=arrow(length=2,shaftwidth=.1,color=color.orange,axis=vector(0,0,1))

bBoard=box(length=6,width=2,height=.2,opacity=.8,pos=vector(0,0,0,))
bn=box(length=1,width=.75,height=.1, pos=vector(-.5,.1+.05,0),color=color.blue)
nano=box(lenght=1.75,width=.6,height=.1,pos=vector(-2,.1+.05,0),color=color.green)
myObj=compound([bBoard,bn,nano])



while True:
    while arduinoData.inWaiting() == 0:
        pass
    dataPacket = arduinoData.readline()
    try:
        dataPacket = str(dataPacket, 'utf-8')

        if use_from == 'quaternion':
            splitPacket=dataPacket.split(",")
            q0=float(splitPacket[0])
            q1=float(splitPacket[1])
            q2=float(splitPacket[2])
            q3=float(splitPacket[3])
    
            roll=-np.atan2(2*(q0*q1+q2*q3),1-2*(q1*q1+q2*q2))
            pitch=np.asin(2*(q0*q2-q3*q1))
            yaw=-np.atan2(2*(q0*q3+q1*q2),1-2*(q2*q2+q3*q3))-np.pi/2
        else:
            splitPacket = dataPacket.split(",")
            roll = float(splitPacket[0])*toRad
            pitch = float(splitPacket[1])*toRad
            yaw = float(splitPacket[2])*toRad+3.141592

        rate(50)
        k=vector(cos(yaw)*cos(pitch), sin(pitch),sin(yaw)*cos(pitch))
        y=vector(0,1,0)
        s=cross(k,y)
        v=cross(s,k)
        vrot=v*cos(roll)+cross(k,v)*sin(roll)

        frontArrow.axis=k
        sideArrow.axis=cross(k,vrot)
        upArrow.axis=vrot
        myObj.axis=k
        myObj.up=vrot
        sideArrow.length=2
        frontArrow.length=4
        upArrow.length=1
    except:
        pass



