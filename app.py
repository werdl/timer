from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/timer/<int:seconds>')
def timer(seconds):
    return render_template('timer.html', seconds=seconds)

if __name__ == '__main__':
    app.run(debug=True)