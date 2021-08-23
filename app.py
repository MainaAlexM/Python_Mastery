from flask import Flask
import autocv

app = Flask(__name__)

@app.route('/')
def hellow():
    return "hellow Maina"

if __name__ == "__main__":
    app.run(debug = True)
   