from manim import *

# Library/file for cartesian graphs (2D, 3D, etc graphs, not in the graph theory sense)

def ez_scatter(x_range, y_range, points, plot_lines=False, dot_color=WHITE, line_color=WHITE, line_color_rg=False, rg_color_palette=(RED, GREEN)):
	'''Given graph axes and points, return scatterplot'''

	graph = Axes(x_range=x_range, y_range=y_range, tips=False)
	ax = graph.add_coordinates()
	points_sorted = sorted(points, key=lambda point: point[0]) #sort by x value
	dots = [
		Dot(ax.coords_to_point(*point), color=dot_color) for point in points_sorted
	]
	dots_group = VGroup(*dots)

	if plot_lines:
		if line_color_rg:
			red, green = rg_color_palette
			rg_color = lambda p1, p2: red if p1 > p2 else green if p1 < p2 else line_color
			lines = [
				Line(
					start=ax.coords_to_point(*points_sorted[i]),
					end=ax.coords_to_point(*points_sorted[i+1]),
					color=rg_color(points_sorted[i][1], points_sorted[i+1][1])
				) for i in range(len(points_sorted) - 1)
			]
		else:
			lines = [
				Line(start=ax.coords_to_point(*points_sorted[i]), end=ax.coords_to_point(*points_sorted[i+1]), color=line_color) for i in range(len(points_sorted) - 1)
			]
		lines_group = VGroup(*lines)
		return VGroup(graph, dots_group, lines_group)
	else:
		return VGroup(graph, dots_group)
