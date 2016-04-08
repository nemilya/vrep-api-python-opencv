# simple_image_retranslate.py
#
# Demo of simple image retranslate from v0 to v1

import vrep
import time

vrep.simxFinish(-1)

clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)

if clientID!=-1:
  print 'Connected to remote API server'

  # get vision sensor objects
  res, v0 = vrep.simxGetObjectHandle(clientID, 'v0', vrep.simx_opmode_oneshot_wait)
  res, v1 = vrep.simxGetObjectHandle(clientID, 'v1', vrep.simx_opmode_oneshot_wait)


  err, resolution, image = vrep.simxGetVisionSensorImage(clientID, v0, 0, vrep.simx_opmode_streaming)
  time.sleep(1)

  while (vrep.simxGetConnectionId(clientID) != -1):
    err, resolution, image = vrep.simxGetVisionSensorImage(clientID, v0, 0, vrep.simx_opmode_buffer)
    if err == vrep.simx_return_ok:
      vrep.simxSetVisionSensorImage(clientID, v1, image, 0, vrep.simx_opmode_oneshot)
    elif err == vrep.simx_return_novalue_flag:
      print "no image yet"
    else:
      print err
else:
  print "Failed to connect to remote API Server"
  vrep.simxFinish(clientID)