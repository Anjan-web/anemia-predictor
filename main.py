import streamlit as st
import pandas as pd
from PIL import Image
st.title('Hi! I am streamlit web app')
st.subheader('Hi I am your subheader')
st.header('Hi I am header')
st.text('Hi i am text function and programmers uses me in place of paragraph tag')
st.markdown('[Google](https://www.google.com)')
st.markdown('---')
st.caption('Hi i am your caption')
st.caption('Hi i am your caption2')
json={'a':'1,2,3','b':'4,5,6'}
st.json(json)
code="""""
print('hellow')
def function():
    return 0;"""
st.code(code,language='python')
st.write('## H2')
st.metric(label='Wind speed',value='120mmsp',delta='-12',delta_color='normal')
table=pd.DataFrame({'column 1':[1,2,3,4,5,6],'column 2':[11,12,13,14,15,16]})
st.table(table)
st.dataframe(table)
image = Image.open("anji.jpg")
st.image(image,caption='Anji Photo',width=400)
state= st.checkbox('check box',value=True)
if state:
    st.write('Hi')
else:
    pass
radio_btn=st.radio('In which country do you live?',options=('US','India','Canada','china'))
print(radio_btn)
def dutton_click():
    print('Button clicked')
btn=st.button('Click me',on_click=dutton_click)
st.selectbox('What is your favourite car?',options=('Audi','Jauar','Kia'))
multi_select=st.multiselect('What is your favourite tech?',options=('Microsoft','apple','amazon'))
st.write(multi_select)

