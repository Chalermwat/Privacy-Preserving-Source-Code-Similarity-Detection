from flask import Flask, request, render_template
import ssdeep

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
    score = ssdeep.compare(hash1,hash2)

    return f'Score: {str(score)}'

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)