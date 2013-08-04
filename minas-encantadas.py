import random

class MinasEncantadas:
	terreno = []

	def __init__(self, altura, largura, valor_minimo, valor_maximo):
		while altura > 0:
			altura -= 1
			temporario = []
			y = largura
			while y > 0:
				y -= 1
				temporario.append(random.randint(valor_minimo, valor_maximo))

			self.terreno.append(temporario);

	def exibe(self):
		for x in self.terreno:
			mstr = ""
			for y in x:
				mstr += "%d\t" % y
			print mstr

mina = MinasEncantadas(10, 10, -5, 5)
mina.exibe()