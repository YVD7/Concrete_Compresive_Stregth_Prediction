import sys
from flask import Flask
from Main.logger import logging
from Main.exception import MainException


app=Flask(__name__)

@app.route("/",methods=["GET","POSt"])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        Main = MainException(e,sys)
        logging.info(Main.error_message)
        logging.info("We are testing logging module")

    return "CI CD pipeline has established."



if __name__=="__main__":
    app.run(debug=True)