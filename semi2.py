import subprocess
import requests
from videoprops import get_audio_properties
from videoprops import get_video_properties

class seminar2:
    def ex1(self):
        subprocess.call(
            ['ffmpeg', '-flags2', '+export_mvs', '-i', '1min.mp4', '-vf',
             'codecview=mv=pf+bf+bb', 'output.mp4'])

    def ex2(self):
        # First we create a 1 minute video
        subprocess.call(
            ['ffmpeg', '-ss', '00:00:00', '-i', 'bbb.mp4', '-to', '00:01:00',
             '-c', 'copy', '1min.mp4'])

        # Export the 1 min audio as MP3 stereo audio track
        subprocess.call(
            ['ffmpeg', '-i', '1min.mp4', '-vn', '-acodec', 'mp3', 'bbbMP3.mp3'])

        # Export BBB(1min) audio in AAC w/ lower bitrate
        subprocess.call(
            ['ffmpeg', '-i', '1min.mp4', '-vn', '-acodec', 'aac', 'bbbMP3.aac'])

        # Create container
        subprocess.call(
            ['ffmpeg', '-i', '1min.mp4', '-i', 'bbbMP3.mp3', '-i', 'bbbMP3.aac',
             '-map', '0:v', '-map', '1:a', '-map', '2:a', 'container.mp4'])

    def ex3(self):
        # Read the tracks from an MP4 container
        video_prop = get_video_properties('container.mp4')
        audio_prop = get_audio_properties('container.mp4')

        # broadcastings
        DVB = {'video': ['mpeg2', 'h264', 'none', 'none'],
               'audio': ['aac', 'ac3', 'mp3', 'none']}
        ISDB = {'video': ['mpeg2', 'h264', 'none', 'none'],
                'audio': ['aac', 'none', 'none', 'none']}
        ATSC = {'video': ['mpeg2', 'h264', 'none', 'none'],
                'audio': ['none', 'none', 'none', 'none']}
        DTMB = {'video': ['avs', 'avs+', 'mpeg2', 'h264'],
                'audio': ['aac', 'ac3', 'mp3', 'none']}

        for i in range(4):
            for j in range(4):
                if DVB['video'][i] == video_prop['codec_name'] and \
                        DVB['audio'][j] == audio_prop['codec_name']:
                    print('The broadcasting standard DVB fits')

                if ISDB['video'][i] == video_prop['codec_name'] and \
                        ISDB['audio'][j] == audio_prop['codec_name']:
                    print('The broadcasting standard ISDB fits')

                if ATSC['video'][i] == video_prop['codec_name'] and \
                        ATSC['audio'][j] == audio_prop['codec_name']:
                    print('The broadcasting standard ATSC fits')

                if DTMB['video'][i] == video_prop['codec_name'] and \
                        DTMB['audio'][j] == audio_prop['codec_name']:
                    print('The broadcasting standard DTMB fits')
    def ex4(self):
        response = requests.get(
            "https://raw.githubusercontent.com/PaulaO22/Subtitles/main/big_buck_bunny.eng.srt")
        print(response.content)

        with open("bbb_subtitles.srt", 'wb') as f:
            f.write(response.content)  # Extract content from file
        subprocess.call(['ffmpeg', '-i', '1min.mp4', '-vf',
                         'subtitles=big_buck_bunny.eng.srt',
                         'mysubtitledmovie.mp4'])

