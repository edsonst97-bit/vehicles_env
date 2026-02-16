# 🚗 Dashboard de Análisis de Mercado Automotriz

Esta aplicación web proporciona una interfaz interactiva para explorar un conjunto de datos de anuncios de venta de vehículos en EE. UU. El objetivo es identificar patrones de precios, demanda y depreciación mediante visualizaciones dinámicas.

---

## 🚀 Funcionalidades Interactivas

El dashboard permite generar gráficos bajo demanda utilizando botones para facilitar la navegación:

*   **Distribución de Precios:** Histograma interactivo para entender los rangos de costo más comunes.
*   **Análisis de Depreciación:** Gráfico de dispersión con **línea de tendencia (OLS)** que muestra la relación entre el año del modelo y su precio.
*   **Comparativa por Condición:** Gráficos de caja (boxplots) para evaluar cómo influye el estado del vehículo en su valor final.
*   **Ranking de Modelos:** Visualización del Top 10 de los modelos más frecuentes en el inventario.

## 🛠️ Tecnologías y Librerías

El proyecto ha sido desarrollado utilizando el stack de datos de **Python**:

*   **[Streamlit](https://docs.streamlit.io)**: Para la creación de la interfaz web y el despliegue.
*   **[Pandas](https://pandas.pydata.org)**: Para el procesamiento y limpieza de los datos de `vehicles_us.csv`.
*   **[Plotly Express](https://plotly.com)**: Para la generación de gráficos interactivos y responsivos.
*   **[Statsmodels](https://www.statsmodels.org)**: Utilizado como motor para el cálculo de tendencias de regresión lineal.