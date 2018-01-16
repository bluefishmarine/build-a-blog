from flask import Flask, request, redirect, render_template, session,flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:werto5678@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = "sjfh576b929%&#fj"


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(2000))


    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/blog', methods = ['GET'])
def blog():
    if request.args:
        id = int(request.args.get("id"))   
        blog = Blog.query.filter_by(id = id).first()
        print (blog)
        return render_template("article.html", blog=blog)

    blogs = Blog.query.all()
    return render_template('blogs.html',blogs = blogs)

@app.route("/new", methods=['GET','POST'])
def new_post():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        post = Blog(title,body)
        db.session.add(post)
        db.session.commit()
        id = post.id    
        return redirect("/blog?id={0}".format(id))

    return render_template('new.html')

if __name__ == '__main__':
    app.run()