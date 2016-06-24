# coding: utf-8

__author__ = 'Administrator'


# import

import os
import sys
from HomePageBase import HomePageBase


# code

class MyHomePage2(HomePageBase):

	def __init__(self):
		super(self.__class__, self).__init__()


	def title(self):
		return 'my home page 2'


	def body(self):
		return 'the normal body'


if __name__ == '__main__':
	pass
