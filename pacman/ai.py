import random

class AI:
	Up, Right, Down, Left = range(4)

	def __init__(self, player, ghosts, game, fruit, level):
		self.player = player
		self.ghosts = ghosts
		self.game = game
		self.fruit = fruit
		self.level = level

	def next_move(self):
		return random.choice((self.Up, self.Up, self.Down, self.Left, self.Left, self.Right))
