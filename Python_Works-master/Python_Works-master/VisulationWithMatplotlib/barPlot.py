import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.array([1,2,3,4,5,6,7])
y = x*2+5
z = np.array(["Turkey","Usa","Germany","Poland","Mexico","China","England"])

plt.bar(z,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
