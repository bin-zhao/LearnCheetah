# coding: utf-8

__author__ = 'Administrator'

from Cheetah.Template import Template


class LayerTemplateBase(Template):

	def __init__(self, *args, **kargs):
		super(LayerTemplateBase, self).__init__(*args, **kargs)
		self.comment			= u'洗炼'
		self.namespace			= 'role'
		self.name				= 'RoleFlush'
		self.model				= 'Role'
		self.btn_back			= True
		self.btn_close			= True
		self.mediator			= True
		self.global_event		= True


	def camel2underline(self, identifier):
		pass


	def underline2camel(self, identifier):
		pass


	def upperFirstLetter(self, identifier):
		pass


if __name__ == '__main__':
	pass
