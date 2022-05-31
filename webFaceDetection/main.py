from flask import *  
import cv2
import numpy as np


app = Flask(__name__)  
 
@app.route('/')  
def message(): 
       #image = cv2.imread('C://Geeksforgeeks//image_processing//fruits.jpg')
  
      # cv2.imshow('Original Image', image)
      return render_template('index.html')  
if __name__ == '__main__':  
   app.run(debug = True)  