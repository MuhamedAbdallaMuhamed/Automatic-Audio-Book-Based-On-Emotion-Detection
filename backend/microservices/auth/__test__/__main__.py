import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))

if __name__ == '__main__':
    from __test__ import *
    unittest.main()
