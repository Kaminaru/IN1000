class Node:
	def __init__(self, minne, antPros):
		'''
		Klasse for representasjon av noder i en regnelynge
		Oppretter en node med gitt minne-storrelse og antall prosessorer
		'''
		self._minne = minne    # GB
		self._antPros = antPros # antall prossessorer

	def antProsessorer(self):
		"""
		Henter og returnerer antall prosessorer i noden
		"""
		return self._antPros

	def nokMinne(self, paakrevdMinne):
		"""
		Sjekker om nok minne for et program
		Tar paakrevdMinne som er GB minne som kreves for programmet
		Returnerer True hvis noden har misnt saaa mye minne
		"""
		# Hvis paakrevendeMinne er mindre eller lik av den bestemt node saa returneres True.
		if paakrevdMinne <= self._minne:
			return True
		return False
