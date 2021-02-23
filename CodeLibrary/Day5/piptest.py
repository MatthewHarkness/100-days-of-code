# https://www.w3schools.com/python/python_pip.asp
# pip package 'camelcase' installed via the following in cmd:
# "pip install camelcase"
# it can be uninstalled just as easily:
# "pip uninstall camelcase"
#find more packages: https://pypi.org/

import camelcase

c = camelcase.CamelCase()

text = 'hello world'

print(c.hump(text))