# Video Converter
This is a small script tool to convert from/to any video format keeping the same directory structure.

It can be useful for who needs more control while converting videos. 

# How it works
This tool relies on [ffmpeg tool](https://www.ffmpeg.org/) for the hard work of converting the videos between almost any available format.

The only concern of this tool is to recursively scan the *input* directory and write the output to a folder *input*/**converted**, keeping the same directories structure of the input.

# Dependencies
To run this script you'll need to install:
- [python >= 3.8](https://www.python.org/downloads/)
- [ffmpeg tool](https://www.ffmpeg.org/) 

# Running
To execute  the script you'll type in your terminal:
```
python convert.py
```

The program will prompt you to provide arguments.

This is an example of use converting all **mpg** video from directory **/home/user/Desktop** to **avi** format.  
```
 enter the source directory containing the media files: /home/user/Desktop
 enter the input format ex.: mpg, asf, mpeg: mpg
 enter the output format ex.: avi, mp4: avi
```

This is the output:
```
converted /home/user/Desktop/videos/video.mpg to /home/user/Desktop/converted/videos/video.avi
converted /home/user/Desktop/videos/sub-dir/video-b.mpg to /home/user/Desktop/converted/videos/sub-dir/video-b.avi
```