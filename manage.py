from thermos import app, db
from thermos.models import User, Bookmark, Tag
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def insert_data():
    adi = User(username="adi", email="adi@gmail.com", password="1234")
    db.session.add(adi)

    def add_bookmark(url, description, tags):
        db.session.add(Bookmark(url=url, description=description, user=adi, tags=tags))

    for name in ["python", "flask", "webdev", "programming"]:
        db.session.add(Tag(name=name))

    db.session.commit()

    add_bookmark("http://www.google.com", "Google", "python, flask, webdev")

    sri = User(username="sri", email="sri@gmail.com", password="1234")
    db.session.add(sri)
    db.session.commit()
    print("Initialized the database")
    

if __name__ == '__main__':
    manager.run()