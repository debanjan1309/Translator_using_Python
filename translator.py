# import libraries
from translate import Translator
import pyttsx3

# input section
line=input("Text:") # taking input of the text
fl=input("Given language:") # language of the given text
tl=input("Translation language:") # language of the given text

# translation work
translator=Translator(from_lang=fl, to_lang=tl)
translation=translator.translate(line)
print(translation)

# audio generation
text=open("book.txt", "w") # creating text file
text.write(translation) # writting text file
text.close()
book=open(r"book.txt") # openning text file
book_text=book.readlines() # reaading text file
engine=pyttsx3.init()
hear=input("speak?(yes/no):") # user input for audio
if (hear== "yes" or hear== "Yes"):
    for i in book_text:
        engine.say(i) # generation of audio
        engine.runAndWait()