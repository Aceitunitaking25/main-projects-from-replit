from flask import Flask, redirect, request, session, Blueprint, render_template
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from .db_management import init_db, create_admin, create_first_blog, get_blogs, get_db
from .session_and_blog import login, post_blog, show_blog_HTML

blog_bp = Blueprint(
'blog', __name__,
static_folder='static', 
template_folder='templates'
)

init_db()
create_admin()
create_first_blog()

blog_bp.add_url_rule('/login',view_func=login,methods=['POST', 'GET'])

@blog_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')

blog_bp.add_url_rule('/post_blog',view_func=post_blog, methods=['POST','GET'])

@blog_bp.route('/blog', methods=['GET'])
def index():
    blogs_html = show_blog_HTML()
    return render_template('indexBlog.html', blogs_html=blogs_html)