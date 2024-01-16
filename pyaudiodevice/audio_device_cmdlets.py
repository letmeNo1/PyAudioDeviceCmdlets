import os
import re
import subprocess


class PyAudioDeviceCmdlets:
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib\AudioDeviceCmdlets.dll")
        self._import = f"Import-Module {self.path};"

    def _exec_powershell(self, cmd):
        # 使用subprocess模块调用PowerShell
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)

        if result.stderr != "":
            raise ValueError(result.stderr)
        else:
            return result.stdout

    def _convert_value(self, value):
        value = value.strip()
        if value.isdigit():
            return int(value)
        elif value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        elif value.find("%") > 0:
            print(value)
            return float(value.replace("%", ""))
        else:
            return value

    def _format_data(self, data):
        entries = re.split(r'\n\n+', data.strip())
        entry_dict = {}
        for entry in entries:
            lines = entry.split('\n')
            for line in lines:
                key, value = re.split(r'\s*:\s*', line)
                entry_dict[key.strip()] = self._convert_value(value)
        return entry_dict

    '''
    Get the device with the ID corresponding to the given <string>
    '''

    def get_audio_device_by_id(self, id):
        powershell_command = f"Get-AudioDevice -ID {id}"
        data = self._exec_powershell(f"{self._import} {powershell_command}")
        return data

    '''
    Get the device with the Index corresponding to the given <int>
    '''

    def get_audio_device_by_index(self, index: int):
        powershell_command = f"Get-AudioDevice -Index {str(index)}"
        data = self._exec_powershell(f"{self._import} {powershell_command}")
        return self._format_data(data)

    '''
    Get a list of all enabled devices as <AudioDevice>
    '''

    def get_audio_device_list(self):
        powershell_command = "Get-AudioDevice -List"
        data = self._exec_powershell(f"{self._import} {powershell_command}")
        entries = re.split(r'\n\n+', data.strip())

        result_dict = {}

        for entry in entries:
            entry_dict = {}
            lines = entry.split('\n')
            for line in lines:
                key, value = re.split(r'\s*:\s*', line)
                entry_dict[key.strip()] = self._convert_value(value)
            name = entry_dict.get('Name')
            if name:
                result_dict[name] = entry_dict
        return result_dict

    '''
    Set the given playback/recording device as both the default device and the default communication device, for its type
    '''

    def set_default_communication_device(self, audio_device: str):
        powershell_command = f"Set-AudioDevice {audio_device}"
        self._exec_powershell(f"{self._import} {powershell_command}")

    '''
    Set the given playback/recording device as the default communication device and not the default device, for its type
    '''

    def set_communication_only_device(self, audio_device: str):
        powershell_command = f"Set-AudioDevice {audio_device} -CommunicationOnly"
        self._exec_powershell(f"{self._import} {powershell_command}")

    '''
    Set the given playback/recording device as the default device and not the default communication device, for its type
    '''

    def set_default_only_device(self, audio_device: str):
        powershell_command = f"Set-AudioDevice {audio_device} -DefaultOnly"

        self._exec_powershell(f"{self._import} {powershell_command}")

    '''
    Set the device with the ID corresponding to the given <string> as both the default device and the default communication device, for its type
    '''

    def set_default_communication_device_by_name(self, name: str):
        device_list = self.get_audio_device_list()
        powershell_command = f'''Set-AudioDevice -ID "{device_list.get(name).get('ID')}"'''
        self._exec_powershell(f"{self._import} {powershell_command}")

    '''
    Set the device with the ID corresponding to the given <string> as the default communication device and not the default device, for its type
    '''

    def set_communication_only_device_by_name(self, name: str):
        device_list = self.get_audio_device_list()

        powershell_command = f'''Set-AudioDevice -ID "{device_list.get(name).get('ID')}" -CommunicationOnly'''
        self._exec_powershell(f"{self._import} {powershell_command}")

    '''
    Set the device with the ID corresponding to the given <string> as the default device and not the default communication device, for its type
    '''

    def set_default_only_device_by_name(self, name: str):
        device_list = self.get_audio_device_list()
        powershell_command = f'''Set-AudioDevice -ID "{device_list.get(name).get('ID')}" -DefaultOnly'''
        self._exec_powershell(f"{self._import} {powershell_command}")

    '''
    Set the device with the ID corresponding to the given <string> as both the default device and the default communication device, for its type
    '''

    def set_default_communication_device_by_id(self, device_id: str):
        powershell_command = f'''Set-AudioDevice -ID "{device_id}"'''
        self._exec_powershell(f"{self._import} {powershell_command}")

    '''
    Set the device with the ID corresponding to the given <string> as the default communication device and not the default device, for its type
    '''

    def set_communication_only_device_by_id(self, device_id: str):
        powershell_command = f'''Set-AudioDevice -ID "{device_id}" -CommunicationOnly'''
        self._exec_powershell(f"{self._import} {powershell_command}")

    '''
    Set the device with the ID corresponding to the given <string> as the default device and not the default communication device, for its type
    '''

    def set_default_only_device_by_id(self, device_id: str):
        powershell_command = f'''Set-AudioDevice -ID "{device_id}" -DefaultOnly'''
        self._exec_powershell(f"{self._import} {powershell_command}")

    '''
    Set the device with the Index corresponding to the given <int> as both the default device and the default communication device, for its type
    '''

    def set_default_communication_device_by_index(self, device_index: int):
        powershell_command = f'''Set-AudioDevice -Index "{device_index}"'''
        self._exec_powershell(f"{self._import} {powershell_command}")

    '''
    Set the device with the Index corresponding to the given <int> as the default communication device and not the default device, for its type
    '''

    def set_communication_only_device_by_index(self, device_index: int):
        powershell_command = f'''Set-AudioDevice -Index "{device_index}" -CommunicationOnly'''
        self._exec_powershell(f"{self._import} {powershell_command}")

    '''
    Set the device with the Index corresponding to the given <int> as the default device and not the default communication device, for its type
    '''

    def set_default_only_device_by_index(self, device_index: int):
        powershell_command = f'''Set-AudioDevice -Index "{device_index}" -DefaultOnly'''
        self._exec_powershell(f"{self._import} {powershell_command}")
