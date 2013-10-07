from flask.ext.sqlalchemy import SQLAlchemy
import os, sys

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

    # Force import all models that exist so they're all registered into the SQLAlchemy instance.
    # When I first wrote this I thought I was so clever. Still do.
    path = os.path.dirname(os.path.abspath(__file__))

    for py in [f[:-3] for f in os.listdir(path) if f.endswith('.py') and f != '__init__.py' and f != 'shared.py']:
        module = __import__('database_models.' + py)
        class_list = [getattr(module, x) for x in dir(module) if isinstance(getattr(module, x), type)]
        for cls in class_list:
            setattr(sys.modules[__name__], cls.__name__, cls)

    return db