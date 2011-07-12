cdef extern from *:
     int glx_init()
     void glx_makecurrent()
     int glx_initialized()


def _check_glxwindow():
    if glx_initialized():
       return

    r = glx_init()

    if r == -1:
       raise IOError("Cannot connect to X server")

    if r == -2:
       raise IOError("Could not create visual")


def makecurrent():
    _check_glxwindow()
    glx_makecurrent()