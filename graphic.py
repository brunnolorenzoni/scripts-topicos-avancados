import matplotlib.pyplot as plt 
ax = plt.gca() 

gp = dataset.groupby("newCol_mes")["COD_IBGE"].count()
keys = gp.keys()

gp.plot(kind='bar',x=keys,y=gp) 

plt.show() 