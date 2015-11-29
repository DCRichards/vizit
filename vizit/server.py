from flask import Flask
import os

# note that we need to ensure static_folder is set or Flask
# will look for dir 'static'
app = Flask(__name__, static_url_path='', static_folder='web')

@app.route('/')
def root():
    return app.send_static_file('index.html')

def start():
    app.run()