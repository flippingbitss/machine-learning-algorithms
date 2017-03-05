import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# LINK = 'http://vincentarelbundock.github.io/Rdatasets/csv/datasets/AirPassengers.csv'

# response = urllib.request.urlopen(LINK)
# data = response.read()      # a `bytes` object
# text = data.decode('utf-8')
df= pd.read_csv("insurance.csv")



# df.set_index("X", inplace= True)
x=np.array(df["X"])
y=df["Y"]

x1 = np.stack((np.ones(len(x)),x), axis=1)
w=(np.linalg.inv(np.transpose(x1).dot(x1))).dot(np.transpose(x1)).dot(y)
abline_values = [w[1] * i + w[0] for i in x]
plt.scatter(x, y)
plt.plot(x, abline_values)
plt.scatter([40], [w[1] * 40 + w[0]])
plt.show()
