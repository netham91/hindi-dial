# -*- coding: utf-8 -*-
from gtts import gTTS
import csv

a = ["अ","आ","इ","ई","उ","ऊ","ऋ","ए","ऐ","ओ","औ","ब","भ","द","ड","ध","ढ","ग","घ","ह","ज","झ","य","क","ख","म","न","ञ","ण","ङ","ल","प","फ","र","स","ष","श","च","छ","त","ट","थ","ठ","व"]
#print a
#tts = gTTS(text=a[0], lang='hi')
#tts.save("a.mp3")
for x in a:
	tts = gTTS(text=x,lang='hi')
	tts.save(x+".mp3")