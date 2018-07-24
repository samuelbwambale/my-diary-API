from flask_script import Manager
from app import app
import unittest
manager = Manager(app)

@manager.command
def test():
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
