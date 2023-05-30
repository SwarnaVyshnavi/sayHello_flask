from flask import Flask,render_template,flash,request

app=Flask(__name__)
app.secret_key="3e243r"

@app.route('/hello')
def index():
    flash("Whats your name???")
    return render_template("index.html")
# if __name__==__main__:
#     app.run()
@app.route('/greet',methods=['POST','GET'])
def greet():
    flash("Hi     "+str(request.form['name_input'])+"!"+"      Great to see you!!")
    
    return render_template("index.html")