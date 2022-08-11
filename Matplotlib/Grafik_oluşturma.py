import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
"""
x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x,y,"o--g") # -g düz yeşil çizgi --g kesikli çizgi #o noktalı
plt.axis([0,6,0,20]) # 6 x ekseni genişliği 20 y ekseni genişliği
plt.title("Grafik Başlığı")
plt.xlable("X lable")
plt.ylable("Y lable")
"""
"""
x = np.linspace(0,2,100)
plt.plot(x,x, label ="linear",color = "red")
plt.plot(x,x**2, label ="quadratic", color ="yellow")
plt.plot(x,x, label ="cubic", color= "green")

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("simple plot")
plt.legend() # sol üst köşede veriler yazar
plt.show()
"""
"""
x = np.linspace(0,2,100)
fig,axs = plt.subplots(3)

axs[0].plot(x,x, color = "red")
axs[0].set_title("linear")
axs[1].plot(x,x**2, color = "black")
axs[1].set_title("quadratic")
axs[2].plot(x,x**3, color = "grey")
axs[2].set_title("cubic")
plt.tight_layout()
plt.show()
"""
"""
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2)
fig.suptitle("grafik başlığı")
axs[0,0].plot(x,x, color = "red")
axs[0,1].plot(x,x**2, color = "blue")
axs[1,0].plot(x,x**3, color = "yellow")
axs[1,1].plot(x,x**4, color = "green")
"""
df = pd.read_csv("Players.csv")
df = df.drop(["birth_city"], axis = 1).groupby("Player").mean()
df.plot(subplots=True)
plt.legend()
plt.show()