# looks for new folders in the user_uploads, if that is not yet processed, it generates the process.
import os

def text_to_audio(folder):
    print("working 1",folder)
def generate_reel(folder):
    print("working 2",folder)

if __name__=="__main__":
    with open("handled.txt","r") as f:
        handled_folders=f.readlines()
        handled_folders=[f.strip() for f in handled_folders]
    folders=os.listdir("user_uploads")
    
    for folder in folders:
        if(not(folder  in handled_folders)):

            text_to_audio(folder) #generate audio mp3 from prompt.txt
            generate_reel(folder) #convert image and audio in the folder into a reel
            with open("handled.txt","a") as f:
                f.write(folder + "\n")