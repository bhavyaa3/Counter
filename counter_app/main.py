
from flask import Flask, render_template
from replit import db

app = Flask(__name__)

if 'number'  not in db:
  db['number'] =0
#HTML and CSS


#database = {'number':0}
 
@app.route('/')
#/ means home page
def home():
  #return show(page=home_page , number=db['number'])
  #return my_home_page
  return render_template('index.html', number = db['number']) 
  #we have given a path as argument
  
@app.route('/increment')
def increment():
  #increament a number
  db['number']+=1
  return render_template('index.html', number = db['number']) 
  
@app.route('/decrement')
def decrement():
   db['number']-=1
   
   return render_template('index.html', number = db['number']) 
   
app.run(host='0.0.0.0', port=81)
