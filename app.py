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


df=pd.DataFrame(np.random.randn(50,20)), columns=("col %d" % i for i in range(20))
st.dataframe(df)

selecao1 = st.checkbox ("Marcado")

if selecao1
    st.write(selecao1)