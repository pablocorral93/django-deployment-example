from django import template


register = template.Library()

#You can also do it with decorators
@register.filter(name="cut")
def cut(value,arg):

	"""
	This cuts out all values of "arg" from the string

	"""

	return value.replace(arg,'')


#register.filter('cut', cut)