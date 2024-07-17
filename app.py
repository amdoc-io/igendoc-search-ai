from flask import Flask
from api import register_all_apis

app = Flask(__name__)
register_all_apis(app=app)

if __name__ == "__main__":
    app.run(debug=True)
