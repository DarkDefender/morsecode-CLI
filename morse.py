import sys
import morsealf
import playmorse
import sound

def convtomorse(word,morse):
    strpos = 0
    while strpos <= len(word) - 1:
        morse = morse + morsealf.signtomorse(arg[strpos])
        strpos += 1
    morse = morse + "  " #end of word
    return morse

def convtotext(morsecode):
    text = ""
    morse = ""
    strpos = 0
    while strpos <= len(morsecode) - 1:
        if str.isspace(morsecode[strpos]):
            if str.isspace(morsecode[strpos:strpos + 5]):
                text = text + morsealf.morsetosign(morse) + " "
                strpos += 5
                morse = ""
            elif str.isspace(morsecode[strpos:strpos + 3]):
                text = text + morsealf.morsetosign(morse)
                strpos += 3
                morse = ""
            elif str.isspace(morsecode[strpos:strpos + 2]):
                print("Expected 1,3 or 5 number of spaces at pos " + str(strpos))
                break
        morse = morse + morsecode[strpos]
        strpos += 1
    text = text + morsealf.morsetosign(morse) #end of line
    return text

if sys.argv[1] == "-m":
    morsecode = sys.argv[2]
    print(convtotext(morsecode))

elif sys.argv[1] == "-p":
    morse = ""
    for arg in sys.argv[2:]:
        morse = convtomorse(arg,morse)
    playmorse.morsetosound(morse)

elif sys.argv[1] == "-d":
     morsecode = sound.loadnconvert(sys.argv[2])
     print(morsecode.strip())
     print(convtotext(morsecode.strip()))

else:
    morse = ""
    for arg in sys.argv[1:]:
        morse = convtomorse(arg,morse)
    print(morse)
