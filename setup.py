from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules=[Extension("glxcontext",
                       ["glxcontext/_glxcontext.c",
                       "glxcontext/glxcontext.pyx"],
                       libraries=['X11','GL'])]

setup(name='glxcontext',
      version='0.01',
      packages=['glxcontext'],
      cmdclass={'build_ext': build_ext},
      ext_modules=ext_modules)
