from flask import *  
   
app = Flask(__name__)  
  
@app.route('/admin')  
def admin():  
    return 'admin'  
  
@app.route('/librarion')  
def librarion():  
    return 'librarion'  
  
@app.route('/student')  
def student():  
    return 'student'  
  
@app.route('/user/<name>')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))  
    if name == 'librarion':  
        return redirect(url_for('librarion'))  
    if name == 'student':  
        return redirect(url_for('student'))  
if __name__ =='__main__':  
    app.run(debug = True)  


# from flask import Flask  
  
# app = Flask(__name__) #creating the Flask class object   
 
# @app.route('/') #decorator drfines the   
# def home():  
#     return "hello, this is our first flask website";  
  
# if __name__ =='__main__':  
#     app.run(debug = True)  
    
    
# from flask import Flask  
# app = Flask(__name__)  
 
# @app.route('/home')  
# def home():  
#     return "hello, welcome to our website";  
  
# if __name__ =="__main__":  
#     app.run(debug = True)  