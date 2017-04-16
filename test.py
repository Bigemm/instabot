from instabot import User, api
import logging.config
import unittest


test_login, test_password = 'instabotproject', 'drcherryisagoodman'

class TestUser(unittest.TestCase):

    def test_user(self):
        user = User(test_login, test_password)
        print(api.get_user_followers(user, user.id))

if __name__ == '__main__':
    logging.config.fileConfig('instabot/log.conf')
    log = logging.getLogger('main')
    unittest.main()