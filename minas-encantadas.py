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
		maior = elemento = 0
		if type(proporcao) == 'int':
			px, py = proporcao, proporcao
		else:
			px, py = proporcao[0], proporcao[1]
		for x in xrange(0, self.dimensoes[0] - px + 1):
			for y in xrange(0, self.dimensoes[1] - py + 1):
				valor = self.soma(x, y, proporcao)
				if valor > maior:
					maior = valor
					elemento = Posicao(x, y, [px, py], valor)
		self.busca.append(elemento)


	def soma(self, ix, iy, proporcao):
		soma = 0
		for x in range(ix, ix + proporcao[0]):
			for y in range(iy, iy + proporcao[1]):
				soma += self.terreno[x][y]
		return soma


mina = MinasEncantadas(10, 10, -50, 50)
mina.exibe()

for px in xrange(2, 9):
	for py in xrange(2, 9):
		mina.processa([px, py])

ideal = Posicao(0, 0, [0, 0], 0)

for melhor in mina.busca:
	if melhor.valor > ideal.valor:
		ideal = melhor
	print "O melhor valor para matrizes de %dx%d foi %d nas coordenadas x, y (%d, %d)." % (melhor.proporcao[0], melhor.proporcao[1], melhor.valor, melhor.x, melhor.y)

print "O valor ideal para matrizes de %dx%d foi %d nas coordenadas x, y (%d, %d)." % (ideal.proporcao[0], ideal.proporcao[1], ideal.valor, ideal.x, ideal.y)
