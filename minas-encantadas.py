import random

class Posicao:
	x = y = proporcao = valor = 0

	def __init__(self, x, y, proporcao, valor):
		self.x = x
		self.y = y
		self.valor = valor
		self.proporcao = proporcao


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
		proporcao = 3
		mstr = ""
		x = 0
		while x + proporcao < self.dimensoes[0]:
			y = 0
			while y + proporcao < self.dimensoes[1]:
				self.soma(x, y, proporcao)
				y += 1
			mstr += "\n"
			x += 1
		print mstr


	def soma(self, ix, iy, proporcao):
		mstr = ""
		soma = 0
		for x in range(ix, ix + proporcao):
			for y in range(iy, iy + proporcao):
				mstr += "%d\t" % self.terreno[x][y]
				soma += self.terreno[x][y]
			mstr += "\n"
		self.busca.append(Posicao(x, y, proporcao, soma))
		print '----------------------------------------------------'
		print mstr
		print '-------------------------------------------- %d' % soma


mina = MinasEncantadas(10, 10, -5, 5)
mina.exibe()
mina.processa()

for i in xrange(5):
	print mina.busca[i].valor