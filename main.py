from flask import Flask, render_template
import os 
from blog.app import blog_bp

app = Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(blog_bp, static_folder='/static')

@app.route('/')
def home():
    return render_template('indexHome.html')

app.run(host='0.0.0.0', port=5000)