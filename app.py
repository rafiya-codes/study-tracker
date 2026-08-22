
from flask import Flask , render_template , request, redirect, url_for

app = Flask(__name__)

resources = []

@app.route('/')
def index():
    return render_template('index.html', resources=resources)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        subject = request.form["subject"]
        title = request.form["title"]
        link = request.form["link"]
        resources.append({
            "subject": subject,
            "title": title,
            "link": link
        })
        return redirect(url_for("index"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)