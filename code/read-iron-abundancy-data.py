#!/usr/bin/env python

import numpy as np
import matplotlib
import matplotlib.image

filename     = "../data/Vesta/iron/GRD_IRON_CORRECTED_COUNTS_MAP.TAB"
filename_out = "../data/Vesta/iron//vesta-iron-abundancy.png"

data = np.loadtxt(filename)
grid = np.zeros((2*180,2*360),dtype=np.float64)

minval = np.min(data[:,7])
maxval = np.max(data[:,7])

for i in range(len(data)):
    ymin = int((data[i][1] + 90) * 2)
    ymax = int((data[i][2] + 90) * 2)
    xmin = int(((data[i][4] + 360) % 360) * 2)
    xmax = int(((data[i][5] + 360) % 360) * 2)
    dx   = int(data[i][6] * 2)
    val  = (data[i][7] - minval)/(maxval - minval)
    #
    for y in range(ymin, ymax):
        for x in range(xmin, xmin+dx):
            grid[360-y-1][x%720] = val

matplotlib.image.imsave(filename_out, grid, cmap='gray')
# plt.imshow(grid)
# plt.show()
