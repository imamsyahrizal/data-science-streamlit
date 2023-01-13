# This code is for study only and from Tutorial by DATA PROFESSOR 
# Link original code https://github.com/dataprofessor/streamlit_freecodecamp

##### Import Libraries #####
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

##### Page Title #####

# import image
image = Image.open('SimpleDna\dna-logo.jpg')
# display image
st.image(image, use_column_width=True)

st.write(
    """
    # DNA Nucleotide Count Web Appp

    This app counts the nucleotide composition of query DNA!

    ***
    """
)

##### Input Text Box #####

st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines() # Split per baris
sequence = sequence[1:] # Skip first list
sequence = ''.join(sequence) # Concatenates list to string

st.write(
    """
    ***
    """
)

## Print input DNA sequence 
st.header('INPUT (DNA Query)')
sequence

## DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print dictionary
st.subheader('1. Print dictionary')

def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)
X

### 2. Print text
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')      # membuat DataFrame
df = df.rename({0: 'count'}, axis='columns')        # mengganti nama kolom 0 menjadi count
df.reset_index(inplace=True)                        # membuat index menjadi urutan (sebelumnya index menggunakan nucleotide)
df = df.rename(columns={'index' : 'nucleotide'})    # mengganti nama kolom index menjadi nucleotide
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)                              # mengatur ukuran lebar bar
)
st.write(p)