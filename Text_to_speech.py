# -*- coding: utf-8 -*-
"""


@author: Vasudev 
"""

# -*- coding: utf-8 -*-
"""

@author: Vasudev
"""


import streamlit as st
from gtts import gTTS 
import PyPDF2

st.header("Convert Your Text into Speech or Speech into Text and PDF to Speech ")

def audio_output(text,lan):
    text_obj = gTTS(text=text, lang=lan,slow=False)
    text_obj.save("temp.mp3")
    return st.audio("temp.mp3")

out = st.radio("",["Text To Speech","PDF To Speech"],horizontal=True)
if out == "Text To Speech":
    list_lang= ["English","Hindi","Marathi","Gujarati","Malayalam","Tamil",
    "Telugu","Kannada","Urdu","Bengali","French","German","Greek","Rassian"]

    lang_dic = {"English":"en","Hindi":"hi","Marathi":"mr","Gujarati":"gu",
    "Malayalam":"ml","Tamil":"ta","Telugu":"te","Urdu":"ur","Bengali":"bn",
    "French":"fr","German":"de","Greek":"el","Kannada":"kn","Rassian":"ru"}

    start = st.selectbox("Select Language",list_lang)
    text = st.text_area("Enter Text Here...")
    lang_code = lang_dic.get(start)

    if st.button("Convert"):
        audio_output(text,lang_code)

elif out == "PDF To Speech":
    file = st.file_uploader('Choose your .pdf file', type="pdf")
    if file is not None:
        #file = open(uploaded_file)
        reader = PyPDF2.PdfFileReader(file,"rb")
        page = st.number_input("Enter Page Number",step=1,min_value=1)
        text = reader.getPage(page-1).extract_text()
        if st.button("Convert"):
            audio_output(text,"en")
            if st.button("View text"):
                st.write(text)
