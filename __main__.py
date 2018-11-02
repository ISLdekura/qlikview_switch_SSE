"""
deck in wonderland 20181102
QlikViewのsettings.iniからSSEの設定を追加/削除を行います。
コマンドラインオプション:
    以下のどちらかが必須
    -a, --add: SSE設定を追加
    -r, --remove: SSE設定を削除
    以下のどちらかが必須
    -d, --desktop: Desktop版のsettings.iniを参照
    -s, --server: Server版のsettings.iniを参照
"""

import os
import argparse
import configparser


class SwitchSettings:
    def __init__(self, **kwargs):
        # SSEプラグインの設定内容
        # "SSEPlugin="を含まない内容で追加したい1行を記述します。
        with open("plugin_string.txt", "r") as f:
            self.plugin_string = f.readline()

        # settings.iniの場所
        if kwargs["desktop"] and kwargs["server"]:
            raise RuntimeError("Both of Desktop and Server mode selected")
        if (not kwargs["desktop"]) and (not kwargs["server"]):
            raise RuntimeError("Location required")
        self.settings_file_location = None
        if kwargs["desktop"]:
            self.settings_file_location = os.getenv('APPDATA') + r"\QlikTech\QlikView\settings.ini"
        if kwargs["server"]:
            self.settings_file_location = r"C:\ProgramData\QlikTech\QlikViewServer\settings.ini"

        # モード設定
        if kwargs["add"] and kwargs["remove"]:
            raise RuntimeError("Both of Add and Remove mode selected")
        if (not kwargs["add"]) and (not kwargs["remove"]):
            raise RuntimeError("Mode required")
        self.mode_add = kwargs["add"]
        self.mode_remove = kwargs["remove"]

    def add_settings(self):
        config = configparser.ConfigParser()
        config.read(self.settings_file_location, encoding="utf_8_sig")
        config.set(section="Settings 7", option="SSEPlugin", value=self.plugin_string)
        with open(self.settings_file_location, "w", encoding="utf_8_sig") as f:
            config.write(f, space_around_delimiters=False)

    def remove_settings(self):
        config = configparser.ConfigParser()
        config.read(self.settings_file_location, encoding="utf_8_sig")
        config.remove_option(section="Settings 7", option="SSEPlugin")
        with open(self.settings_file_location, "w", encoding="utf_8_sig") as f:
            config.write(f, space_around_delimiters=False)

    def do_switch(self):
        if self.mode_add:
            self.add_settings()
        if self.mode_remove:
            self.remove_settings()


def main():
    # 引数を解釈
    parser = argparse.ArgumentParser(description="Mode")
    parser.add_argument("-a", "--add", help="Add SSE Settings", action="store_true")
    parser.add_argument("-r", "--remove", help="Remove SSE Settings", action="store_true")
    parser.add_argument("-d", "--desktop", help="Desktop Mode", action="store_true")
    parser.add_argument("-s", "--server", help="Server mode", action="store_true")
    args = parser.parse_args()

    print(args)

    ss = SwitchSettings(
        add=args.add,
        remove=args.remove,
        desktop=args.desktop,
        server=args.server)

    ss.do_switch()


if __name__ == "__main__":
    main()
