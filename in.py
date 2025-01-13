import whisper
import ffmpeg
import numpy as np
from datetime import timedelta
import traceback
from mutagen.mp3 import MP3
import argparse

# ... existing code ...

# main code 

model = whisper.load_model("base") #small

# ... existing code ...

print (stringgy)

# {{ edit_1 }}
# Create requirements.txt
with open("requirements.txt", "w") as f:
    f.write("whisper\n")
    f.write("ffmpeg-python\n")
    f.write("numpy\n")
    f.write("mutagen\n")