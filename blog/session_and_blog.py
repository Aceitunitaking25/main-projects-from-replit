from flask import Flask, redirect, request, session, Blueprint, render_template
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from .db_management import init_db, create_admin, create_first_blog, get_blogs, get_db

def login():
    #This works when the user go to /login
    #If the method IS NOT "GET", the code ignores this block
    if request.method=="GET":
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')

    #Checking if the username and pass provided are the admin ones
    conn = get_db()
    cursor = conn.cursor()
    user = cursor.execute(
            'SELECT 1 FROM users WHERE username = ?',
            (username,)).fetchone()
    #Checking if the user privided the right pass for admin
    if user and check_password_hash(user['password'], password):
        session['username'] = username
        session['password'] = password
        return redirect('/post_blog')
    else:
        return '<h2>Credenciales invalidass</h2>'

def post_blog():
    if 'username' not in session:
        redirect('/login')
    if request.method == 'GET':
        blogs_html = show_blog_HTML()
        return render_template('postblog.html', blogs = blogs_html)
    #This code works if the method is POST
    title = reques.form.get('title')
    date = request.form.get('date')
    body_text = request.form.get('body_text')

    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO blogs(title, date, body_text) VALUES (?,?,?)',
            (title, date, body_text))
        conn.commit()
        conn.close()
    except Exception:
        return 'Error al registrar entrada al blog'
    return redirect('/post_blog')

def show_blog_HTML():
    blogs = get_blogs()
    #Getting all the blogs in dictionary form to present it now in 
    # a pretty HTML format
    blogs_html = ''
    for blog in blogs:
        blogs_html += f"""
    <div class="blog-post">
        <h2 class="blogTitle">{blog['title']}</h2>
        <p class="date">{blog['date']}</p>
        <p class="bodyText">{blog['body_text']}</p>
    </div>"""
    return blogs_html