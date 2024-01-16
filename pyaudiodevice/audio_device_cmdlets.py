import os
import re
import subprocess


# PowerShell命令
# powershell_command = "Get-Process"
#
# # 使用subprocess模块调用PowerShell
# result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)
#
# # 打印PowerShell命令的输出
# print("PowerShell Output:", result.stdout)
#
# # 打印PowerShell命令的错误（如果有的话）
# print("PowerShell Error:", result.stderr)
#
# "Import-Module .\AudioDeviceCmdlets.dll;"
class PyAudioDeviceCmdlets:
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib\AudioDeviceCmdlets.dll")
        self._import = f"Import-Module {self.path};"

    def __exec_powershell(self, cmd):
        # 使用subprocess模块调用PowerShell
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)

        if result.stderr != "":
            raise ValueError(result.stderr)
        else:
            return result.stdout

    def __convert_value(self,value):
        value = value.strip()
        if value.isdigit():
            return int(value)
        elif value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        elif value.find("%"):
            return float(value.replace("%",""))
        else:
            return value

    def __format_data(self, data):
        entries = re.split(r'\n\n+', data.strip())
        entry_dict = {}
        for entry in entries:
            lines = entry.split('\n')
            for line in lines:
                key, value = re.split(r'\s*:\s*', line)
                entry_dict[key.strip()] = self.__convert_value(value)
        return entry_dict

    def get_audio_device_list(self):
        powershell_command = "Get-AudioDevice -List"
        data = self.__exec_powershell(f"{self._import} {powershell_command}")
        entries = re.split(r'\n\n+', data.strip())

        result_dict = {}

        for entry in entries:
            entry_dict = {}
            lines = entry.split('\n')
            for line in lines:
                key, value = re.split(r'\s*:\s*', line)
                entry_dict[key.strip()] = self.__convert_value(value)
            name = entry_dict.get('Name')
            if name:
                result_dict[name] = entry_dict
        return result_dict

    def get_default_audio_device(self):
        powershell_command = "Get-AudioDevice -Playback"
        data = self.__exec_powershell(f"{self._import} {powershell_command}")
        return self.__format_data(data)

    def get_audio_device_by_id(self, id):
        powershell_command = f"Get-AudioDevice -ID {id}"
        data = self.__exec_powershell(f"{self._import} {powershell_command}")
        return data

    def get_audio_device_by_index(self, index: int):
        powershell_command = f"Get-AudioDevice -Index {str(index)}"
        data = self.__exec_powershell(f"{self._import} {powershell_command}")
        return self.__format_data(data)

    def get_audio_device_is_mute(self):
        powershell_command = f"Get-AudioDevice -PlaybackCommunicationMute"
        data = self.__exec_powershell(f"{self._import} {powershell_command}")
        return self.__convert_value(data)

    def get_audio_device_volume(self):
        powershell_command = f"Get-AudioDevice -PlaybackCommunicationVolume"
        data = self.__exec_powershell(f"{self._import} {powershell_command}")
        return self.__convert_value(data)


