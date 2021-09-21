from app import create_app,db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User,Pitch,Comment,Downvote,Upvote

app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)
manager.add_command('server',Server(use_debugger=True))


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Comment = Comment, Upvote = Upvote, Downvote = Downvote,Pitch = Pitch)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()