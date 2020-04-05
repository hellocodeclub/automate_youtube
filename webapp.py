from flask import Flask,render_template, request
from flask_bootstrap import Bootstrap
from download import download_audio

app=Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/download", methods=['POST'])
def download():
    video1_url = request.form['firstvideo']
    download_audio(video1_url)

    return render_template('index.html')


if __name__=='__main__':
    app.run(port=5000,debug=True)