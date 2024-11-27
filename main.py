import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import video_to_text
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_video():
	# print(request.files['file'].read())
	
	if 'file' not in request.files:
		flash('No file part')
		return redirect('transcription.html', filename=filename)
	file = request.files['file']
	if file.filename == '':
		flash('No video selected for uploading')
		return redirect('transcription.html' , filename=filename)
	else:
		#print('upload_video filename: ' + filename)
		#flash('Video successfully uploaded and displayed below')
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		print(filename)
		value123=video_to_text.video_to_text(filename)
		summary_content = video_to_text.summarization()
		return render_template('transcription.html', filename=filename, value=value123, summary=summary_content)

@app.route('/display/<filename>')
def display_video(filename):
	#print('display_video filename: ' + filename)
	return redirect(url_for('transcription.html', filename='uploads/' + filename), code=301)

@app.route('/transcription')
def sample_func():
    
    return render_template('transcription.html')

@app.route('/transcription.html')
def func_transcription():
    
    video_file_name = "abc.mp4"
    value123 = video_to_text.video_to_text(video_file_name)
    print(value123)
    return render_template('transcription.html', value=value123)

@app.route('/summary.html')
def func_summary():
    return render_template('summary.html')

if __name__ == "__main__":
    app.run()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    