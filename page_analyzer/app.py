from flask import Flask
from dotenv import load_dotenv

load_dotenv()
__all__ = ['app']
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to Flask!'
