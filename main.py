from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

# This is where you create a Flask application instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "oh_you_found_the_key?_ohwell_gg!"  # Set a secret key for the app (used for session management and CSRF protection)
app.config['UPLOAD_FOLDER'] = 'static/files'  # Directory to save uploaded files

# AES KEY
AES_KEY = b"this is my key NOT yours lil boy"# my AES key

class UploadFileForm(FlaskForm):
    # Define a file upload field in the form
    file = FileField(f"File", validators=[InputRequired()])
    submit = SubmitField("Upload a File")

# Define routes for the root URL ("/") and "/home"
@app.route("/", methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        # Ensure the upload folder exists
        upload_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'])
        os.makedirs(upload_folder, exist_ok=True)
        file.save(os.path.join(upload_folder, secure_filename(file.filename)))
        return render_template("encrypt.html", form=form)
    return render_template('index.html', form=form)

# Run the app only if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5000)
