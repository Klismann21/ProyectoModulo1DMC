import streamlit as st
st.title("Proyecto módulo 1 Fundamentals")
st.sidebar.title("Parámetros")

st.image("Python_logo.png")
st.sidebar.image("DMC.png")

modulo=st.side.selectbox("Elija un modulito",["Modulito Listas","Modulito Array","Modulito Funciones"])

if modulo="Modulito Listas":

  valor_inicial = st.number_input("Ingrese el valor inicial",value=0)
  valor_final= st.number_input("Ingrese el valor final",value=1)
  
  lista_numerica=list(range(valor_inicial,valor_final))
  
  st.write(lista_numerica)
elif modulo="Modulito Array"
    st.write("Estas en el modulito de arreglos")
    


    
else
    st.write("Estas en el modulo de funciones")
  
