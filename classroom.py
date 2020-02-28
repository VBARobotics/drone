from pyparrot.Minidrone import Mambo
import threading
import time
red="e0:14:19:8e:3d:cf"
blue="d0:3a:27:16:e6:3b"
mamboAddr=blue
gun="off"
mambo = Mambo(mamboAddr, use_wifi=False)
print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)
    print("taking off!")
    mambo.safe_takeoff(2)
    if gun == 'on':
        print("shoot the gun")
        for shots in range(3):
           print("Fire: " + str(shots))
           mambo.fire_gun()
           mambo.smart_sleep(2)

    mambo.smart_sleep(2)
    print("Room Length")
    mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=2)
    mambo.smart_sleep(5)

#    print("Flying direct: going around in a circle (yes you can mix roll, pitch, yaw in one command!)")
#    mambo.fly_direct(roll=-25, pitch=0, yaw=-40, vertical_movement=-10, duration=3)

    print("Room Arc")
    mambo.fly_direct(roll=-25, pitch=0, yaw=-30, vertical_movement=-10, duration=3)
    mambo.fly_direct(roll=-25, pitch=0, yaw=0, vertical_movement=0, duration=1)
    print("Flying direct: going backwards (negative pitch)")
#    mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=0.5)

    mambo.smart_sleep(2)
    print("landing")
    mambo.safe_land(3)

    print("disconnecting")
    mambo.disconnect()
