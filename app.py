from crypt import methods
from flask import Flask
from importlib_metadata import method_cache

app=Flask(__name__)

@app.route("/",methods=["GET","POSt"])
def index():
    return "Starting Machine Learning Project"


if __name__=="__main__":
    app.run(debug=True)