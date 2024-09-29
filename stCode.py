import streamlit as st
from operaciones import funciones 

optionsMenu=["Inicio","Saludo simple","Suma de dos números","Área de un triángulo","Calculadora de descuento","Suma de una lista de números","Funciones con valores predeterminados","Números pares e impares","Multiplicación con *args","Información de una persona con **kwargs","Calculadora flexible", "Contacto"]
selectOption=st.sidebar.selectbox("Menú",optionsMenu)

match selectOption:
    case "Inicio":
        funciones.inicio()
          
    case "Saludo simple":
        funciones.saludo_simple()
        
    case "Suma de dos números":
        funciones.suma_dos_numeros()
        
    case "Área de un triángulo":
        funciones.area_triangulo()
        
    case "Calculadora de descuento":
        funciones.calculadora_descuento()
        
    case "Suma de una lista de números":
        funciones.suma_lista_numeros()
        
    case "Funciones con valores predeterminados":
        funciones.funciones_valores_predeterminados()
        
    case "Números pares e impares":
        funciones.numeros_pares_impares()
        
    case "Multiplicación con *args":
        funciones.multi_args()
        
    case "Información de una persona con **kwargs":
        funciones.info_persona_kwargs()
        
    case "Calculadora flexible":
        funciones.calculadora_flexible()
        
    case "Contacto":
        funciones.info_conctacto()