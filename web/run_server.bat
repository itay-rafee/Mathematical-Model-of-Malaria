set FLASK_ENV=development
cd %cd%
start Scripts\activate
set FLASK_APP=server.py
start http://127.0.0.1:5000/
flask run