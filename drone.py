from pyparrot.Minidrone import Mambo
from pyparrot.DroneVision import DroneVision
from pyparrot.Model import Model
import threading
import cv2
import time

mambo = Mambo(mamboAddr, use_wifi=True)
print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)
    print("Preparing to open vision")
    mamboVision = DroneVision(mambo, Model.MAMBO, buffer_size=30)
    userVision = UserVision(mamboVision)
    mamboVision.set_user_callback_function(userVision.save_pictures, user_callback_args=None)
    success = mamboVision.open_video()
    print("Success in opening vision is %s" % success)

    print("taking off!")
    mambo.safe_takeoff(5)
    print("shoot the gun")
    mambo.fire_gun()

    print("Flying direct: yaw")
    mambo.fly_direct(roll=0, pitch=0, yaw=50, vertical_movement=0, duration=1)

    print("Flying direct: going backwards (negative pitch)")
    mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=0.5)

    print("Ending the sleep and vision")
    mamboVision.close_video()

    mambo.smart_sleep(5)

    print("disconnecting")
    mambo.disconnect()
