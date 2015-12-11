import numpy as np
import matplotlib.pyplot as plt
import cmath
import csv

from matplotlib import rc
from pylab import *
from scipy.optimize import fsolve
from mpl_toolkits.axes_grid.axislines import SubplotZero

import matplotlib.cm as cm
from matplotlib.colors import LogNorm




def xclip_data(data, clip_length):
	clipped_data =\
	 copy(data[int(clip_length/2.0): -int(clip_length/2.0), :])

	return clipped_data

def shift_1d_data(data):
	shifted_data = copy(data)
	min_data = data[0]
	for i in range(0, len(data)):
		if (data[i] < min_data):
			min_data = data[i]

	for i in range(0, len(data)):
		shifted_data[i] = (shifted_data[i] - min_data)

	return shifted_data

def normalize_1d_data(data):
	normalized_data = copy(data)
	norm_factor = 0

	for i in range(0, len(data)):
		norm_factor = norm_factor + data[i]
	norm_factor = norm_factor/len(data)
	for i in range(0, len(data)):
		normalized_data[i] = normalized_data[i]/abs(norm_factor)

	return normalized_data