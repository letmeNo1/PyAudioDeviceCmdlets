from pyaudiodevice.common import Common

a = Common()
print(a.get_audio_device_list())
print(a.set_default_communication_device_by_name("扬声器 (Jabra Engage 50 II)"))

from pyaudiodevice.common import Common

# Create an instance of DefaultPlayback
common = Common()

# Get the default playback device as <AudioDevice>
default_device = common.get_default_device()

print(default_device)