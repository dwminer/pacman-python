import random
import time

class AI:
	Up, Right, Down, Left = range(4)

	def __init__(self, player, ghosts, game, fruit, level):
		self.player = player
		self.ghosts = ghosts
		self.game = game
		self.fruit = fruit
		self.level = level

	def next_move(self):
		val = int(time.time()) % 4
		print(self.player.x)
		if val < 1:
			return self.Up
		elif val < 2:
			return self.Right
		elif val < 3:
			return self.Down
		else:
			return self.Left
