# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 14:54:55 2022

@author: Sam
"""

import matplotlib.pyplot as plt
import math
import numpy as np
#sediment flow parameters
q0=0.22; a=1.1; 
#bed shape parameters
b=0.2; k=2.0; eps=0.5; #bed porosity not given so I'll assume 0.5
#space domain
xdelta=0.1;
start=0.0; end=4.0;
x=np.arange(start, end+xdelta,xdelta)
#time domain
tdelta=[0.05,0.1,0.15]
#clear figures
plt.cla(); plt.clf();
#setup
n=[];
plt.style.use("dark_background");
fig, ax= plt.subplots(figsize=[4.8, 3.6],dpi=300);
# initial conditions plot
n.append(b*np.sin(k*x));
ax.plot(x,n[0],label="t=0");
# different time delta plots
for i in range(len(tdelta)):
    n.append( b*np.sin(k*x)-tdelta[i]*(a*b*k/eps)*np.cos(k*x) );
    ax.plot(x,n[i+1],label="$\Delta t=$"+str(tdelta[i]));
# style of the plot
ax.set_xlabel("location (m)");
ax.set_ylabel("bed elevation (m)");
ax.legend();
ax.grid(True);
plt.show();
#now with a plot of the flow on top
plt.style.use("default");
fig2, ax2= plt.subplots(figsize=[4.8, 3.6],dpi=300);
ax2.plot(x,n[0],label="$\eta (x)$",zorder=0);
y_dummy=x*0;
q=q0+a*n[0];
ax2.quiver(x,n[0],q,y_dummy,zorder=1);

# style of the plot
ax2.set_xlabel("location (m)");
ax2.set_ylabel("bed elevation (m)");
ax2.set_title("flux $q_s$ on surface");
ax2.legend();
ax2.grid(True);
plt.show();