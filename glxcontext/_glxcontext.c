#include <stdio.h>
#include <stdlib.h>
#include<X11/X.h>
#include<X11/Xlib.h>
#include<GL/gl.h>
#include<GL/glx.h>
#include<GL/glu.h>

Display                 *dpy;
Window                  root;
GLint                   att[] = { GLX_RGBA, None };
XVisualInfo             *vi;
Colormap                cmap;
XSetWindowAttributes    swa;
Window                  win = {0};
GLXContext              glc;
XWindowAttributes       gwa;
XEvent                  xev;

int glx_init() {
    dpy = XOpenDisplay(NULL);
 
    if(dpy == NULL) {
	return -1;
    }
        
    root = DefaultRootWindow(dpy);

    vi = glXChooseVisual(dpy, 0, att);

    if(vi == NULL) {
	return "Error";
    }

    cmap = XCreateColormap(dpy, root, vi->visual, AllocNone);

    swa.colormap = cmap;
    swa.event_mask = ExposureMask | KeyPressMask;
 
    // Width/height here is irrelevant, we're not gonna show it
    win = XCreateWindow(dpy, root, 0, 0, 1, 1, 0, vi->depth, InputOutput, vi->visual, CWColormap | CWEventMask, &swa);

    //XMapWindow(dpy, win);
    //XStoreName(dpy, win, "glx context");
 
    glc = glXCreateContext(dpy, vi, NULL, GL_TRUE);
    glXMakeCurrent(dpy, win, glc);

    return 0;
}


int glx_initialized(){
    return (vi != NULL);
}


void glx_makecurrent(){
    glXMakeCurrent(dpy, win, glc);     
}
