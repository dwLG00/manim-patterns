from manim import *

# Helper functions for setting colors of things and whatnot

def set_color(li: list, color: list, animate=False):
	'''Set color of each object in li to corresponding color in color. If animate is set to True, instead return a list of animations.'''

	if animate:
		animations = []
		for i, obj in enumerate(li):
			animations.append(obj.animate.set_color(color[i]))
		return animations
	for i, obj in enumerate(li):
		obj.set_color(color[i])



def line_graph_color_rg(points: list, lines: list, red=RED, green=GREEN, animate=False):
	'''Color line segments in a line graph based on whether they are increasing or decreasing. Requires sorted set of points. If animate is set to True, instead return a list of animations.'''
	# Abstracted from finmetrics-manim

	assert len(points) == len(lines) + 1
	if animate:
		animations = []
		for i, line in enumerate(lines):
			if points[i+1][1] - points[i][1] > 0: # line slope is positive
				animations.append(line.animate.set_color(green))
			elif points[i+1][1] - points[i][1] < 0: # line slope is negative
				animations.append(line.animate.set_color(red))
		return animations
	for i, line in enumerate(lines):
		if points[i+1][1] - points[i][1] > 0: # line slope is positive
			line.set_color(green)
		elif points[i+1][1] - points[i][1] < 0: # line slope is negative
			line.set_color(red)
