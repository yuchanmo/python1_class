# import mod1

# mod1.sum(1,2)



# import sys

# dir(sys.path)


# sys.path.append('C:/Yuchan/Python')


# from gam



from game.sound import *

echo.echo_test()
wav.echo_test()

import numpy as np
import matplotlib.pyplot as plt

mu,sigma = 2,0.5

v = np.random.normal(mu,sigma,10000)

plt.hist(v,bins=50,normed = 1)
plt.show()



import os
os.path.dirname('c:\python')