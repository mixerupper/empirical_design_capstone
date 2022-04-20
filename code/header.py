import numpy as np
from datetime import datetime

class Header():
	def __init__(self, sample):
		self.sample = sample

	def data_root(self, path):
		return '../../data/'+path

	def raw_root(self, path):
		if self.sample:
			return self.data_root('01a-sample-raw/' + path)
		else:
			return self.data_root('01b-full-raw/' + path)		

	def clean_root(self, path, sample = True):
		if self.sample:
			return self.data_root('02a-sample-clean/' + path)
		else:
			return self.data_root('02b-full-clean/' + path)

	def sample_raw_root(self, path):
		return self.data_root('01a-sample-raw/' + path)

	def sample_clean_root(self, path, sample = True):
		return self.data_root('02a-sample-clean/' + path)
		
	def full_raw_root(self, path):
		return self.data_root('01b-full-raw/' + path)		

	def full_clean_root(self, path, sample = True):
		return self.data_root('02b-full-clean/' + path)

	def results_root(self, path):
		return self.data_root('03-results/' + path)