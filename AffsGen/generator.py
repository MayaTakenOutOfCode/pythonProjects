import random
import gtts

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

print("++++++++++++++++++++++++++++++")
print("Thx for using me!")
