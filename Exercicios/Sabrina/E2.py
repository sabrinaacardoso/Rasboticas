
import sim
import time
sim.simxFinish(-1) 

clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) 
# start a connnection

if clientID!=-1:
    print ("Connected to remote API server")
else:
    print("Not connected to remote API serv")

#Starting the code

#Iniciando Motores
err_codel,l_motor_handle = sim.simxGetObjectHandle(clientID,"Pioneer_p3dx_leftMotor", sim.simx_opmode_blocking)
err_coder,r_motor_handle = sim.simxGetObjectHandle(clientID,"Pioneer_p3dx_rightMotor", sim.simx_opmode_blocking)

#Iniciando Sensores
err_Sensorl, l_sensorHandle = sim.simxGetObjectHandle(clientID,"Pioneer_p3dx_ultrasonicSensor4",sim.simx_opmode_oneshot_wait)
err_Sensorl, state_Sensorl, coord_Sensorl, detectedObjectHandle_Sensorl, detectedSurfaceNormalVector_Sensorl = sim.simxReadProximitySensor(clientID, l_sensorHandle,sim.simx_opmode_streaming)
err_Sensorr, r_sensorHandle = sim.simxGetObjectHandle(clientID,"Pioneer_p3dx_ultrasonicSensor5",sim.simx_opmode_oneshot_wait)
err_Sensorr, state_Sensorr, coord_Sensorr, detectedObjectHandle_Sensorr, detectedSurfaceNormalVector_Sensorr = sim.simxReadProximitySensor(clientID, r_sensorHandle,sim.simx_opmode_streaming)


while(clientID!=-1):
    #Chamada dos sensores
    err_Sensorl, state_Sensorl, coord_Sensorl, detectedObjectHandle_Sensorl, detectedSurfaceNormalVector_Sensorl = sim.simxReadProximitySensor(clientID, l_sensorHandle,sim.simx_opmode_streaming)
    err_Sensorr, state_Sensorr, coord_Sensorr, detectedObjectHandle_Sensorr, detectedSurfaceNormalVector_Sensorr = sim.simxReadProximitySensor(clientID, r_sensorHandle,sim.simx_opmode_streaming)
    #Respostas dos sensores
    #print(err_Sensorl)
    #print(err_Sensorr)
    print(state_Sensorl)
    print(state_Sensorr)
    #print(coord_Sensorl)
    #print(coord_Sensorr)
    #print(detectedObjectHandle_Sensorl)
    #print(detectedObjectHandle_Sensorr)
    #print(detectedSurfaceNormalVector_Sensorl)
    #print(detectedSurfaceNormalVector_Sensorr)
    if(state_Sensorl == True or state_Sensorr == True):
        err_code = sim.simxSetJointTargetVelocity(clientID,l_motor_handle,1.0,sim.simx_opmode_streaming)
        err_code = sim.simxSetJointTargetVelocity(clientID,r_motor_handle,0.0,sim.simx_opmode_streaming)
    else:
        err_code = sim.simxSetJointTargetVelocity(clientID,l_motor_handle,1.0,sim.simx_opmode_streaming)
        err_code = sim.simxSetJointTargetVelocity(clientID,r_motor_handle,1.0,sim.simx_opmode_streaming)
