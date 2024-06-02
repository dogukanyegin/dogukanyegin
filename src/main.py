import os
import dbm

from flask import Flask, send_file,render_template,request
import qrcode
from sqlalchemy import sql
# Suggested code may be subject to a license. Learn more: ~LicenseLog:4287395123.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:2309587331.
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
