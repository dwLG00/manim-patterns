from manim import *

class BMatrix(Matrix):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, left_bracket="[", right_bracket="]", **kwargs)

class PMatrix(Matrix):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, left_bracket="(", right_bracket=")", **kwargs)
