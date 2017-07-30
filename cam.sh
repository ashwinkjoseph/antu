#! bin/bash

sudo modprobe v4l2loopback devices=2
ffmpeg -f video4linux2 -s 1000x1000 -i /dev/video0 -c copy -f v4l2 /dev/video2 -f v4l2 /dev/video1
