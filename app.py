from flask import Flask
app = Flask(_name_)
@app.route("/")
def home():
 return "<h1>Hello from CI/CD Pipeline - Version 1</h1>"
if _name_ == "_main_":
  app.run(host="0.0.0.0", port=5000)
