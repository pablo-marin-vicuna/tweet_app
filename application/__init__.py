from flask import Flask

app = Flask(__name__) #initialize

from application import routes

if __name__ == '__main__':
    app.run()
    