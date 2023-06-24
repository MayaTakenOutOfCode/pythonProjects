import random
import gtts
from pynput.keyboard import Key, Controller

import speech_recognition as sr
import pyautogui as keyboard


print("++++++++++++++++++++++++++++++\n")



def generateSubAudio(af,af2):
    
    affs1 = ""
    affs2 = ""
          
    for ele in af:
        affs1 += ele
        tts = gtts.gTTS(affs1, slow=False )
        tts.save("affs1.wav")
    
    for ele in af2:
        affs2 += ele
        tts = gtts.gTTS(affs2, slow=False )
        tts.save("affs2.wav")
def useKeyboard():
    af = []
    num1 = int(input(
    "Enter a number that represents an amount of affirmations you're gonna use: "
    ))
    if num1 <=0:
        print("You gotta write positive and not equal 0")
    else:
        for i in range(0,num1):
            ele = str(input("Affirmation(subliminal):"))
            af.append(ele + ".")

    af2 = []

    num2 = int(input("Enter a number that represents amount of booster affirmations you will use: "))

    if num2 <=0:
        print("You gotta write positive and not equal 0 ")
    else:
        for k in range(0,num2):
            ele2 = str(input("Affirmation(boost):"))
    
            af2.append(ele2 + ".")
    random.shuffle(af)
    random.shuffle(af2)
    generateSubAudio(af, af2)    
    
def chooseMethod():
    print("Choose k - keyboard affs, v - voice affs\n")
    key = input('Your choice: ')
    if(key == 'k'):
        useKeyboard()
    elif(key == 'v'):
        useVoice()
    else:
        print("This is not avalible for you, the key you can only use are: k, v")
        
def useVoice():
    
    af = []

    num1 = int(input(
        "Enter a number that represents an amount of affirmations you're gonna use: "
    ))

    if num1 <=0:
        print("You gotta write positive and not equal 0")
    else:
        for i in range(0,num1):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            inp = r.recognize_google(audio)
            ele = inp+"\n";
    
            af.append(ele + ".")

    af2 = []

    num2 = int(input("Enter a number that represents amount of booster affirmations you will use: "))

    if num2 <=0:
        print("You gotta write positive and not equal 0 ")
    else:
        for k in range(0,num2):
            r2 = sr.Recognizer()
            with sr.Microphone() as source2:
                audio2 = r.listen(source2)
            inp2 = r.recognize_google(audio2)
            ele2 = inp2+"\n";
    
            af2.append(ele2 + ".")
    random.shuffle(af)
    random.shuffle(af2)
    generateSubAudio(af, af2)
chooseMethod()
#print(af, "\n",af2)

print("++++++++++++++++++++++++++++++")
print("Thx for using me!")
