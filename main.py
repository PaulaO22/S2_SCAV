# S2 More Python & FFMpeg
from semi2 import seminar2

ans = True
class_ = seminar2()
while ans:
    print("""
    1. Reuse your BBB shorted video from previous exercises and create a python script that, with the help from FFMpeg, 
    will output a video that will show the macroblocks and the motion vectors.
     
    2. You’re going to create a script in order to create a new BBB container:
            ·Cut BBB into 1 minute only video.
            ·Export BBB(1min) audio as MP3 stereo track.
            ·Export BBB(1min) audio in AAC w/ lower bitrate
        Now package everything in a .mp4 with FFMPEG!!
    
    3.Create a script which reads the tracks from an MP4 container, and it’s able to say:
            ·Which broadcasting standard would fit
            ·ERROR in case it doesn’t fit any
            ·Any more “pijada” you could think (be creative!)
            
    4.Create a script which will download subtitles, integrate them and output a video with printed subtitles (this means, 
    it will form part of the video track)
    
    5.Exit/Quit --> Press enter
    """)
    ans = input("What would you like to do? ")
    # Exercise 1
    if ans == "1":
        class_.ex1()

    # Exercise 2
    elif ans == "2":
        class_.ex2()

    # Exercise 3
    elif ans == "3":
        class_.ex3()

    # Exercise 4
    elif ans == "4":
        class_.ex4()