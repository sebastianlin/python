

from distutils.core import setup, Extension
setup(name='cextension', version='1.0',  \
      ext_modules=[Extension('cextension', ['demo34.c'])])


