# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:27:23 2022

@author: Juan A. BENCOSME
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
from collections import OrderedDict
from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
from matplotlib import lines
from matplotlib.patches import Rectangle
from matplotlib.transforms import Bbox

linestyles_dict = OrderedDict(
    [('solid',               (0, ())),
     ('loosely dotted',      (0, (1, 10))),
     ('dotted',              (0, (1, 5))),
     ('densely dotted',      (0, (1, 1))),

     ('loosely dashed',      (0, (5, 10))),
     ('dashed',              (0, (5, 5))),
     ('densely dashed',      (0, (5, 1))),

     ('loosely dashdotted',  (0, (3, 10, 1, 10))),
     ('dashdotted',          (0, (3, 5, 1, 5))),
     ('densely dashdotted',  (0, (3, 1, 1, 1))),

     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))])

data = pd.read_excel ("pva_tga_data.xlsx",sheet_name = "1")

x1 = data["TEMP"]
y1 = data["MASA"]
x2 = data["TEMP-1"]
y2 = data["MASA-1"]
x3 = data["TEMP-2"]
y3 = data["MASA-2"]
x4 = data["TEMP-3"]
y4 = data["MASA-3"]
x5 = data["TEMP-4"]
y5 = data["MASA-4"]
# y3 = data["D"]

fig = plt.figure (figsize = (8,8)); 

fig, ax1 = plt.subplots();

line1 = ax1. plot(x1,y1, color = 'black', label = 'PVA', linestyle=linestyles_dict['solid'])

line2 = ax1. plot(x2,y2, color = 'blue', label = 'PVA-LI10', linestyle='dashdot')

line3 = ax1. plot(x3,y3, color = 'green', label = 'PVA-LI20', linestyle=linestyles_dict['solid'])

line4 = ax1. plot(x4,y4, color = 'orange', label = 'PVA-LI30', linestyle=linestyles_dict['solid'])

line5 = ax1. plot(x5,y5, color = 'red', label = 'PVA-LI40', linestyle=linestyles_dict['solid'])
# ax2 = ax1.twinx()
# line2 = ax2.plot(x1,y2, color = 'crimson', label = '$1^{er}$ Dérivée...', linestyle='--') 



# Inset figure of low-temperature fit, located by data coordinates in ax1.
bb_data_ax2 = Bbox.from_bounds(0.125, 0.13, 0.53, 0.53)
disp_coords = ax1.transData.transform(bb_data_ax2)
fig_coords_ax2 = fig.transFigure.inverted().transform(disp_coords)
bb_ax2 = Bbox(fig_coords_ax2)
ax2 = fig.add_axes(bb_ax2)


# The data: only display for low temperature in the inset figure.
Ymax =max(y1) + 25

ax2.plot(x1[x1<Ymax], y1[x1<Ymax],linestyle=linestyles_dict['solid'], c='black', mew=2, alpha=0.8,
         label='Experiment')


ax2.plot(x2[x2<=Ymax], y2[x2<=Ymax],linestyle='dashdot', c='blue', mew=1, alpha=0.8,
          label='Experiment')


ax2.plot(x3[x3<=Ymax], y3[x3<=Ymax],linestyle=linestyles_dict['solid'], c='green', mew=1, alpha=0.8,
           label='Experiment')

ax2.plot(x4[x4<=Ymax], y4[x4<=Ymax],linestyle=linestyles_dict['solid'], c='orange', mew=1, alpha=0.8,
           label='Experiment')


ax2.plot(x5[x5<=Ymax], y5[x5<=Ymax],linestyle=linestyles_dict['solid'], c='red', mew=1, alpha=0.8,
          label='Experiment')



#Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax1, [0.135,0.11,0.52,0.52])
ax2.set_axes_locator(ip)


# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
mark_inset(ax1, ax2, loc1=2, loc2=1, fc="none", ec='0.55')



ax1.tick_params(axis = 'y', labelcolor='black')



ax1.set_ylabel (' Masse (%)', color = 'black')


ax1.set_xlabel("Température (°C)")

lines = line1 + line2 + line3 + line4 + line5

labels = [l.get_label() for l in lines]
ax1.legend(lines,labels, loc='best', fontsize=8, shadow=0);

# plt.savefig('GRAFICA SOUTENANCE .svg', bbox_inches='tight', dpi=2600)
plt.show()

# ax3.plot(x1,y3, color = color2, label = 'Strain1', marker = 4, markersize = 8, linestyle='-.')
# offset = 0


# 	best
# 	upper right
# 	upper left
# 	lower left
# 	lower right
# 	right
# 	center left
# 	center right
# 	lower center
# 	upper center
# 	center


# # ax1.legend(loc='best')

# ax1.set_xlabel ('Linear')




# host = host_subplot(111, axes_class=AA.Axes)
# plt.subplots_adjust(top=1.0, right=0.85)

# par1 = host.twinx()
# par2 = host.twinx()
# # par3 = host.twinx()

# offset = -25
# new_fixed_axis = par2.get_grid_helper().new_fixed_axis
# par2.axis["left"] = new_fixed_axis(loc="left",
#                                     axes=par2,
#                                     offset=(offset, 0))

# # offset = 0
# # new_fixed_axis = par1.get_grid_helper().new_fixed_axis
# # par1.axis["left"] = new_fixed_axis(loc="left",
# #                                     axes=par1,
# #                                     offset=(offset, 0))

# # offset = 0
# # new_fixed_axis = par3.get_grid_helper().new_fixed_axis
# # par3.axis["left"] = new_fixed_axis(loc="right",
# #                                     axes=par3,
# #                                     offset=(offset, 0))
# par1.axis["left"].toggle(all=True)
# # par2.axis["left"].toggle(all=True)
# host.set_xlim(0, 45)
# #
# # offset = -35
# # new_fixed_axis = par1.get_grid_helper().new_fixed_axis
# # par1.axis["left"] = new_fixed_axis(loc="left",
# #                                     axes=par1,
# #                                     offset=(offset, 0))


# # host.set_xlabel("Fraction Liquide-Ethane")
# # host.set_ylabel("Temperature (K)")
# # par1.set_ylabel("Fraction Vapeur-Ethane")
# # par2.set_ylabel("Fraction")


# # # par3.axis["left"].toggle(all=True)

# p1, = par1.plot(x1,y1,'b',label='Liquide',markersize = 10)
# p2, =par2.plot(x1,y3,'g',label='Liquide',markersize = 10)
# # p3, = par3.plot(x1,y3,'y--',label='Liquide',markersize = 10)
# # p3, = plt.plot(x1,y3,'y--',label='Liquide',markersize = 10)
# # par1.axis["right"].label.set_color(p1.get_color())
# # par2.axis["left"].label.set_color(p2.get_color())
