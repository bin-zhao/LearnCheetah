# coding: utf-8

__author__ = 'Administrator'


from Cheetah.Template import Template
import os


templateDef = """
<HTML>
<HEAD><TITLE>$title</TITLE></HEAD>
<BODY>
$contents
## this is a single-line Cheetah comment and won't appear in the output
#* This is a multi-line comment and won't appear in the output
blah, blah, blah
*#
</BODY>
</HTML>"""

# 0

def test0():
	nameSpace = {'title': 'Hello World Example', 'contents': 'Hello World!'}

	t = Template(templateDef, searchList=[nameSpace])

	print(t)


# 1

def test1():
	t			= Template(templateDef)

	t.title		= 'MyTitle'
	t.contents	= 'MyContents'
	print(t)

	t.title		= 'my_title'
	t.contents	= 'my_contents'
	print(t)


# 2

class TemplateDef(Template):
	title		= 'class_title'
	contents	= 'class_contents'

def test2():
	obj				= TemplateDef(templateDef)
	print(obj)


# 3

class PrecompiledTemplate(Template):

	def __init__(self):
		super(self.__class__, self).__init__()


def test3():
	t				= PrecompiledTemplate()
	t.title			= 'precompiled_title'
	t.content		= 'precompiled_contents'
	print(t)


# 4

def test4():
	t				= Template('just simple')
	print(t)


# 5

class SearchObject(object):

	name					= 'Lucy'

	def __init__(self):
		self.name			= 'Tommy'


def test5():
	templateStr		= 'You say:\n\tHello, $name!'
	fileName		= 'F:/_python/HelloWorld.tmpl'
	fileName1		= 'F:/_python/HelloWorld.txt'

	t				= Template(templateStr)
	t.name			= 'Tom'									# 没有name会异常
	print(t)

	t				= Template(file = fileName)
	t.name			= 'Jerray'
	print(t)

	f				= open(fileName)
	t				= Template(file = f)
	t.name			= 'Jack'
	print(t)

	searchList		= ({'name' : 'abc'}, SearchObject())

	# 用class打印Lucy，用object打印Tommy，顺序从前往后
	t				= Template(templateStr, searchList = searchList)
	print(t)

	t				= Template(file = fileName1, searchList = searchList)
	print(t)

	f.seek(0)
	t				= Template(file = f, searchList = searchList)
	print(t)

	f.close()


# 6

def test6():
	# templateStr			= '''
	# #set $namespace0			= '[namespace0]'
	# #set $subPlaceHolder		= '[sub]'
	# #set $namespace1			= '[namespace1]'
	# $namespace0.name['attr']('abc', $subPlaceHolder, 1)
	# ${namespace1.name['attr']('abc', $subPlaceHolder, 1)}
	# '''
	templateStr			= ''''''
	t					= Template(templateStr)
	print(t)


# if __name__ == '__main__':
# test1()
# test2()
# test3()
# test4()
# test5()
test6()