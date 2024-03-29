## Description
AudioDeviceCmdlets is a suite of PowerShell Cmdlets to control audio devices on Windows


## Features
Get list of all audio devices  
Get default audio device (playback/recording)  
Get default communication audio device (playback/recording)  
Get volume and mute state of default audio device (playback/recording)  
Get volume and mute state of default communication audio device (playback/recording)  
Set default audio device (playback/recording)  
Set default communication audio device (playback/recording)  
Set volume and mute state of default audio device (playback/recording)  
Set volume and mute state of default communication audio device (playback/recording)


## Installation
pip install pyaudiodevice


## Usage
```
from your_module_name import DefaultPlayback

# Get the default playback device's mute state as <bool>
is_mute = default_playback.get_is_mute()

# Get the default playback device's volume level on 100 as <float>
volume_level = default_playback.get_volume()

# Set the default playback device's mute state to the opposite of its current mute state
default_playback.toggle_mute()

# Set the default playback device's mute state to the given <bool>
default_playback.set_mute(True)

# Set the default playback device's volume level on 100 to the given <float>
default_playback.set_volume(0.5)

```

```
from pyaudiodevice.common import Common

# Create an instance of DefaultPlayback
common = Common()

# Get the default playback device as <AudioDevice>
default_device = common.get_default_device()

# Get a list of all enabled devices as <AudioDevice>
device_list = common.get_audio_device_list()

# Get the device with the Index corresponding to the given <int>
device_info = common.get_audio_device_by_index(index)

# Get the device with the ID corresponding to the given <string>
device_info = common.get_audio_device_by_id(id)
```





## Attribution
Based on code 
https://github.com/frgnca/AudioDeviceCmdlets
