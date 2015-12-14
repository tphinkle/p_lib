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

import sys
sys.path.append('/home/preston/Desktop/Programming/datasci/p_lib/plot/')
import p_plot




def turn_cw(direction_):
	if direction_ == 'up':
		direction = 'right'

	elif direction_ == 'right':
		direction = 'down'

	elif direction_ == 'down':
		direction = 'left'

	elif direction_ == 'left':
		direction = 'up'

	return direction

def turn_ccw(direction_):
	if direction_ == 'up':
		direction = 'left'

	elif direction_ == 'left':
		direction = 'down'

	elif direction_ == 'down':
		direction = 'right'

	elif direction_ == 'right':
		direction = 'up'

	return direction

def get_cw_tile(direction_, tile_):
	if direction_ == 'up':
		tile = (tile_[0], tile_[1] + 1)
	elif direction_ == 'right':
		tile = (tile_[0] + 1, tile_[1])
	elif direction_ == 'down':
		tile = (tile_[0], tile_[1] - 1)
	elif direction_ == 'left':
		tile = (tile_[0] - 1, tile_[1])

	return tile

def get_bottom_left_tile_coords_bw(matrix_):
	for i in range(0, matrix_.shape[0]):
		for j in range(0, matrix_.shape[1]):
			if matrix_[matrix_.shape[0]-i-1,j] == 1:
				return (matrix_.shape[0]-i, j)

def walk_around_ccw(matrix_):
	try:
		current_direction = 'up'

		start_tile = get_bottom_left_tile_coords_bw(matrix_)
		current_tile = start_tile

		i = start_tile[0]
		j = start_tile[1]
		k = 0

		path = []
		path.append(start_tile)
		
		while (current_tile != start_tile or k == 0):
			k = k + 1
			cw_tile = get_cw_tile(current_direction, current_tile)
			
			

			if matrix_[cw_tile[0], cw_tile[1]] == 1:
				#print('00')
				current_direction = turn_cw(current_direction)
				continue
			
			if current_direction == 'up':
				if matrix_[current_tile[0]-1, current_tile[1]+1] == 1:
					#print('a_1')
					i = current_tile[0]
					j = current_tile[1] + 1
				else:
					#print('a_2')
					i = current_tile[0] - 1
					j = current_tile[1] + 1
					current_direction = turn_ccw(current_direction)

			elif current_direction == 'right':
				if matrix_[current_tile[0] + 1, current_tile[1] + 1] == 1:
					#print('b_1')
					i = current_tile[0] + 1
					j = current_tile[1]
				else:
					#print('b_2')
					i = current_tile[0] + 1
					j = current_tile[1] + 1
					current_direction = turn_ccw(current_direction)

			elif current_direction == 'down':
				if matrix_[current_tile[0] + 1, current_tile[1] - 1] == 1:
					#print('c_1')
					i = current_tile[0]
					j = current_tile[1] - 1
				else:
					#print('c_2')
					i = current_tile[0] + 1
					j = current_tile[1] - 1
					current_direction = turn_ccw(current_direction)

			elif current_direction == 'left':
				if matrix_[current_tile[0] - 1, current_tile[1] - 1] == 1:
					#print('d_1')
					i = current_tile[0] - 1
					j = current_tile[1]
				else:
					#print('d_2')
					i = current_tile[0] - 1
					j = current_tile[1] - 1
					current_direction = turn_ccw(current_direction)

			current_tile = (i,j)
			path.append(current_tile)
			
			
		#p_plot.plot_matrix_line(matrix_, path)
		return path

	except IndexError:
		return False

def convert_path_to_xseries(path_):
	xseries = []
	for i in range(0, len(path_)):
		xseries.append(path_[i][1])
	return xseries

def convert_path_to_yseries(path_):
	yseries = []
	for i in range(0, len(path_)):
		yseries.append(path_[i][0])
	return yseries