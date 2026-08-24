
from flask import Flask , render_template , request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///resources.db"
db = SQLAlchemy(app)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    subject = db.Column(db.String(100), nullable= False )
    title = db.Column(db.String(200), nullable = False)
    link = db.Column(db.String(500), nullable = False) 

@app.route('/')
def index():
    resources = Resource.query.all()
    return render_template('index.html', resources=resources)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        subject = request.form["subject"]
        title = request.form["title"]
        link = request.form["link"]
        new_resource = Resource(subject=subject, title=title, link=link)
        db.session.add(new_resource)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)