import wave
from struct import *

def loadnconvert(filename):
    n = 0
    frames = (0,)
    sound = wave.open(filename,'r')
    while sound.getnframes() > n:
        frames = frames + unpack('h', sound.readframes(1))
        sound.setpos(n)
        n += 100

    sound.close()
    return soundtomorse(frames)


def soundtomorse(frames):
    prevsilent = False
    silentdur = 0
    signaldur = 0
    morse = ""

    for sframe in frames:
        if abs(sframe) < 1000 and prevsilent == False:
            prevsilent = True
        elif abs(sframe) < 1000:
            if silentdur >= 44: #lenght of a paus
                morse = morse + " "
                silentdur = 0
            if signaldur > 10 and signaldur <= 24:
                morse = morse + "."
            elif signaldur > 24:
                morse = morse + "_"
            signaldur = 0
            silentdur += 1
            prevsilent = True
        else:
            signaldur += 1
            silentdur = 0
            prevsilent = False

    return morse
