#!/bin/sh
python3 status/download.py &
sleep 10
pkill -f "download.py"
pkill ffmpeg
