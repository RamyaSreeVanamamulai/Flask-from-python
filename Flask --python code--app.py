You can create a simple app.py file to test your setup with a basic route:
open a file in that and name app.py 
//code

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True)
Save this and run:
python app.py


It  shows some run file go Open your browser and go to http://127.0.0.1:5000 — you should see "Hello, world!"

🎉 That’s it!
This is how I started learning Flask — from downloading Python to building and running my first app. 
It may seem like a lot at first, but once you set up your environment, building apps becomes super smooth and fun!
