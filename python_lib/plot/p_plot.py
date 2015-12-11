import matplotlib.pyplot as plt
from matplotlib import rc

import matplotlib.cm as cm
from matplotlib.colors import LogNorm

from mpl_toolkits.axes_grid.axislines import SubplotZero


red_color = (238.0/255.0, 75.0/255.0, 62.0/255.0)
blue_color = (0.0/255.0, 172.0/255.0, 233.0/255.0)
green_color = (31.0/255.0, 218.0/255.0, 154.0/255.0)
black_color = (0, 0, 0)
yellow_color = (255.0/255.0, 255.0/255.0, 0)

sphere_280ps_color = red_color
rod_b1_color = blue_color
rod_b42_color = green_color

short_color = sphere_280ps_color
long_color = rod_b42_color

def plot_data(x, c = 'black_color'):
	fig = plt.figure()
	plot = plt.plot(x, color = c)
	fig.set_size_inches(5,5)
	plt.xlim(0, x.shape[0])
	plt.show()
	return

def plot_data_xy(x, y, c = 'black_color'):
	fig = plt.figure()
	plot = plt.plot(x, y, color = c)
	fig.set_size_inches(5,5)
	plt.show()
	return

def save_plot_data(x, file_name, save = True):
	fig = plt.figure()
	c = black_color
	plot = plt.plot(x, color = c)
	plt.xlim(0, len(x))
	if save == True:
		plt.savefig(file_name, figsize = (10,10), dpi = 160, bbox_inches = 'tight')
	else:
		plt.show()
	return

def save_plot_two_data(x, y, file_name, save = True):
	fig = plt.figure()
	plot1 = plt.plot(x, color = sphere_280ps_color)
	plot2 = plt.plot(y, color = rod_b1_color)
	if save == True:
		plt.savefig(file_name, figsize = (10,10), dpi = 160, bbox_inches = 'tight')
	else:
		plt.show()
	return

def plot_two_data(x, y):
	fig = plt.figure()
	plot1 = plt.plot(x, color = red_color)
	plot2 = plt.plot(y, color = blue_color)
	plt.show()
	return

def save_plot_data_xy(x, y, file_name, c = 'black_color', save = True):
	fig = plt.figure()
	plot = plt.plot(x, y, color = c)
	if save == True:
		plt.savefig(file_name, figsize = (10,10), dpi = 160, bbox_inches = 'tight')
	else:
		plt.show()
	return

def plot_matrix(matrix):
	fig = plt.figure()
	plt.imshow(matrix, cmap = plt.cm.gray, interpolation = 'none')
	plt.show()
	return
 
def plot_matrix_line(matrix, line):
	fig = plt.figure()
	plt.imshow(matrix, cmap = plt.cm.gray, interpolation = 'none')
	x = []
	y = []
	for i in range(0, len(line)):
		x.append((line[i])[0])
		y.append(line[i][1])

	plt.plot(y[:], x[:], color = yellow_color, lw = 3)
	plt.ylim(matrix.shape[0], 0)
	plt.xlim(0, matrix.shape[1])
	plt.show()
	return

def save_plot_matrix(matrix, file_name, save = True):
	fig = plt.figure()
	plt.imshow(matrix, cmap = cm.hot, norm = LogNorm())
 	

	if save == True:
		plt.savefig(file_name, figsize = (10,10), dpi = 160, bbox_inches = 'tight')
	else:
		plt.show()
	return
 
def save_plot_matrix_line(matrix, line, file_name, save = True):
	fig = plt.figure()
	
	x = []
	y = []


	for i in range(0, len(line)):
		x.append(line[i][0])
		y.append(line[i][1])

	plt.plot(y[:], x[:], color = yellow_color, ls = '--', lw = 3)
 	
	plt.imshow(matrix, cmap = cm.hot, norm = LogNorm())

	if save == True:
		plt.savefig(file_name, figsize = (10,10), dpi = 160, bbox_inches = 'tight')
	else:
		plt.show()
	return

