from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def main():
    return "<center><h1>HOLA  ITE ensenada</h1></center><marquee>PAKO</marquee>"

##ENDPOINT
@app.route("/login/<user>/<passw>")
def adios(user,passw):
    return jsonify(saludo=f"bye bye {user}")

@app.route("/register")
def registro():
    return jsonify(saludo="Asi no se usa el bye tio joderrr")


@app.route("/saludo")
def saludo():
    return '{"value":"bye bye"}'

if __name__=='__main__':
    app.run()
#flask --app app run
