from node import Node
class Rack:
	def __init__(self):
		"""
		Klasse for representasjon av rack i en regneklynge
		Oppretter et rack der det senerer kan plasseres noder
		"""
		self._noder = []  # liste med alle noder i rack objekt


	def settInn(self, node):
		"""
		Plasserer en ny node inn i racket.
		Bruker parameter node (som er noden som skal plasseres inn)
		"""
		self._noder.append(node)

	def getAntNoder(self):
		"""
		Henter og returnerer antall noder i racket
		"""
		return len(self._noder)

	def antProsessorer(self):
		"""
		Beregner og returnerer sammenlagt antall prosessorer i nodene i et rack
		"""
		antallPros = 0 # antall prosessorer i den rack
		for node in self._noder:  # loopen for alle noder i node liste
			antallPros += node.antProsessorer()  # antall Prosessorer i hvernode legges til antallPros varaiabel
		return antallPros


	def noderMedNokMinne(self, paakrevdMinne):
		"""
		Beregner antall noder i racket med minne over gitt grense
		Tar parameter paakrevdMinne (som er antall GB minne som kreves)
		Returnerer antall noder med tilstrekkelig minne
		"""
		antallNod = 0     # antall noder med nok krevende minne
		# loopen for alle noder i liste av alle noder
		for node in self._noder:
			if node.nokMinne(paakrevdMinne):   # if nokMinne returnerer True
				antallNod += 1              # antall noder med nok krevende minne oker med 1
		return antallNod
