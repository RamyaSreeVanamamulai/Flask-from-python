# Flask-from-python
1.how i started learning flask
To get started, first download and install Python from the official website https://www.python.org. After installing Python, open Visual Studio Code (VS Code). Inside VS Code, you can open PowerShell by clicking on Terminal in the top menu and then selecting New Terminal – it usually opens PowerShell by default. In the PowerShell terminal, you can check if pip is installed by typing pip --version. Then, install Flask and virtualenv by running the following commands: pip install flask and pip install virtualenv. These tools help you build and run your Flask web applications in a separate environment. Once everything is installed, you’re ready to create your project and start building your Flask app!

2. Create a Virtual Environment
python -m venv env
3. Activate the Virtual Environment
Windows (PowerShell):
.\env\Scripts\Activate.ps1
Windows (Command Prompt):
.\env\Scripts\activate.bat
Mac/Linux:
source env/bin/activate
4. Install Dependencies
pip install flask
If you're using other libraries like Flask-SQLAlchemy, include them like this:
pip install flask flask-sqlalchemy


Make sure everything is installed.
