"""
========================================
06_real_world_multiple_inheritance.py
========================================
Real-world Example:

✔ Device + Camera + Phone
"""

class Camera:
    def camera_feature(self):
        print("Camera: Taking photo")

class Phone:
    def call_feature(self):
        print("Phone: Making call")

class SmartPhone(Camera, Phone):
    def app_feature(self):
        print("Smartphone: Running apps")

sp = SmartPhone()

sp.camera_feature()
sp.call_feature()
sp.app_feature()