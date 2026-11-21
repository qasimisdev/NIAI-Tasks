# Task 42 - pandas installation / getting started
#
# install with:
#   pip install pandas
# or with anaconda:
#   conda install pandas
#
# this script checks that it's installed and working.

try:
    import pandas as pd
except ImportError:
    print("pandas is not installed. run:  pip install pandas")
    raise SystemExit

print("pandas is installed, version", pd.__version__)

# tiny test to see it really works
mydataset = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2],
}
myvar = pd.DataFrame(mydataset)
print(myvar)

# numpy is installed with pandas
import numpy as np
print("numpy version", np.__version__)
