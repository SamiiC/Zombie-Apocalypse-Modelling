import numpy as np
import matplotlib.pyplot as plt

P = 0   #birthrate
d = 0.009 #natural death percent (per day)
B = 0.002 #transmission percent (per day)
G = 0.020 #resurect percent (per day)
A = 0.001 #destroy percent (per day)

#initial conditions

survivors0 = 500  #initial population
zombies0 = 0 #initial zombie population
removed0 = 1 #initial deth population


time_step = 0.02
t = np.arange(0.0,30.0,time_step) #time grid


no_steps = len(t)
survivors = np.zeros(no_steps)
zombies = np.zeros(no_steps)
removed = np.zeros(no_steps)
survivors[0] = survivors0
zombies[0] = zombies0
removed[0] = removed0
for i in range(0,no_steps-1):
  survivors[i+1] = survivors[i]+ time_step * (P - B*survivors[i]*zombies[i] - d*survivors[i])

  zombies[i+1] = zombies[i] + time_step*(B*survivors[i]*zombies[i]+G*removed[i] - A*survivors[i]*zombies[i])
  removed[i+1] = removed[i]+time_step*(d*survivors[i]+A*survivors[i]*zombies[i] - G*removed[i])


plt.plot(t,survivors,label = 'Living') #blue line
plt.plot(t,zombies,label = 'Zombies') #green line
plt.legend()
plt.xlabel('Days from outbreak')
plt.ylabel('Population')
plt.title('Zombie Apocalypse')
plt.show()
