import unittest
from app import app

class FlaskTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(clas):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()

        self.app.testing = True
        pass
    
    def tearDown(self):
        pass

    def testHome(self):
        log = self.app.get('/')
        self.assertEqual(log.status_code, 200)


    

if __name__ == '__main__':
    unittest.main()
