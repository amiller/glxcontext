import glxcontext
from OpenGL.GL import *
from OpenGL.GL.framebufferobjects import *
import numpy as np
    

def test_offscreen_triangle(size=(200, 200)):
    glxcontext.makecurrent()

    width, height = size

    # Set up the frame buffer
    fbo = glGenFramebuffers(1)
    glBindFramebuffer(GL_FRAMEBUFFER, fbo)

    rbc = glGenRenderbuffers(1)
    glBindRenderbuffer(GL_RENDERBUFFER, rbc)
    glRenderbufferStorage(GL_RENDERBUFFER, GL_RGB8, width, height)
    glFramebufferRenderbuffer(GL_FRAMEBUFFER,
                              GL_COLOR_ATTACHMENT0,
                              GL_RENDERBUFFER, rbc)
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw a triangle of area portion 0.375
    glColor3ub(11, 13, 17)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.75*width, 0.25*height)
    glVertex2f(0.25*width, 0.25*height)
    glVertex2f(0.50*width, 0.75*height)
    glEnd()
    glFinish()

    # Get the pixels back and check they're right
    pixels = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE, outputType='array')

    check = pixels.mean(0).mean(0)
    assert np.all(check == [11 / 8., 13 / 8., 17 / 8.])
    print 'Offscreen render produced correct results'


if __name__ == '__main__':
    test_offscreen_triangle()
