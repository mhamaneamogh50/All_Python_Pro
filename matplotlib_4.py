import matplotlib.pyplot as plt
a=[2,4,6,8]
n=['amogh','vivek','raj','pranav']
v=[0,0,0.1,0]
plt.pie(a,labels=n,shadow=True,explode=v)
plt.show()
