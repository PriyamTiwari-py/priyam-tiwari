import streamlit as st
import cv2
from PIL import Image,ImageEnhance 
import numpy as np
import os
@st.cache
def load(img):
	img=Image.open(img)
	return img
def main():
	st.title('---------------face detection----------------')
	activities=['detection','about']
	choice=st.sidebar.selectbox('select',activities)
	if choice=='detection':
		st.subheader('face detection')
		img=st.file_uploader('upload',type=['jpg','png','jpeg'])
		if img is not None:
			img1=load(img)
			img1=np.array(img1.convert('RGB'))
			img1=cv2.cvtColor(img1,1)
			img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
			st.text('original')
			st.image(img1)

	elif choice=='about':
		st.subheader('about')
if __name__=='__main__':	
	main()