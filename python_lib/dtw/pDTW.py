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



def get_distance_DTW(a_i, b_i):
	distance_ = ((a_i - b_i)**2.0)**0.5
	return distance_

def get_distance_DDTW(a, i, b, j):
	#a,b are 1-D numpy arrays
	#i, j are indices of elements we want distance between

	if i == a.shape[0]-1:
		d_a = (a[i]-a[i-1]+(a[0]-a[i-1]/2.0)/2.0)
	else:
		d_a = (a[i] - a[i-1] + (a[i+1] - a[i-1])/2.0)/2.0

	if j == b.shape[0]-1:
		d_b = (b[j] - b[j-1]+(b[0] - b[j-1]/2.0)/2.0)
	else:
		d_b = (b[j] - b[j-1] + (b[j+1] - b[j-1])/2.0)/2.0

	distance_ = ((d_a - d_b)**2.0)**0.5
	return distance_

def get_distance_matrix_DTW(a, b):
	distance_matrix_ = np.zeros((len(a), len(b)))
	for i in range(0, distance_matrix_.shape[0]):
		for j in range(0, distance_matrix_.shape[1]):
			distance_matrix_[i,j] = get_distance_DTW(a[i], b[j])

	return distance_matrix_

def get_distance_matrix_DDTW(a, b):
	distance_matrix_ = np.zeros(a.shape[0], b.shape[0])
	for i in range(0, distance_matrix_.shape[0]):
		for j in range(0, distance_matrix_.shape[1]):
			distance_matrix_[i,j] = get_distance_DDTW(a, i, b, j)

	return distance_matrix_

def get_cost_matrix(distance_matrix_, h_wt_ = 1, v_wt_ = 1, d_wt_ = 1):
	infinity = 2.0**32.0
	cost_matrix_ = infinity*np.zeros((distance_matrix_.shape[0], distance_matrix_.shape[1]))

	for i in range(0, cost_matrix_.shape[0]):
		for j in range(0, cost_matrix_.shape[1]):
			if i == 0 and j == 0:
				cost_matrix_[i,j] = distance_matrix_[i,j]
			else:
				if i == 0:
					cost_matrix_[i,j] = distance_matrix_[i,j] + v_wt_*cost_matrix_[i,j-1]
				elif j == 0:
					cost_matrix_[i,j] = distance_matrix_[i,j] + h_wt_*cost_matrix_[i-1,j]

				else: cost_matrix_[i,j] = min(h_wt_*distance_matrix_[i,j] + cost_matrix_[i-1,j],\
					v_wt_*distance_matrix_[i,j] + cost_matrix_[i,j-1],\
					d_wt_*distance_matrix_[i,j] + cost_matrix_[i-1,j-1])

	return cost_matrix_

def get_warp_path(cost_matrix_):
	warp_path = np.zeros((0,2))

	warp_path.append((cost_matrix_.shape[0] - 1, cost_matrix_.shape[1]-1))

	i = warp_path[0,0]
	j = warp_path[0,1]

	while(i > 0 or j > 0):
		if i == 0:
			j = j - 1
		elif j == 0:
			i = i - 1

		else:
			if min(cost_matrix_[i-1, j], cost_matrix_[i-1, j-1], cost_matrix_[i,j-1]) == cost_matrix_[i-1, j]:
				i = i - 1
			elif min(cost_matrix_[i-1, j], cost_matrix_[i-1, j-1], cost_matrix_[i, j-1]) == cost_matrix_[i-1, j-1]:
				i = i - 1
				j = j - 1
			elif min(cost_matrix_[i-1, j], cost_matrix_[i-1, j-1], cost_matrix_[i,j-1]) == cost_matrix_[i, j-1]:
				j = j - 1

		warp_path = np.append(warp_path, [[i,j]], axis = 0)

	return warp_path
	
def get_cost_path(matrix_, path_):
	cost_path_ = np.zeros((0,1))
	for i in range(0, path_.shape[0]):
		cost_path_ = np.append(cost_path_, matrix[path[i,0], path[i,1]], axis = 0)

	return cost_path
