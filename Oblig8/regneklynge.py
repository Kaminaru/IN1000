from node import Node
from rack import Rack
# Klasse for representasjon av regneklynge med racks og noder
class Regneklynge:
	def __init__(self, filnavn):
		"""
		Oppretter tom regneklynge for racks
		Leser data om regneklynge fra fil, bygger datastrukturen
		Tar parameter filnavn, som er navn til fil med data for regneklyngen
		"""
		self._listeRacs = [] # liste med alle racks objekter i regneklynge objekt
		# Her appender jeg rack objekt, for aa lage den forste rack objekt
		# Det hjelper aa lage looper videre, som sjekker om det er nok plass i rack liste.
		self._listeRacs.append(Rack())
		fil = open(filnavn)
		# For loopemn som gaar gjennom alle linjer i fil
		self._noderPerRack = int(fil.readline())
		for linje in fil:
			biter = linje.strip().split()  # liste med alle deler i linje
			# loopen som gaar gjennom antall noder (biter[0] for antall noder)
			for i in range(int(biter[0])):
				# node objekt lik Node(minne, prosessorer)  - biter[1],biter[2] tok jeg fra liste som ble lagt tidligere
				node = Node(int(biter[1]),int(biter[2]))
				self.settInnNode(node)  # bruker metode settInnNode som jobber med de node objektene videre


	def settInnNode(self, node):
		"""
		Plasserer en node inn i et rack med ledig plass, eller i et nytt
		Tar parameter node som er referanse til noden som skal settes inn i datastrukturen
		"""
		# hvis siste index(rack objekt) har liste som har ikke plass.
		#(Den kaller paa metode for rack getAntNoder som sjekker hvor mange noder er i rack)
		# Og hvis den lik grense til hvor mange noder det er per Rack. Saa lages det ny rack objekt
		# Som har ny liste for noder. Deretter velger den igjen siste objekt i listeRack (dvs. den nyeste
		# objekt med tumt liste) Og legger til node

		# Men hvis siste rack objekt i _listeRack har plass i sin liste med noder
		# saa settes node objekt i den rack objekt liste
		if self._listeRacs[-1].getAntNoder() == self._noderPerRack:
			self._listeRacs.append(Rack())
			self._listeRacs[-1].settInn(node)
		elif self._listeRacs[-1].getAntNoder() < self._noderPerRack:
			self._listeRacs[-1].settInn(node)

	def antProsessorer(self):
		"""
		Beregner og returnerer totalt antall prosessorer i hele regnelyngen
		"""
		antPro = 0   # antall prosessorer i helle regneklynge
		for racks in self._listeRacs:  # loopen for alle racks i rackliste
			antPro += racks.antProsessorer() # legger til andtall prosessorer som antProsessorer metode returnerer
		return antPro

	def noderMedNokMinne(self, paakrevdMinne):
		"""
		Beregner antall noder i regneklynge med minne over angitt grense
		Tar parameter paakrevdMinne - hvor mye minne skal noder som telles med ha
		Returnerer antall noder med tilstrekkellig minne
		"""
		antallNod = 0   # antall noder i regneklynge med nok minne
		for racks in self._listeRacs: # loopen for alle racks i rackliste
			antallNod += racks.noderMedNokMinne(paakrevdMinne)
		return antallNod

	def antRacks(self):
		"""
		Henter og returnerer antall racks i regneklynge
		"""
		return len(self._listeRacs)
