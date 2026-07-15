import numpy as np
import streamlit as st
import libreria_funciones as lf
st.title("Proyecto módulo 1 Fundamentals")
st.sidebar.title("Parámetros")

st.image("Python_logo.png")
st.sidebar.image("DMC.png")

modulo=st.sidebar.selectbox("Elija un modulito",["Modulito Listas","Modulito Array","Modulito Funciones"])

if modulo=="Modulito Listas":

  valor_inicial = st.number_input("Ingrese el valor inicial",value=0)
  valor_final= st.number_input("Ingrese el valor final",value=1)
  
  lista_numerica=list(range(valor_inicial,valor_final))
  
  st.write(lista_numerica)
elif modulo=="Modulito Array":
  st.write("Estas en el modulito de arreglos")
  limite_inferior=st.number_input("Ingrese el límite inferior",value=1200)
  limite_superior=st.number_input("Ingrese el límite superior",value=1250)
  cantidad_datos=st.number_input("Ingrese la totalidad de datos a crear",value=31)

  datos_produccion=np.random.randint(limite_inferior,limite_superior,cantidad_datos)
  st.write(datos_produccion)

  st.write("La produccion total es :",np.sum(datos_produccion))
  st.write("La prucción promedio es" , np.mean(datos_produccion))

    
else:
  st.write("Estas en el modulo de funciones")

  principal=st.number_input("Monto de Prestamo",value=0)
  tasa_anual=st.number_input("Tasa anual en decimal",value=0.10)
  anios=st.number_input("Ingrese el numero de años del prestamo",value=1)
  pagos_por_anio=st.number_input("Ingrese la cantidad de veces a pagar por año",value=12)
  cuota= lf.cuota_prestamo(principal,tasa_anual,pagos_por_anio)
  st.write("El valor de las cuotas mensuales es :",cuota)
