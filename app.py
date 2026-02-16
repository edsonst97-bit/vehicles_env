import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Datos de Vehículos')

# Histograma de Precios 
price_button = st.button('Construir histograma de precios')

if price_button:
    st.write('Distribución de precios de los vehículos')
    
    fig = px.histogram(car_data, x="price", nbins=50, 
                       title="Distribución de Precios de los Vehículos",
                       color_discrete_sequence=['skyblue'], 
                       marginal="rug") 
    
    fig.update_layout(xaxis_title="Precio (USD)", yaxis_title="Frecuencia")
    st.plotly_chart(fig, use_container_width=True)

#Precios por Condición
if st.button('Comparar precios por condición'):
    st.write('Relación entre la condición del vehículo y su precio de venta')
    
    # Creamos el boxplot con plotly.express
    fig = px.box(car_data, 
                 x='condition', 
                 y='price', 
                 color='condition',
                 title='Comparación de Precios por Condición del Vehículo',
                 labels={'condition': 'Condición', 'price': 'Precio (USD)'})
    
    st.plotly_chart(fig, use_container_width=True)

#Top 10 
if st.button('Mostrar Top 10 Modelos'):
    st.write('Los 10 modelos de autos con más anuncios en el sistema')
    
    # 1. Procesamiento de datos con Pandas
    top_10_series = car_data['model'].value_counts().head(10)
    # Convertimos a DataFrame para que Plotly lo lea fácilmente
    top_10_df = top_10_series.reset_index()
    top_10_df.columns = ['model', 'count']
    
    # 2. Crear gráfico de barras horizontales
    fig = px.bar(top_10_df, 
                 y='model', 
                 x='count', 
                 orientation='h', # Barra horizontal
                 title='Top 10 Modelos de Autos Más Frecuentes',
                 color='count', # Color basado en la frecuencia
                 color_continuous_scale='magma', # Paleta solicitada
                 labels={'model': 'Modelo', 'count': 'Cantidad de Vehículos'})
    
    # Invertir el eje Y para que el más frecuente aparezca arriba
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    
    st.plotly_chart(fig, use_container_width=True)

    # Análisis de Depreciación ---
if st.button('Analizar Depreciación (Año vs Precio)'):
    st.write('Relación entre el año del modelo y el precio de venta con línea de tendencia')
    
    # Crear el scatter plot con línea de tendencia
    fig = px.scatter(car_data, 
                     x='model_year', 
                     y='price', 
                     opacity=0.5, # Equivalente a alpha=0.5
                     trendline="ols", # Agrega la línea de regresión lineal (Mínimos Cuadrados Ordinarios)
                     trendline_color_override="red", # Color de la línea de tendencia
                     title='Análisis de Depreciación: Año del Modelo vs Precio',
                     labels={'model_year': 'Año del Modelo', 'price': 'Precio (USD)'},
                     color_discrete_sequence=['royalblue']) # Color de los puntos
    
    # Mejorar el diseño (grid y estilo)
    fig.update_layout(xaxis=dict(showgrid=True, gridcolor='LightGray'),
                      yaxis=dict(showgrid=True, gridcolor='LightGray'))
    
    st.plotly_chart(fig, use_container_width=True)