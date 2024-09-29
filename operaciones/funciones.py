import streamlit as st


def inicio():
    logo_ici='C:/Users/Colibecas/OneDrive/Pictures/Imagenes/ici.png'
    introduccion= """
     Este programa ofrece una variedad de herramientas interactivas para simplificar 
     tareas comunes. Podrás realizar cálculos como sumar números, obtener el área de un 
     triángulo, aplicar descuentos, y mucho más. Además, incluye funciones avanzadas como 
     el uso de argumentos variables y una calculadora flexible. Explora las opciones del 
     menú para encontrar la herramienta que necesitas y disfruta de una experiencia 
     rápida y sencilla. 
         
     Instrucciones de uso:
     De el lado izquierdo tienes el menú, dale click para conocer el catalogo.
     """

    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(logo_ici)
    st.markdown("<h1 style='text-align: center; color: white;'>Tablero Interactivo ICI</h1>", unsafe_allow_html=True)
    st.markdown("<hr/>",unsafe_allow_html=True)
    st.markdown("<h5>¡Bienvenido al Tablero Interactivo ICI!</h5>",unsafe_allow_html=True)
    st.text(introduccion)
        
        
def saludo_simple():
    st.markdown("## Saludo simple")
    nombre = st.text_input("Escribe tu nombre:")
    if st.button("Saludar"):
        st.write(f"¡Hola, {nombre}!")

def suma_dos_numeros():
    st.markdown("## Suma de dos números")
    num1 = st.number_input("Introduce el primer número:", step=1.0)
    num2 = st.number_input("Introduce el segundo número:", step=1.0)
    if st.button("Sumar"):
        resultado = num1 + num2
        st.write(f"La suma es: {resultado}")

def area_triangulo():
    st.markdown("## Área de un triángulo")
    base = st.number_input("Introduce la base del triángulo:", step=1.0)
    altura = st.number_input("Introduce la altura del triángulo:", step=1.0)
    if st.button("Calcular área"):
        area = (base * altura) / 2
        st.write(f"El área del triángulo es: {area}")

def calculadora_descuento():
    st.markdown("## Calculadora de descuento")
    precio = st.number_input("Introduce el precio original:", step=1.0)
    
    descuento = st.number_input("Introduce el porcentaje de descuento (opcional, por defecto 10%):", value=10, step=1) #Necesitan ser del mismo tipo si no da error de tipo.
    impuesto = st.number_input("Introduce el porcentaje de impuesto (opcional, por defecto 16%):", value=16, step=1)
    
    if st.button("Calcular precio final"):
        precio_descuento = precio - (precio * descuento / 100) # El descuento es del 10% sobre el precio original
        precio_final = precio_descuento + (precio_descuento * impuesto / 100) #el impuesto es  16% sobre el precio después del descuento.
        st.write(f"El precio final es: {precio_final}")

def suma_lista_numeros():
    st.markdown("## Suma de una lista de números")
    lista_numeros = st.text_input("Introduce una lista de números separados por comas:")
    if st.button("Sumar lista"):
        numeros = [float(n) for n in lista_numeros.split(",")]
        suma = sum(numeros)
        st.write(f"La suma de la lista es: {suma}")

def funciones_valores_predeterminados():
    st.markdown("## Funciones con valores predeterminados")
    def producto(nombre, cantidad=1, precio=10):
        return f"Total por {cantidad} unidad(es) de {nombre}: {cantidad * precio}"
    
    nombre = st.text_input("Introduce el nombre del producto:")
    cantidad = st.number_input("Cantidad (por defecto 1):", value=1, step=1)
    precio = st.number_input("Precio por unidad (por defecto 10):", value=10.0, step=1.0)
    
    if st.button("Calcular precio total"):
        st.write(producto(nombre, cantidad, precio))

def numeros_pares_impares():
    st.markdown("## Números pares e impares")
    lista_numeros = st.text_input("Introduce una lista de números separados por comas:")
    if st.button("Separar pares e impares"):
        numeros = [int(n) for n in lista_numeros.split(",")]
        pares = [n for n in numeros if n % 2 == 0]
        impares = [n for n in numeros if n % 2 != 0]
        st.write(f"Números pares: {pares}")
        st.write(f"Números impares: {impares}")

def multi_args():
    st.markdown("## Multiplicación con *args")
    lista_numeros = st.text_input("Introduce una lista de números separados por comas para multiplicar:")
    if st.button("Multiplicar"):
        if lista_numeros:  # Verifica si la lista no está vacía
            try:
                numeros = [float(n) for n in lista_numeros.split(",")]
                def multiplicar(*args):
                    resultado = 1
                    for num in args:
                        resultado *= num
                    return resultado
                resultado = multiplicar(*numeros)
                st.write(f"El resultado de la multiplicación es: {resultado}")
            except ValueError:
                st.error("Por favor, introduce una lista válida de números separados por comas.")
        else:
            st.warning("No se ha introducido ninguna lista de números.")


def info_persona_kwargs():
    st.markdown("## Información de una persona con **kwargs")
    nombre = st.text_input("Nombre:")
    edad = st.number_input("Edad:", step=1, format="%d")  # Asegúrate de que sea un número entero
    ciudad = st.text_input("Ciudad:")
    
    if st.button("Mostrar información"):
        if nombre and edad and ciudad:  # Verifica si todos los campos están llenos
            def mostrar_info(**kwargs):
                for key, value in kwargs.items():
                    st.write(f"{key}: {value}")
            mostrar_info(Nombre=nombre, Edad=edad, Ciudad=ciudad)
        else:
            st.warning("Por favor, llena todos los campos antes de enviar.")

def calculadora_flexible():
    st.markdown("## Calculadora flexible")
    num1 = st.number_input("Introduce el primer número para la operación:", step=1.0)
    num2 = st.number_input("Introduce el segundo número para la operación:", step=1.0)
    operacion = st.selectbox("Elige una operación", ["Suma", "Resta", "Multiplicación", "División"])
    if st.button("Calcular"):
        if operacion == "Suma":
            resultado = num1 + num2
        elif operacion == "Resta":
            resultado = num1 - num2
        elif operacion == "Multiplicación":
            resultado = num1 * num2
        elif operacion == "División":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "No se puede dividir entre 0"
        st.write(f"El resultado de la {operacion} es: {resultado}")
        
        
def info_conctacto():
    st.title(":blue[Acerca de mi] :sunglasses:")
    
    st.markdown("""
    <p>Hola, mi nombre es <strong>Juan Pablo</strong>, soy estudiante de la carrera Ingenieria en Computacion Inteligente.
    En mi corta trayectoria he aprendido las bases de diversos lenguajes de programacion como c ,java ,python, etc.. 
    Tengo experiencia en el desarrollo de aplicaciones web utilizando Python y Streamlit, y disfruto 
    creando soluciones que simplifiquen las tareas de los usuarios.
    Esto apenas comienza, puedes seguir mi rastro en las siguientes redes sociales:</p>
    
    <h4><strong>Contacta conmigo<strong></h4>
    <p>Si tienes alguna pregunta o quieres saber más sobre mis proyectos, puedes contactarme en:</p>
    <ul>
        <li><strong>Email:</strong> jpandurreyes@gmail.com</li>
        <li><strong>GitHub:</strong> <a href="https://github.com/Jpandurre" target="_blank">github.com/Jpandurre</a></li>
        <li><strong>Instagram:</strong> <a href="https://www.instagram.com/juan.pablo_3/" target="_blank">@juan.pablo_3</a></li>
    </ul>
    
    <p>¡Gracias por visitar el Tablero Interactivo ICI!</p>
    """, unsafe_allow_html=True)