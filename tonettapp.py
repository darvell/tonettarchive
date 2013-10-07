from flask import Flask
from database_models import shared

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///777.db"
shared.init_db(app)

@app.route('/')
def render_index():
    return '777'

@app.before_first_request
def get_ready():
    shared.db.create_all() # Should only do something if the tables have never been made.


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()