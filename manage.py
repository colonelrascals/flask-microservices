from flask_script import Manager

from project import app, db
# created a new Manager instance to handle all of the manager commands from the command line.
manager = Manager(app)

@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    manager.run()
