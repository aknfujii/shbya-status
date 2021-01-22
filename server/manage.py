from flask_script import Manager, Command

from app import app, db

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command("init_db", InitDB())
    manager.run()
