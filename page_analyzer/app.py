import psycopg2
import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')
#print(DATABASE_URL)
conn = psycopg2.connect(DATABASE_URL)

@app.route('/')
def start_page():
    return render_template(
        'index.html'
    )
