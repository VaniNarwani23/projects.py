

from gtts import gTTS
import os    
x=input("what do you want to listen:")
gtts = gTTS(text=x)
gtts.save("pcvoice.mp3")
# to start the file from python
os.system("start pcvoice.mp3")

print("\nA music file named pcvoice.mp3 has been added to the repl.")