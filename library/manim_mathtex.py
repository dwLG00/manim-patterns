from manim import *

def mathtex(string) -> MathTex:
	'''Split string space-wise and return generated MathTex'''
	l = [x for x in string.split(' ') if x != '']
	return MathTex(*l)
