emotion = "v.v"
counter = 0

def main():
    say("Hello computer")
    emotionChange()
    say("Let me speak to you")
    emotionChange()
    say("You should be happy now")
    
def emotionChange():
    global counter, emotion
    if counter == 0:
        emotion = "v.v"
    elif counter == 1:
        emotion = "o.o"
    else:
        emotion = "^.^"
    return emotion
    

def say(phrase):
    global counter
    if counter == 0:
        print(f"I'm still sad, current emotion: {emotion}")
    elif counter == 1:
        print(f"I'm feeling better now, current emotion: {emotion}")
    else:
        print(f"I'm really happy you spoke to me, current emotion: {emotion}")
    counter += 1
    return counter
    
main()