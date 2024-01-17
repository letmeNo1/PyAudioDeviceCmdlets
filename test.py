from pyaudiodevice.audio_common import AudioCommon

a = AudioCommon()
# print(a.get_audio_device_list())
# print(a.set_default_communication_device_by_name("扬声器 (Jabra Engage 50 II)"))


# Create an instance of DefaultPlayback
common = AudioCommon()

# Get the default playback device as <AudioDevice>
default_device = common.get_audio_device_list()

print(default_device)