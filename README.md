Flask-from-Python
How I Started Learning Flask
Learning Flask was one of the most exciting parts of my Python journey. It opened the door to building real web applications using just code and a browser. Here’s how I got started with Flask, step-by-step, using simple tools and commands.

1. How I Got Started with Flask
To begin, the very first thing I did was download Python from the official website:
👉 https://www.python.org

Once Python was installed on my computer, I opened Visual Studio Code (VS Code), which is a great editor for writing Python code. To open the terminal in VS Code:

Go to the top menu,

Click Terminal → New Terminal
This usually opens PowerShell by default (especially on Windows).

Next, I checked whether pip (Python’s package manager) was already installed by typing:
pip --version
Then, I installed the tools I needed to get started:
pip install flask
pip install virtualenv
These tools help you build and run your Flask web apps inside a separate environment, which keeps everything clean and organized.

2. Create a Virtual Environment
After installing the tools, I created a virtual environment to manage all the project dependencies separately:
python -m venv env
3. Activate the Virtual Environment
Depending on your operating system, the activation command is slightly different:

👉 On Windows (PowerShell):
.\env\Scripts\Activate.ps1
👉 On Windows (Command Prompt):
.\env\Scripts\activate.bat
👉 On Mac/Linux:
source env/bin/activate
After this, you’ll see the environment name (env) appear in your terminal — this means the virtual environment is active.

4. Install Flask and Other Dependencies
With the virtual environment active, I installed Flask again — this time inside the environment:
pip install flask
If you plan to use a database with your app, you can install Flask-SQLAlchemy as well:
pip install flask flask-sqlalchemy
To make sure everything installed correctly, I ran:
pip list
This showed a list of all installed packages like Flask, Jinja2, Werkzeug, etc.

Now that everything is installed, you're ready to build your Flask project!
