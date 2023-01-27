from flask import Flask, render_template,send_from_directory, request

import os

app = Flask(__name__,template_folder='templates')
print(app.template_folder)

# Checking if the template folder exist 
if not os.path.isdir(app.template_folder):
    print(f"{app.template_folder} does not exist.")

@app.route('/')
def index():
    template_file = 'index.html'
    # Checking if the template file exist
    if not os.path.isfile(os.path.join(app.template_folder, template_file)):
        print(f"{template_file} does not exist in {app.template_folder}.")
    return render_template(template_file)
