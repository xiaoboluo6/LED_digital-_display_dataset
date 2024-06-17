# Author: Ankush Gupta
# Date: 2015
"Script to generate font-models."

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 如果添加了新的字体  需要把所有字体的ttf放进来  生成font_px2pt.cp  后续fontlist.txt里面需要调用data/model/font_px2pt.cp

import pygame
from pygame import freetype
from text_utils import FontState
import numpy as np 
import matplotlib.pyplot as plt 
import _pickle as cp


pygame.init()


ys = np.arange(8,200)
A = np.c_[ys,np.ones_like(ys)]

xs = []
models = {} #linear model

FS = FontState()
FS.fonts = ['data/fonts/LED1/DS-DIGI.TTF',
'data/fonts/LED2/DS-DIGII.TTF',
'data/fonts/LED3/DS-DIGIT.TTF',
'data/fonts/Normalnum1/FUTRFW.TTF',
'data/fonts/Normalnum2/monofontorg.ttf']

#plt.figure()
for i in range(len(FS.fonts)):
	print(i)
	font = freetype.Font(FS.fonts[i], size=12)
	h = []
	for y in ys:
		h.append(font.get_sized_glyph_height(float(y)))
	h = np.array(h)
	m,_,_,_ = np.linalg.lstsq(A,h)
	models[font.name] = m
	xs.append(h)

with open('data/models/num_font_px2pt10000.cp', 'wb') as f:
	cp.dump(models,f)
#plt.plot(xs,ys[i])
#plt.show()
