from flask import Flask, request, render_template
import tlsh

app = Flask(__name__)

HOST = "127.0.0.1"
PORT = "3000"

@app.route('/')
def hello():
    return render_template('index.html')

@app.post('/compare')
def CompareHash():
    hash1 = request.form['hash1']
    hash2 = request.form['hash2']
    try:
        # score = tlsh.diff(hash1,hash2)
        score = tlsh.diffxlen(hash1,hash2)
    except:
        return render_template('index.html',score="Invalid Hash")

    return render_template('index.html',score=str(score))

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)