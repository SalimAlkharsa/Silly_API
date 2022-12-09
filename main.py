from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Chat GPT just accessed the Net'

if __name__ == '__main__':
    app.run()
