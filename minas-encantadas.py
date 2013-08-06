import random

class Posicao:
	x, y, proporcao, valor = 0, 0, 0, 0

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
		maior = elemento = 0
		if type(proporcao) == int:
			px, py = proporcao, proporcao
		elif type(proporcao) == list:
			px, py = proporcao[0], proporcao[1]
		else:
			print "o tipo de dado recebido por processa deve ser [lista] ou inteiro"
			return False
		for x in xrange(0, self.dimensoes[0] - px + 1):
			for y in xrange(0, self.dimensoes[1] - py + 1):
				valor = self.soma(x, y, proporcao)
				if valor > maior:
					maior = valor
					elemento = Posicao(x, y, [px, py], valor)
		if type(elemento) != int:
			self.busca.append(elemento)


	def soma(self, ix, iy, proporcao):
		soma = 0
		for x in range(ix, ix + proporcao[0]):
			for y in range(iy, iy + proporcao[1]):
				soma += self.terreno[x][y]
		return soma


class Teste:
	profiler = False

	def __init__(self, x, y, vmin, vmax):
		self.profiler = [x, y, vmin, vmax]

		mina = MinasEncantadas(x, y, vmin, vmax)
		mina.exibe()

		for px in xrange(2, mina.dimensoes[0] / 2):
			for py in xrange(2, mina.dimensoes[1] / 2):
				mina.processa([px, py])

		ideal = Posicao(0, 0, [0, 0], 0)

		for melhor in mina.busca:
			if type(melhor) == int:
				print "melhor is integer %d" % melhor
			if type(ideal.valor) != int:
				print "ideal valor is not integer %d" % melhor.valor
			if melhor.valor > ideal.valor:
				ideal = melhor
			print "O melhor valor para matrizes de %dx%d foi %d nas coordenadas x, y (%d, %d)." % (melhor.proporcao[0], melhor.proporcao[1], melhor.valor, melhor.x, melhor.y)

		print "O valor ideal para matrizes de %dx%d foi %d nas coordenadas x, y (%d, %d)." % (ideal.proporcao[0], ideal.proporcao[1], ideal.valor, ideal.x, ideal.y)

Teste(30, 30, -50, 50)