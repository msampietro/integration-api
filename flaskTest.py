from flask import Flask
app = Flask(__name__)

@app.route("/newClient")    #For POST method add - methods=['POST'] -
def hello():
    return "Client Created"


@app.route("/postForm")    #For POST method add - methods=['POST'] -
def instapageForm():
    return "Form inserted on Odoo"


if __name__ == "__main__":
    app.run()