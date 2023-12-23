from flask import Flask, render_template, redirect
import time

app = Flask(__name__)

@app.route('/<int:seconds>')
def timer(seconds):
    return render_template('timer.html', seconds=seconds)

@app.route('/<int:minutes>:<int:seconds>')
def mtimer(minutes, seconds):
    return render_template('timer.html', seconds=(minutes * 60 ) + seconds)

@app.route('/<int:hours>:<int:minutes>:<int:seconds>')
def htimer(hours, minutes, seconds):
    return render_template('timer.html', seconds=(hours * 3600) + (minutes * 60 ) + seconds)

@app.route('/')
def home():
    return redirect('/1:00')