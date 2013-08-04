import random

class Posicao:
	x = y = proporcao = valor = 0

	def __init__(self, x, y, proporcao, valor):
		self.x = x
		self.y = y
		self.valor = valor
		self.proporcao = proporcao


class MinasEncantadas:
	terreno = busca = dimensoes = []

	def __init__(self, altura, largura, valor_minimo, valor_maximo):
		self.dimensoes = [altura, largura]
		self.terreno = [[random.randint(valor_minimo, valor_maximo) for x in xrange(altura)] for x in xrange(largura)]


	def exibe(self):
		for x in self.terreno:
			mstr = ""
			for y in x:
				mstr += "%d\t" % y
			print mstr


	def processa(self, proporcao):
		mstr = ""
		maior = elemento = 0
		for x in xrange(0, self.dimensoes[0] - proporcao + 1):
			for y in xrange(0, self.dimensoes[1] - proporcao + 1):
				valor = self.soma(x, y, proporcao)
				if valor > maior:
					maior = valor
					elemento = Posicao(x, y, proporcao, valor)
				print ": %d ---\n\n" % valor
		self.busca.append(elemento)
		print mstr


	def soma(self, ix, iy, proporcao):
		mstr = ""
		soma = 0
		for x in range(ix, ix + proporcao):
			for y in range(iy, iy + proporcao):
				mstr += "%d\t" % self.terreno[x][y]
				soma += self.terreno[x][y]
			mstr += "\n"
		print mstr
		return soma


mina = MinasEncantadas(10, 10, -5, 5)
mina.exibe()
mina.processa(4)

for melhor in mina.busca:
	print melhor.valor