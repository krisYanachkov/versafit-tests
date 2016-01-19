from base import *
import os, sys

class Add_News(VFTestCase):
	
	@logged_in('club')
	def test_add_news(self):
		
		self.e_wait('.sub-nav li:nth-of-type(5)')
		
		self.e('.sub-nav li:nth-of-type(5)').click()
		sleep(1)
		
		self.e('[name="title"]').send_keys('BMW')
		self.e('[name="text"]').send_keys('Svetofarna gonka. Toi vkarva bmw-to v oboroti, izkliuchva ESP-to. Trugva s vartene na gumi. Parva, vtora, treta - 120. Chetvarta - 160-180-200-220-240. Peta - 260-280-300-320. Vkara shesta - 380... i togava osazna neshto - tova biaha metrite, s koito izostavashe ot Golfa.')
		
		self.e('[type="Submit"]').click()
		
		sleep(1)
		
		self.go('/club/kristestclub')
		self.e_wait('.MultiFile-label img')
		
		self.assertEqual('BMW', self.e('.news-item:nth-of-type(2) h2').text)
		self.delete_event()
		
	@logged_in('club')
	@url('/club/manage/news/')
	def delete_event(self):
		
		self.assertEqual('BMW', self.e('.news-item:nth-of-type(2) h2').text)
		self.e('.news-item:nth-of-type(2) a:nth-of-type(2)').click()
		sleep(1)
		
		self.assertEqual('BMW M', self.e('.news-item h2').text)
		