from config import secret_key, key_postdb, key_userdb
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required,\
    logout_user
from datetime import datetime

app = Flask(__name__)
# pgAdmin4 db
# app.config['SQLALCHEMY_DATABASE_URI'] = \
#     key_userdb
app.config['SQLALCHEMY_DATABASE_URI'] = key_postdb
app.config['SQLALCHEMY_BINDS'] = {'users': 'sqlite:///users.db'}
app.config['SECRET_KEY'] = secret_key
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class Post(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Post --{self.title}-- with ID --{self.id} created on --' \
               f'{self.created}--'


class User(UserMixin, db.Model):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(10), nullable=False, unique=True)
    user_pass = db.Column(db.String(16), nullable=False)

    def __repr__(self):
        return f'User ID: {self.id} Username: {self.user_email} UserPW:' \
               f' {self.user_pass}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


all_projects = [
    {
        'title': 'Baby Weight Collector',
        'languages': ['HTML', 'CSS', 'JS', 'jQuery', 'Python', 'Flask',
                      'SQLAlchemy'],
        'description': 'Small webapp that takes guesses and provides an avg.'
                       ' guess and table of guesses.',
        'github': "https://github.com/8BitJustin/baby_weight_collector"
    },
    {
        'title': 'Blogging Site',
        'languages': ['HTML', 'CSS', 'Bootstrap', 'JS', 'Python', 'Flask',
                      'SQLAlchemy'],
        'description': 'Website that displays blog entries that are '
                       'created/altered by designated user.',
        'github': "https://github.com/8BitJustin/personal-blog-website"
    }
]


@app.route('/')
def index():
    all_posts = Post.query.order_by(Post.created.desc()).all()
    return render_template('index.html', posts=all_posts,
                           projects=all_projects)


@app.route('/blog')
def blog():
    all_posts = Post.query.order_by(Post.created.desc()).all()
    return render_template('blog.html', posts=all_posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        user = User.query.all()[0]
        if username == user.user_email and password == user.user_pass:
            login_user(user)
            return redirect(url_for('create'))
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        new_post = Post(title=post_title, content=post_content)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/create')
    else:
        all_posts = Post.query.order_by(Post.created.desc()).all()
        return render_template('create.html', posts=all_posts)


# start edit route here
@app.route('/create/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/create')
    else:
        return render_template('edit.html', post=post)


@app.route('/create/delete/<int:id>')
@login_required
def delete(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/create')


if __name__ == "__main__":
    app.run(debug=True)
