import glxcontext
from OpenGL.GL import glGetString, GL_VERSION, GL_RENDERER

def test_create():
    glxcontext.makecurrent()
    print 'GL_VERSION:', glGetString(GL_VERSION)
    print 'GL_RENDERER:', glGetString(GL_RENDERER)

if __name__ == '__main__':
    test_create()

