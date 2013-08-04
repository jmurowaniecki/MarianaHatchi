import random

class MinasEncantadas:
	terreno = busca = []
	dimensoes = []

	def __init__(self, altura, largura, valor_minimo, valor_maximo):
		self.dimensoes = [altura, largura]
		self.terreno = [[random.randint(valor_minimo, valor_maximo) for x in xrange(altura)] for x in xrange(largura)]


	def exibe(self):
		for x in self.terreno:

			mstr = ""

			for y in x:
				mstr += "%d\t" % y

			print mstr


	def processa(self):
		tam_x = tam_y = 3

		mstr = ""

		x = 0

		while x + tam_x < self.dimensoes[0]:

			y = 0

			while y + tam_y < self.dimensoes[1]:

				self.soma([x, y], [x + tam_x, y + tam_y])

				y += 1

			mstr += "\n"

			x += 1

		print mstr


	def soma(self, de, ate):
		mstr = ""
		soma = 0
		for x in range(de[0], ate[0]):
			for y in range(de[1], ate[1]):
				mstr += "%d\t" % self.terreno[x][y]
				soma += self.terreno[x][y]
			mstr += "\n"
		print '----------------------------------------------------'
		print mstr
		print '-------------------------------------------- %d' % soma

mina = MinasEncantadas(10, 10, -5, 5)
mina.exibe()
mina.processa()