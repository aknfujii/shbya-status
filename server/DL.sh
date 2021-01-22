#!/bin/sh
# 10秒動画をダウンロード　残っているプロセスを削除
python download.py &
sleep 10
pkill -f "download.py"
pkill ffmpeg
