# coding: utf-8

__author__ = 'Administrator'

from Cheetah.Template import Template


class MyTemplate(Template):

	COUNT				= 10

	def __init__(self, *args, **kargs):
		super(self.__class__, self).__init__(*args, **kargs)
		self.size		= 11


	def fnTest(self):
		return 'MyTemplate.fnTest'


def test():
	t				= MyTemplate(file = 'programBaseTmpl.tmpl')
	print(t)


# if __name__ == '__main__':
# 	test()
test()