import streamlit as st
import pandas as pd
from generate_data import generate_sales_data

# Aplicar estilos personalizados
st.markdown("""
    <style>
    /* Cambia el color del título */
    .css-18e3th9 { 
        color: #FF4B4B;
    }
    /* Cambia el color de fondo */
    .css-1aumxhk { 
        background-color: #F0F2F6;
    }
    /* Cambia el color del texto */
    .css-1j7n9i3 { 
        color: #262730;
    }
    /* Ajusta el ancho del cuerpo */
    .css-1n7n5ex { 
        max-width: 1200px; /* Ajusta este valor para el nuevo ancho del contenedor */
        margin: 0 auto; /* Centra el contenido */
    }
    /* Estilos personalizados para columnas */
    .col1 {
        width: 100%;
        float: left;
        padding: 10px;
        box-sizing: border-box;
    }
    .col2 {
        width: 100%;
        float: left;
        padding: 10px;
        box-sizing: border-box;
    }
    /* Estilos personalizados para los botones */
    .stButton > button {
        background-color: #4cd137; /* Fondo verde */
        color:#192a56;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #4cd137; 
        color: #192a56; 
        border: 2px solid #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# Título con formato personalizado
st.markdown("<h1 style='font-size: 40px; text-align: center;'>📊 Generador de Datos de Ventas 💰</h1>", unsafe_allow_html=True)

# Sidebar para parámetros de generación
st.sidebar.header('Parámetros de Generación')

# Parámetros de fecha
start_date = st.sidebar.date_input('Fecha de Inicio', pd.to_datetime('2020-01-01'))
end_date = st.sidebar.date_input('Fecha de Fin', pd.to_datetime('2024-08-29'))

# Parámetros de cantidad
num_records = st.sidebar.slider('Número de Registros', min_value=100, max_value=1000000, value=1000, step=100)

# Parámetros máximos basados en datos suministrados
max_clients = 100  # Ajusta si tienes más o menos clientes en los datos
num_clients = st.sidebar.slider('Número de Clientes', min_value=1, max_value=max_clients, value=min(max_clients, 50))

max_vendors = 50   # Ajusta si tienes más o menos vendedores en los datos
num_vendors = st.sidebar.slider('Número de Vendedores', min_value=1, max_value=max_vendors, value=min(max_vendors, 50))

max_cities = 138    # Ajusta según el número total de ciudades que tienes
num_cities = st.sidebar.slider('Número de Ciudades', min_value=1, max_value=max_cities, value=min(max_cities, 43))

max_products = 85  # Basado en la lista de productos proporcionada
num_products = st.sidebar.slider('Número de Productos', min_value=1, max_value=max_products, value=min(max_products, 35))

# Diseño de la página en dos columnas
st.markdown("""
    <div class="col1">
        Configura los parámetros en la barra lateral.
    </div>
    <div class="col2">
""", unsafe_allow_html=True)

# Generar datos al presionar el botón
if st.sidebar.button('Generar Datos'):
    df = generate_sales_data(start_date, end_date, num_records, num_clients, num_vendors, num_cities, num_products)
    st.write(f"Datos generados: {num_records} registros desde {start_date} hasta {end_date}")
    st.dataframe(df)

    # Mostrar conteo por categoría para ver la distribución de productos
    ##st.write("Distribución de productos por categoría:")
    ##st.dataframe(df['Categoria'].value_counts())

    # Opcional: Descargar los datos como CSV
    csv = df.to_csv(index=False)
    st.download_button(
        label="Descargar CSV",
        data=csv,
        file_name='datos_ventas.csv',
        mime='text/csv'
    )

st.markdown("""
    </div>
""", unsafe_allow_html=True)

# Botón para mostrar la página "Quién Soy"
if st.sidebar.button('Quién Soy'):
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #fffa65;'>QUIÉN SOY?</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center;">
            <img src="https://raw.githubusercontent.com/JUANCITOPENA/ANALISIS_AUTOMATIZADO_PYTHON/main/JuancitoFoto.png" 
                alt="Foto de Juancito Peña" 
                style="width: 200px; height: auto; border-radius: 50%;">
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
       <p style='font-size: 25px; color: #ecf0f1; text-align: justify;'>
        Mi nombre es <strong>Juancito Peña V</strong>, soy <strong>ingeniero en Sistemas y Computación</strong> 💻, con una Especialidad en <strong>Desarrollo de Software</strong> 🖥️, y una Maestría en <strong>Sistemas Mención Gerencial</strong> 🎓. Universidad Dominicana O&M. 
        Actualmente estoy cursando una Maestría en <strong>Ciencia de Datos para Negocios</strong> 📊 (Big Data & Business Analytics). en CEUPE - European Business School. 
        He realizado varios cursos y certificaciones, soy un amante de la <strong>Tecnología</strong> 🚀, de los <strong>Datos</strong> 📈 y de la <strong>Programación</strong> 👨‍💻. 
        Creo en el poder de la tecnología para aportar valor a las personas, a las empresas y a la educación 🎓.
        </p>
        <p style='font-size: 25px; color: #ecf0f1; text-align: justify;'>
        Mis Habilidades van desde Uso con en <strong>SQL</strong> 💾, <strong>Power BI</strong> 📊 y <strong>Python</strong> 🐍 | <strong>Desarrollo de Software</strong> (HTML, CSS, JS, REACT, PHP, C#) 💻, SQL | <strong>Soy Instructor de Grado Universitario</strong> 👨‍🏫, <strong>Padre</strong> 👨‍👩‍👧‍👦 y <strong>Amigo</strong> 🤝.
       </p>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center;">
        <a href="https://www.linkedin.com/in/tu-perfil" target="_blank" style="text-decoration: none; color: #fff200; margin: 0 10px;">
            <i class="fab fa-linkedin" style="font-size: 48px;"></i>
        </a>
        <a href="https://www.youtube.com/channel/tu-canal" target="_blank" style="text-decoration: none; color: #fff200; margin: 0 10px;">
            <i class="fab fa-youtube" style="font-size: 48px;"></i>
        </a>
        <a href="https://github.com/tu-perfil" target="_blank" style="text-decoration: none; color: #fff200; margin: 0 10px;">
            <i class="fab fa-github" style="font-size: 48px;"></i>
        </a>
        <a href="https://twitter.com/tu-perfil" target="_blank" style="text-decoration: none; color: #fff200; margin: 0 10px;">
            <i class="fab fa-twitter" style="font-size: 48px;"></i>
        </a>
        <a href="https://www.facebook.com/tu-perfil" target="_blank" style="text-decoration: none; color: #fff200; margin: 0 10px;">
            <i class="fab fa-facebook" style="font-size: 48px;"></i>
        </a>
        <a href="https://www.instagram.com/tu-perfil" target="_blank" style="text-decoration: none; color: #fff200; margin: 0 10px;">
            <i class="fab fa-instagram" style="font-size: 48px;"></i>
        </a>
    </div>
    
    
    
    """, unsafe_allow_html=True)
    st.markdown("""
        <p style='font-size: 25px; color: #ecf0f1; text-align: center; margin-top: 20px;'>
        Si te interesa este Reporte y tenerlo en tus proyectos, contáctame al: 
        <a href="mailto:juancito.pena@gmail.com" style='color: #1f77b4;'>juancito.pena@gmail.com</a>. Acordemos un precio.
        </p>
    """, unsafe_allow_html=True)
 
