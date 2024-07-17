from flask import Flask
from api import register_all_apis
from middleware import middleware

app = Flask(__name__)
app.before_request(middleware)
register_all_apis(app=app)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
