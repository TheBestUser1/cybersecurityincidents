from Test_Connex import *
from Test_Parser import *
from Test_main  import *

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.realpath(__file__))
sys.path.append(PARENT_DIR)

import unittest


if __name__ == "__main__":
    unittest.main()