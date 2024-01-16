from typing import Dict, Any, Union, List

class PyAudioDeviceCmdlets:
    def __init__(self) -> None:
        self._import = None
        self.path = None
        self.path: str
        self._import: str

    def __exec_powershell(self, cmd: str) -> str:
        ...

    def __convert_value(self, value: str) -> Any:
        ...

    def __format_data(self, data: str) -> Dict[str, Any]:
        ...

    def get_audio_device_list(self) -> Dict[str, Dict[str, Any]]:
        # Get a list of all enabled devices as <AudioDevice>
        ...

    def get_default_audio_device(self) -> Dict[str, Any]:
        # Get the default communication playback device as <AudioDevice>
        ...

    def get_audio_device_by_id(self, audio_id: str) -> str:
        # Get the device with the ID corresponding to the given <string>
        ...

    def get_audio_device_by_index(self, index: int) -> Dict[str, Any]:
        # Get the device with the Index corresponding to the given <int>
        ...

    def get_audio_device_is_mute(self) -> Union[bool, float]:
        # Get the default communication playback device's mute state as <bool>
        ...

    def get_audio_device_volume(self) -> Union[bool, float]:
        # Get the default communication playback device's volume level on 100 as <float>
        ...
