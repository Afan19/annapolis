from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/art')
def art():
    s = "This is anna's art: "
    s += "here is the art:"
    return s

@app.route('/')
def homepage():
	return render_template("index.html")

@app.route('/tech')
def tech():
    s = "This is anna's tech stuff"
    s += "here is the stuff:"
    return s

if __name__ == '__main__':
    app.run()
