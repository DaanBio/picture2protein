
import pandas as pd
import numpy as np
import math
from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st

@st.cache
def load_image(uploaded_file):
	img = Image.open(uploaded_file)
	return img

st.title("Picture2Protein")
st.subheader("Please upload your picture below")
st.write("This program allows you to turn images in amino acid sequences. Have you ever wondered what you look like as a protein? Use this page together with the [alphafold collab notebook](https://colab.research.google.com/github/deepmind/alphafold/blob/main/notebooks/AlphaFold.ipynb) to find out!")
uploaded_file = st.file_uploader("Upload Files", type=['png', 'jpeg'])
if uploaded_file is not None:
    file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    img = load_image(uploaded_file)
    st.image(img)
    width, height = img.size
    ratio = width / height
    new_width = 30
    new_height = int(new_width / ratio)
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    width, height = img.size
    Number_of_AA = (width * height) + height
    st.subheader(f"The amount of amino acids in your sequence is {Number_of_AA}")
    if Number_of_AA>750:
        st.write("Warning: The amount of aminoacids in your sequence is large, it can take very long times for alphafold to make a prediction. Consider changing the image width.")
    else:
        pass	
    img = img.convert('L')
    pixel_data = np.array(img)
    amino_acid = []
    amino_acid_seq = ""
    for i in pixel_data:
        for j in i:
            if j <= 13:
                j = 'W'
            elif 13 < j <= 26:
                j = 'C'
            elif 26 < j <= 40:
                j = 'M'
            elif 40 < j <= 53:
                j = 'F'
            elif 53 < j <= 66:
                j = 'P'
            elif 66 < j <= 80:
                j = 'I'
            elif 80 < j <= 94:
                j = 'T'
            elif 94 < j <= 108:
                j = 'V'
            elif 108 < j <= 121:
                j = 'A'
            elif 121 < j <= 133:
                j = 'L'
            elif 133 < j <= 146:
                j = 'S'
            elif 146 < j <= 159:
                j = 'G'
            elif 159 < j <= 173:
                j = 'E'
            elif 173 < j <= 187:
                j = 'K'
            elif 187 < j <= 201:
                j = 'R'
            elif 201 < j <= 214:
                j = 'D'
            elif 214 < j <= 227:
                j = 'N'
            elif 227 < j <= 240:
                j = 'Q'
            else:
                j = 'Y'
            amino_acid.append(j)
            amino_acid_seq = amino_acid_seq + j
        amino_acid.append('H')
        amino_acid_seq = amino_acid_seq + 'H'
    st.subheader("The amino acid sequence")
    st.write(amino_acid_seq)
