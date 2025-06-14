# looks for new folders in the user_uploads, if that is not yet processed, it generates the process.
import os
from text_to_audio import text_to_speech_file
import subprocess

def text_to_audio(folder):
    print("working 1",folder)
    #getting the text from the folder
    with open(f"user_uploads/{folder}/prompt.txt") as f:
        text=f.read()
    print(text, folder)
    text_to_speech_file(text, folder)
def generate_reel(folder):
    command=f''' ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
    subprocess.run(command, shell=True, check=True)
    print("working 2",folder)

if __name__=="__main__":
    with open("handled.txt","r") as f:
        while True:
            print("processing")
            handled_folders=f.readlines()
            handled_folders=[f.strip() for f in handled_folders]
            folders=os.listdir("user_uploads")
            
            for folder in folders:
                if(not(folder  in handled_folders)):
                    with open(f"user_uploads/{folder}/prompt.txt") as f:
                                text=f.read()
                                print(text, folder)

                    text_to_audio(folder) #generate audio mp3 from prompt.txt
                    generate_reel(folder) #convert image and audio in the folder into a reel
                    with open("handled.txt","a") as f:
                        f.write(folder + "\n")