import LACDA_Core_Function_FINAL as LACDA
import math
import scipy.stats
import xlrd

class Hour_Analysis:
	count = [0, 0, 0, 0, 0, 0, 0, 0]

	def __init__(self, LACDA_Core):
		self.LACDA_Core = LACDA_Core

	def Interval(self):
		interval = {'02': {'like': [], 'share': [], 'comment': [], 'reach': []},
					'35': {'like': [], 'share': [], 'comment': [], 'reach': []},
					'68': {'like': [], 'share': [], 'comment': [], 'reach': []},
					'911': {'like': [], 'share': [], 'comment': [], 'reach': []},
					'1214': {'like': [], 'share': [], 'comment': [], 'reach': []},
					'1517': {'like': [], 'share': [], 'comment': [], 'reach': []},
					'1820': {'like': [], 'share': [], 'comment': [], 'reach': []},
					'2123': {'like': [], 'share': [], 'comment': [], 'reach': []}}
		sheet = self.LACDA_Core.main_sheet
		time_index = self.LACDA_Core.get_col_index("Posted", sheet)
		link_index = self.LACDA_Core.get_col_index("Permalink", sheet)		

		for index in range(2, sheet.nrows):
			year, month, day, hour, minute, second = (xlrd.xldate_as_tuple(sheet.cell(index, time_index).value, self.LACDA_Core.file.datemode))			
			if hour >= 0 and hour <= 2:
				interval['02']['like'].append(self.LACDA_Core.get_like(sheet.cell(index, link_index).value))
				interval['02']['share'].append(self.LACDA_Core.get_share(sheet.cell(index, link_index).value))
				interval['02']['comment'].append(self.LACDA_Core.get_comment(sheet.cell(index, link_index).value))
				interval['02']['reach'].append(self.LACDA_Core.get_reach(sheet.cell(index, link_index).value))
				self.count[0] += 1
			elif hour >= 3 and hour <= 5:
				interval['35']['like'].append(self.LACDA_Core.get_like(sheet.cell(index, link_index).value))
				interval['35']['share'].append(self.LACDA_Core.get_share(sheet.cell(index, link_index).value))
				interval['35']['comment'].append(self.LACDA_Core.get_comment(sheet.cell(index, link_index).value))
				interval['35']['reach'].append(self.LACDA_Core.get_reach(sheet.cell(index, link_index).value))
				self.count[1] += 1
			elif hour >= 6 and hour <= 8:
				interval['68']['like'].append(self.LACDA_Core.get_like(sheet.cell(index, link_index).value))
				interval['68']['share'].append(self.LACDA_Core.get_share(sheet.cell(index, link_index).value))
				interval['68']['comment'].append(self.LACDA_Core.get_comment(sheet.cell(index, link_index).value))
				interval['68']['reach'].append(self.LACDA_Core.get_reach(sheet.cell(index, link_index).value))
				self.count[2] += 1
			elif hour >= 9 and hour <= 11:
				interval['911']['like'].append(self.LACDA_Core.get_like(sheet.cell(index, link_index).value))
				interval['911']['share'].append(self.LACDA_Core.get_share(sheet.cell(index, link_index).value))
				interval['911']['comment'].append(self.LACDA_Core.get_comment(sheet.cell(index, link_index).value))
				interval['911']['reach'].append(self.LACDA_Core.get_reach(sheet.cell(index, link_index).value))
				self.count[3] += 1
			elif hour >= 12 and hour <= 14:
				interval['1214']['like'].append(self.LACDA_Core.get_like(sheet.cell(index, link_index).value))
				interval['1214']['share'].append(self.LACDA_Core.get_share(sheet.cell(index, link_index).value))
				interval['1214']['comment'].append(self.LACDA_Core.get_comment(sheet.cell(index, link_index).value))
				interval['1214']['reach'].append(self.LACDA_Core.get_reach(sheet.cell(index, link_index).value))
				self.count[4] += 1		
			elif hour >= 15 and hour <= 17:
				interval['1517']['like'].append(self.LACDA_Core.get_like(sheet.cell(index, link_index).value))
				interval['1517']['share'].append(self.LACDA_Core.get_share(sheet.cell(index, link_index).value))
				interval['1517']['comment'].append(self.LACDA_Core.get_comment(sheet.cell(index, link_index).value))
				interval['1517']['reach'].append(self.LACDA_Core.get_reach(sheet.cell(index, link_index).value))
				self.count[5] += 1
			elif hour >= 18 and hour <= 20:
				interval['1820']['like'].append(self.LACDA_Core.get_like(sheet.cell(index, link_index).value))
				interval['1820']['share'].append(self.LACDA_Core.get_share(sheet.cell(index, link_index).value))
				interval['1820']['comment'].append(self.LACDA_Core.get_comment(sheet.cell(index, link_index).value))
				interval['1820']['reach'].append(self.LACDA_Core.get_reach(sheet.cell(index, link_index).value))
				self.count[6] += 1						
			elif hour >= 21 and hour <= 23:
				interval['2123']['like'].append(self.LACDA_Core.get_like(sheet.cell(index, link_index).value))
				interval['2123']['share'].append(self.LACDA_Core.get_share(sheet.cell(index, link_index).value))
				interval['2123']['comment'].append(self.LACDA_Core.get_comment(sheet.cell(index, link_index).value))
				interval['2123']['reach'].append(self.LACDA_Core.get_reach(sheet.cell(index, link_index).value))
				self.count[7] += 1

		return interval

	# Code for the merge subroutine

	def merge(self, a, b):
		'''Function to merge two arrays '''
		c = []
		while len(a) != 0 and len(b) != 0:
			if a[0] < b[0]:
				c.append(a[0])
				a.remove(a[0])
			else:
				c.append(b[0])
				b.remove(b[0])
		if len(a) == 0:
			c += b
		else:
			c += a
		return c

	# Code for merge sort

	def mergesort(self, x):
		""" Function to sort an array using merge sort algorithm """
		if len(x) == 0 or len(x) == 1:
			return x
		else:
			middle = int(len(x)/2)
			a = self.mergesort(x[:middle])
			b = self.mergesort(x[middle:])
		return self.merge(a,b)

	def mean (self, array):
		s = 0
		for i in range(len(array)):
			s += array[i]
		return s/len(array)

	def std_dev (self, array):
		s = 0
		m = self.mean(array)
		for i in range(len(array)):
			s += (array[i] - m)*(array[i] - m)
		return round(math.sqrt(s/len(array)), 5)

	def z_score (self, x, array):
		return (x - self.mean(array))/self.std_dev(array)

	def norm_prob_less (self, x, array):
		return round(scipy.stats.norm(loc = self.mean(array), scale = self.std_dev(array)).cdf(x), 5)

	def norm_prob_greater (self, x, array):
		return round(1 - scipy.stats.norm(loc = self.mean(array), scale = self.std_dev(array)).cdf(x), 5)

	def norm_prob_between (self, x, y, array):
		return round(scipy.stats.norm(loc = self.mean(array), scale = self.std_dev(array)).cdf(y) - scipy.stats.norm(loc = self.mean(array), scale = self.std_dev(array)).cdf(x), 5)

	def highest_value(self, array):
		self.mergesort(array)
		return array[len(array) - 1]

	def highest_time_like(self):
		temp = []
		for item in self.Interval():
			temp.append(self.highest_value(item['like']))

