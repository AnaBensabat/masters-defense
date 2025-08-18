import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['xtick.major.pad']='10'
plt.rcParams['ytick.major.pad']='10'
plt.rcParams['xtick.minor.pad']='10'
plt.rcParams['ytick.minor.pad']='10'
plt.rc('xtick', labelsize=15)    # fontsize of the tick labels

plt.rcParams["axes.linewidth"]='2.5'
plt.rcParams["axes.titlepad"]='10'
plt.rcParams["axes.labelpad"]='10'
plt.rcParams['ytick.major.width']='1.5'
plt.rcParams['xtick.major.width']='1.5'
plt.rcParams['ytick.major.size']='8'
plt.rcParams['xtick.major.size']='8'
plt.rcParams['ytick.minor.width']='1.5'
plt.rcParams['xtick.minor.width']='1.5'
plt.rcParams['ytick.minor.size']='6'
plt.rcParams['xtick.minor.size']='6'

color = "#00552280"
xs = np.linspace(-.5,1.5,10000)
ys = 0.25*(xs**2)*((1-xs)**2)

fig, axs = plt.subplots(1,figsize=(2,1.75))
plt.plot(xs,ys,color=color)
plt.ylim(0,0.15)
plt.tick_params(axis="x",direction="in")#, pad=-15)
#axs.set_xticklabels([0,0.5,1])
axs.tick_params(axis="y",left=False,top=False,labelleft=False)
axs.tick_params(axis="x",direction="in")#, pad=-15)
plt.savefig("double-well.pdf")
plt.tight_layout()
plt.savefig("/home/bensabat/University/Mestrado/Defense/media/double-well.svg")
