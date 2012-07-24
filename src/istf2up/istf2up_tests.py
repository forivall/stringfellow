import application as isup
import unittest

class IsupTestCase(unittest.TestCase):
    def setUp(self):
        isup.app.config['TESTING'] = True
        
        self.app = isup.app.test_client()
        
    def tearDown(self):
        pass
        
    #TODO: add tests when I add functionality

if __name__ == '__main__':
    unittest.main()
