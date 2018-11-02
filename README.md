# Author
    deck in wonderland

# Description
    QlikViewのsettings.iniからSSEの設定を追加/削除します。

# Required File
    作業フォルダに"plugin_string.txt"が必要です。
    その際「SSEPlugin=」は不要です。

    設定ファイルの例:

        R,localhost:50051;Python,localhost:50052

# Command Option
    以下のどちらかが必須
        -a, --add: SSE設定を追加
        -r, --remove: SSE設定を削除
    
    以下のどちらかが必須
        -d, --desktop: Desktop版のsettings.iniを編集する
        -s, --server: Server版のsettings.iniを編集する

    コマンドの例:
        Desktop版のsetting.iniを対象にSSEPlugin設定を追加します。
        $ python qlikview_switch_SSE -a -d
    
        Desktop版のsetting.iniを対象にSSEPlugin設定を削除します。
        $ python qlikview_switch_SSE -r -d
