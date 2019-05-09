import matplotlib.pyplot as plt;
import pandas as pd

url="iris.csv"
stupac= ['D velike', 'Š velike', 'D male', 'Š male', 'Vrsta']
podatci=pd.read_csv8url,names=stupac)

print(podatci)
print(podatci.head(5))
print(podatci.shape)

'''
iris-setosa-1
iris-versicolor-2
iris-virginica-3
'''

plt.scatter(podatci.values[:,2],podatci.values[:,0],c=podatci.values[:,4])
plt.ylabel('Džina velike latice');
plt.xlabel('Dužina male latice');

plt.show();
