#!/usr/bin/env python
# coding: utf-8

# Importando paquetes

# In[1]:


## importando paquetes

import pandas as pd
import streamlit as st
import plotly.express as px

# paquetes para mapa de colombia por departamento

import json
import plotly.graph_objs as go
from urllib.request import urlopen

import plotly.offline as pyo # para exportar en html

import datetime 


# importando Json del mapa de Colombia por departamento

# In[3]:


# with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as response:
#     counties = json.load(response)


# Asignando titulos 

# In[4]:


## titulos para la página

st.set_page_config(page_title='Violencia intrafamiliar')
st.header('Estadisticas de Violencia intrafamiliar en Colombia')
st.subheader('del 1 de enero al 31 de octubre de 2023')



# Importando dataframe

# In[5]:


# Cargando datafre
df_violencia_int_2023= pd.read_excel("DATOS/violencia_intrafamiliar_4.xlsx")


# Creando selectores que se despliegan a la derecha de la página

# In[7]:


st.sidebar.header("Opciones a filtrar:") #sidebar lo que nos va a hacer es crear en la parte izquierda un cuadro para agregar los filtros que queremos tener


### funciones 




####



genero= st.sidebar.multiselect(
        "Seleccionar Genero: ",
        options= df_violencia_int_2023['GENERO'].unique(),
        default= df_violencia_int_2023['GENERO'].unique()
)

agrupacion_edad= st.sidebar.multiselect(
    label= 'Seleccione Grupo Etario',
    options= df_violencia_int_2023['AGRUPA_EDAD_PERSONA'].unique(),
    default=df_violencia_int_2023['AGRUPA_EDAD_PERSONA'].unique()
)

departamento= st.sidebar.multiselect(
    label='Seleccione departamento',
    options=df_violencia_int_2023['DEPARTAMENTO'].unique(),
    default=df_violencia_int_2023['DEPARTAMENTO'].unique()
)

mpio= st.sidebar.multiselect(
    label='Seleccione municipio',
    options=df_violencia_int_2023['MUNICIPIO'].unique(),
    default=df_violencia_int_2023['MUNICIPIO'].unique()
)

# boton que elimina los filtros y deja todo en blanco 



# In[8]:


# today = datetime.datetime.now()
# jan_1 = datetime.date(2023, 1, 1)
# oct_31 = datetime.date(2023, 10, 31)


# In[9]:


# dec_31


# In[10]:


# d = st.date_input(
#     "Seleccionar el rango de fechas de la consecución del delito",
#     (jan_1, oct_31),
#     jan_1,
#     oct_31,
#     format="MM.DD.YYYY",
# )
# d


# In[11]:


# Simulando el selector de rango de fechas en Streamlit
jan_1 = pd.to_datetime("2023-01-01")
oct_31 = pd.to_datetime("2023-10-31")
fecha_inicial = st.sidebar.date_input(
    "Seleccionar fecha inicial",
    value=jan_1,
    min_value=jan_1,
    max_value=oct_31
)
fecha_final = st.sidebar.date_input(
    "Seleccionar fecha final",
    value=oct_31,
    min_value=jan_1,
    max_value=oct_31
)

## creando boton para eliminar todos los foltros


# Botón para limpiar los filtros

if st.sidebar.button("Limpiar filtros"):
    genero = st.sidebar.multiselect(
        "Seleccionar Genero: ",
        options=df_violencia_int_2023['GENERO'].unique(),

    )

    agrupacion_edad = st.sidebar.multiselect(
        label='Seleccione Grupo Etario',
        options=df_violencia_int_2023['AGRUPA_EDAD_PERSONA'].unique(),

    )

    departamento = st.sidebar.multiselect(
        label='Seleccione departamento',
        options=df_violencia_int_2023['DEPARTAMENTO'].unique(),

    )

    mpio = st.sidebar.multiselect(
        label='Seleccione municipio',
        options=df_violencia_int_2023['MUNICIPIO'].unique(),

    )






# Creando df enlazado con los selectores

# In[12]:


#df_seleccion=df_violencia_int_2023.query('GENERO == @genero & AGRUPA_EDAD_PERSONA == @agrupacion_edad & DEPARTAMENTO == @departamento')


# In[15]:


df_seleccion = df_violencia_int_2023.query('GENERO == @genero & AGRUPA_EDAD_PERSONA == @agrupacion_edad & DEPARTAMENTO == @departamento & @fecha_inicial <= `FECHA HECHO` <= @fecha_final & MUNICIPIO == @mpio ')



# In[16]:


#consulta


# Calculando KPIs 

# In[17]:


total_delitos = df_seleccion['CANTIDAD'].sum()





#delitos_municipio = (df_seleccion.groupby(by=['MUNICIPIO']).sum()[['CANTIDAD']].sort_values(by='CANTIDAD'))
delitos_municipio = (df_seleccion.groupby(by=['MUNICIPIO']).sum()[['CANTIDAD']].sort_values(by='CANTIDAD'))
delitos_genero = (df_seleccion.groupby(by=['GENERO']).sum()[['CANTIDAD']].sort_values(by='CANTIDAD'))
delitos_g_etario=(df_seleccion.groupby(by=['AGRUPA_EDAD_PERSONA']).sum()[['CANTIDAD']].sort_values(by='CANTIDAD'))
delitos_arma=(df_seleccion.groupby(by=['ARMA MEDIO']).sum() [['CANTIDAD']].sort_values(by='CANTIDAD'))
delitos_dpto= (df_seleccion.groupby(by=['DEPARTAMENTO']).sum()[['CANTIDAD']].sort_values(by='CANTIDAD'))


# In[20]:


# Mostrando dataframe y KPIs

# In[21]:


st.subheader(f"Delitos totales: {total_delitos:,}")


# In[22]:


st.dataframe(df_seleccion)


# In[23]:


delitos_genero.info()


# Creando gráficas

# In[24]:


# Asegurarse de que 'FECHA HECHO' esté en formato de fecha
df_seleccion['FECHA HECHO'] = pd.to_datetime(df_seleccion['FECHA HECHO'])

# Agrupar por fecha (por día en este caso) y sumar la cantidad para cada día
df_agrupado_por_fecha = df_seleccion.groupby(pd.Grouper(key='FECHA HECHO', freq='D')).sum().reset_index()

# Crear el gráfico de línea suavizado por fecha
line_chart_suavizado = px.line(df_agrupado_por_fecha, x='FECHA HECHO', y='CANTIDAD',
                               title='Cantidad de Incidentes a lo largo del tiempo (Suavizado)',
                               labels={'CANTIDAD': 'Cantidad de Incidentes'})

# Mostrar el gráfico suavizado
st.plotly_chart(line_chart_suavizado)


# In[25]:


pie_chart_delitos_genero = px.pie(delitos_genero,
                                  names=delitos_genero.index,
                                  values='CANTIDAD',
                                  title='Casos de violencia intrafamiliar por Género de la víctima')


# In[26]:


st.plotly_chart(pie_chart_delitos_genero)


# In[27]:


#delitos_municipio

fig_delitos_municipio= px.bar( delitos_municipio,
                              x= 'CANTIDAD',
                              y= delitos_municipio.index,
                              orientation='h',
                              title='Casos de violencia intrafamiliar por municipio'
                             )


# In[28]:


st.plotly_chart(fig_delitos_municipio)


# In[29]:


# delitos_g_etario
fig_delitos_g_etario= px.bar(delitos_g_etario,
                             x= delitos_g_etario.index,
                             y='CANTIDAD',
                             title='Cantidad de delitos por grupo etario de la víctima'
                            )


# In[30]:


st.plotly_chart(fig_delitos_g_etario)


# In[31]:


# delitos_arma

fig_delitos_arma=px.bar(delitos_arma,
                        x='CANTIDAD',
                        y=delitos_arma.index,
                        orientation='h',
                        title='Tipos de armas empleadas por delitos'
                        )


# In[32]:
st.plotly_chart(fig_delitos_arma)

pie_chart_arma_delito = px.pie(delitos_arma,
                                  names=delitos_arma.index,
                                  values='CANTIDAD',
                                  title='Tipos de armas empleadas por delitos')


# In[33]:


st.plotly_chart(pie_chart_arma_delito)


# Mapa de delitos de violencia intrafamiliar por departamento en Colombai

# In[34]:


# locs = delitos_dpto.index

# for loc in counties['features']:
#     loc['id'] = loc['properties']['NOMBRE_DPT']
# fig = go.Figure(go.Choroplethmapbox(
#                     geojson=counties,
#                     locations=locs,
#                     z=delitos_dpto['CANTIDAD'],
#                     colorscale='Viridis',
#                     colorbar_title="CANTIDAD"))
# fig.update_layout(mapbox_style="carto-positron",
#                         mapbox_zoom=3.4,
#                         mapbox_center = {"lat": 4.570868, "lon": -74.2973328})
# fig.show()
     


# In[35]:


delitos_dpto

