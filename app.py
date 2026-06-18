from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
  return "demi project for pear-lite company deploy sucessfully "
app.run(host= '0.0.0.0', port=5000)

