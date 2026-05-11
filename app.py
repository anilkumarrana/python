from flask import flask , render_template
import flask
app = flask(__name__)

@app.route("/")

def home ():
    name = "Anil sunaina"
    return render_template("new_notes.html", name = name)

if __name__ == "__main__":
    app.run(debug = True)