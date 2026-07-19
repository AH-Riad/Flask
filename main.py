from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    name = request.args.get('q')
    subject = request.args.get('sub')
    
    return render_template("index.html", name = name, sub = subject)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/handle-login", methods=["GET","POST"])
def handle_login():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        return f"Welcome {name}!"
    else:
        return render_template("login.html")  
    








if __name__ == '__main__':
    app.run(debug=True)