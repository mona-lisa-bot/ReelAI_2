from flask import Flask, render_template, request, flash, redirect, url_for
import uuid #it creates unique string for each time user inputs, 
# the user input is then stored in a folder with the unique string name.
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET","POST"])
def create():
    meid=uuid.uuid1()
    if request.method == "POST":
        print(request.files.keys())
        upload_id =request.form.get("uuid")
        prompt= (request.form.get("text"))
        input_files=[]
        for key, value in request.files.items():
            print(key,value)#key:filenumber, value:file name 
            #uploading the file 
            file=request.files[key]
            
            if file :
                filename = secure_filename(file.filename)
                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], upload_id)))):
                     os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], upload_id))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], upload_id,filename))
                input_files.append(filename)
                print(file.filename)

                #also save the text in the same folder
                with open(os.path.join(app.config['UPLOAD_FOLDER'], upload_id,"prompt.txt"),"w") as f:
                    f.write(prompt)

            for f1 in input_files:
                with open(os.path.join(app.config['UPLOAD_FOLDER'], upload_id,"input.txt"),"a") as f:
                    f.write(f"file '{f1}'\nduration 1\n")

                
    

    return render_template("create.html", meid=meid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

app.run(debug=True)