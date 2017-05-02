import os
from gtts import gTTS
from mutagen.mp3 import MP3
from glob import glob
from datetime import timedelta

print()

total = 0

for filename in sorted(glob('*.txt')):

    basename, _ = os.path.splitext(filename)

    with open(filename) as f:
        tts = gTTS(text=f.read(), lang='en')
        tts.save(f'{basename}.mp3')

    audio = MP3(f'{basename}.mp3')
    total += audio.info.length
    print(f' {filename:<30} : {timedelta(seconds=audio.info.length)}') 

print(f' {"total":<30} : {timedelta(seconds=total)}')
print()