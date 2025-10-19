from flask import Flask, redirect, request, session, Blueprint, render_template
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

def get_db():
    #Selects an specific db
    conn = sqlite3.connect('blogDatabase.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS blogs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        date TEXT NOT NULL,
        body_text TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_blogs():
    conn = get_db()
    cursor = conn.cursor()
    blogs = cursor.execute('SELECT * FROM blogs ORDER BY id DESC').fetchall()
    conn.close()
    return blogs

def create_admin():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM users WHERE username = ?',
    ('Avatarknight25',))
    if not cursor.fetchone():
        cursor.execute('INSERT OR REPLACE INTO users (username, password) VALUES (?,?)',
        ('Avatarnight25', generate_password_hash('Aceitunita')))
    conn.commit()
    conn.close()

def create_first_blog():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM blogs LIMIT 1')
    if not cursor.fetchone():
        cursor.execute('INSERT INTO blogs (title, date, body_text) VALUES (?,?,?)',
        ("Primer entrada en el blog de Eder", '18-10-2025', 'El proximo año ire a ver a Rush!!!'))
    conn.commit()
    conn.close()