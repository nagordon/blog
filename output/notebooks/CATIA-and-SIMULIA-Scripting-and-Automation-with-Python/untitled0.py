# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 15:40:48 2015

@author: ngordon
"""

from moviepy.editor import VideoFileClip

def avi_to_gif(odbname):
    """converts an avi video file to an animated gif so that it can easily be
        easily inserted into a pptx
        avidir = 'customBeamExample'
    """
    avinames=glob.glob(os.path.dirname(odbname)+'/*.avi')
    for aviname in avinames:
        clip = VideoFileClip(aviname)
        clip.write_gif(os.path.splitext(aviname)[0]+'.gif')