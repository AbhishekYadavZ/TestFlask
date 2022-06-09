from flask import Flask
from flask import render_template
#create the object of Flask
app  = Flask(__name__)
 
 
 
#creating our routes
@app.route('/')
def Index():
    return render_template('index.html')
 
 
#run flask app
# if __name__ == "__main__":
#     app.run(debug=True)
# if __name__ == '__main__':
#       app.run(host='127.0.0.1', port=8000)

app.run(host='0.0.0.0', port=5000)