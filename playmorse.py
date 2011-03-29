import pygame

def playmorse(sound):
    if sound == "short":
        pygame.mixer.music.load("sounds/morse_short.wav")
    elif sound == "long":
        pygame.mixer.music.load("sounds/morse_long.wav")
    elif sound == "silence":
        pygame.mixer.music.load("sounds/silenceshort.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        game = ""

def morsetosound(morsecode):
    pygame.mixer.pre_init(44100, -16, 2)
    pygame.init()
    strpos=0
    while strpos <= len(morsecode) - 1:
        if morsecode[strpos] == ".":
            playmorse("short")
        elif morsecode[strpos] == "_":
            playmorse("long")
        else:
            playmorse("silence")
        strpos += 1

pygame.quit()
