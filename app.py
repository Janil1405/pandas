import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np




st.sidebar.header("Filtros")




st.title("Isso é um :blue[título] :sunglasses:")
st.header("Isso aqui é um cabeçalho", divider="gray")
st.subheader("Isso aqui é um sub-cabeçalho", divider=True)
st.text("Isso aqui é um texto.")


df = pd.DataFrame(np.random.randn(50,20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)

selecao1 = st.checkbox ("Marcado")

if selecao1:
    st.write(selecao1)
    
    
#Elementos de Seleção

#Checkbox
selecao1= st.checkbox("Marcado")

if selecao1:
    st.write(selecao1)
    
# Cor

cor = st.color_picker("Selecione a cor, #00f900")
st.write("Cor selecionada", cor)


#Multselect

opcoes = st.multiselect(
    "Selecione as opções",
    ["Green", "Yellow", "Red", "Blue"]
)
st.write("Sua seleção", opcoes)
  
  

    
    
    
    


    