#!/usr/bin/env python
# coding: utf-8

# **Código de preprocesamiento** 
# 
# Este cuaderno sirve para crear los df de producción de Petroleo y de Gas en Colombia

# Impotando paquetes

# In[149]:


import pandas as pd


# Importando Datos 

# Importando datos oil

# In[150]:


df_oil_2014 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\OIL\\Produccion_Fiscalizada_Crudo_2014.xlsx')
df_oil_2015 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\OIL\\Produccion_Fiscalizada_Crudo_2015.xlsx')
df_oil_2016 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\OIL\\Produccion_Fiscalizada_Crudo_2016.xlsx')
df_oil_2017 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\OIL\\Produccion_Fiscalizada_Crudo_2017.xlsx')
df_oil_2018 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\OIL\\Produccion_Fiscalizada_Crudo_2018.xlsx')
df_oil_2019 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\OIL\\Produccion_Fiscalizada_Crudo_2019.xlsx')
df_oil_2020 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\OIL\\Produccion_Fiscalizada_Crudo_2020.xlsx')
df_oil_2021 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\OIL\\Produccion_Fiscalizada_Crudo_2021.xlsx')
df_oil_2022 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\OIL\\Produccion_Fiscalizada_Crudo_2022.xlsx')
df_oil_2023 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\OIL\\Produccion_Fiscalizada_Crudo_2023.xlsx')


# Importando paquetes de Gas

# In[151]:


df_gas_2018 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\GAS\\Produccion_Fiscalizada_Gas_2018.xlsx')
df_gas_2019 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\GAS\\Produccion_Fiscalizada_Gas_2019.xlsx')
df_gas_2020 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\GAS\\Produccion_Fiscalizada_Gas_2020.xlsx')
df_gas_2021 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\GAS\\Produccion_Fiscalizada_Gas_2021.xlsx')
df_gas_2022 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\GAS\\Produccion_Fiscalizada_Gas_2022.xlsx')
df_gas_2023 = pd.read_excel('C:\\Users\\Miguel Gomez\\Documents\\DOCUMENTOS MIGUEL\\proyectos_autonomos\\Producción_hidrocarburos_colombia\\GAS\\Produccion_Fiscalizada_Gas_2023.xlsx')


# In[152]:


df_gas_2019


# leyendo df

# In[153]:


df_oil_2014


# In[154]:


# cambiar el nombre enero a 01 de df_oil_2020
df_oil_2014.rename(columns={'enero':'01'}, inplace=True)
df_oil_2014.rename(columns={'febrero':'02'}, inplace=True)
df_oil_2014.rename(columns={'marzo':'03'}, inplace=True)
df_oil_2014.rename(columns={'abril':'04'}, inplace=True)
df_oil_2014.rename(columns={'mayo':'05'}, inplace=True)
df_oil_2014.rename(columns={'junio':'06'}, inplace=True)
df_oil_2014.rename(columns={'julio':'07'}, inplace=True)
df_oil_2014.rename(columns={'agosto':'08'}, inplace=True)
df_oil_2014.rename(columns={'septiembre':'09'}, inplace=True)
df_oil_2014.rename(columns={'octubre':'10'}, inplace=True)
df_oil_2014.rename(columns={'noviembre':'11'}, inplace=True)
df_oil_2014.rename(columns={'diciembre':'12'}, inplace=True)

df_oil_2015.rename(columns={'enero':'01'}, inplace=True)
df_oil_2015.rename(columns={'febrero':'02'}, inplace=True)
df_oil_2015.rename(columns={'marzo':'03'}, inplace=True)
df_oil_2015.rename(columns={'abril':'04'}, inplace=True)
df_oil_2015.rename(columns={'mayo':'05'}, inplace=True)
df_oil_2015.rename(columns={'junio':'06'}, inplace=True)
df_oil_2015.rename(columns={'julio':'07'}, inplace=True)
df_oil_2015.rename(columns={'agosto':'08'}, inplace=True)
df_oil_2015.rename(columns={'septiembre':'09'}, inplace=True)
df_oil_2015.rename(columns={'octubre':'10'}, inplace=True)
df_oil_2015.rename(columns={'noviembre':'11'}, inplace=True)
df_oil_2015.rename(columns={'diciembre':'12'}, inplace=True)

df_oil_2016.rename(columns={'enero':'01'}, inplace=True)
df_oil_2016.rename(columns={'febrero':'02'}, inplace=True)
df_oil_2016.rename(columns={'marzo':'03'}, inplace=True)
df_oil_2016.rename(columns={'abril':'04'}, inplace=True)
df_oil_2016.rename(columns={'mayo':'05'}, inplace=True)
df_oil_2016.rename(columns={'junio':'06'}, inplace=True)
df_oil_2016.rename(columns={'julio':'07'}, inplace=True)
df_oil_2016.rename(columns={'agosto':'08'}, inplace=True)
df_oil_2016.rename(columns={'septiembre':'09'}, inplace=True)
df_oil_2016.rename(columns={'octubre':'10'}, inplace=True)
df_oil_2016.rename(columns={'noviembre':'11'}, inplace=True)
df_oil_2016.rename(columns={'diciembre':'12'}, inplace=True)

df_oil_2017.rename(columns={'enero':'01'}, inplace=True)
df_oil_2017.rename(columns={'febrero':'02'}, inplace=True)
df_oil_2017.rename(columns={'marzo':'03'}, inplace=True)
df_oil_2017.rename(columns={'abril':'04'}, inplace=True)
df_oil_2017.rename(columns={'mayo':'05'}, inplace=True)
df_oil_2017.rename(columns={'junio':'06'}, inplace=True)
df_oil_2017.rename(columns={'julio':'07'}, inplace=True)
df_oil_2017.rename(columns={'agosto':'08'}, inplace=True)
df_oil_2017.rename(columns={'septiembre':'09'}, inplace=True)
df_oil_2017.rename(columns={'octubre':'10'}, inplace=True)
df_oil_2017.rename(columns={'noviembre':'11'}, inplace=True)
df_oil_2017.rename(columns={'diciembre':'12'}, inplace=True)

df_oil_2018.rename(columns={'enero':'01'}, inplace=True)
df_oil_2018.rename(columns={'febrero':'02'}, inplace=True)
df_oil_2018.rename(columns={'marzo':'03'}, inplace=True)
df_oil_2018.rename(columns={'abril':'04'}, inplace=True)
df_oil_2018.rename(columns={'mayo':'05'}, inplace=True)
df_oil_2018.rename(columns={'junio':'06'}, inplace=True)
df_oil_2018.rename(columns={'julio':'07'}, inplace=True)
df_oil_2018.rename(columns={'agosto':'08'}, inplace=True)
df_oil_2018.rename(columns={'septiembre':'09'}, inplace=True)
df_oil_2018.rename(columns={'octubre':'10'}, inplace=True)
df_oil_2018.rename(columns={'noviembre':'11'}, inplace=True)
df_oil_2018.rename(columns={'diciembre':'12'}, inplace=True)

df_oil_2019.rename(columns={'enero':'01'}, inplace=True)
df_oil_2019.rename(columns={'febrero':'02'}, inplace=True)
df_oil_2019.rename(columns={'marzo':'03'}, inplace=True)
df_oil_2019.rename(columns={'abril':'04'}, inplace=True)
df_oil_2019.rename(columns={'mayo':'05'}, inplace=True)
df_oil_2019.rename(columns={'junio':'06'}, inplace=True)
df_oil_2019.rename(columns={'julio':'07'}, inplace=True)
df_oil_2019.rename(columns={'agosto':'08'}, inplace=True)
df_oil_2019.rename(columns={'septiembre':'09'}, inplace=True)
df_oil_2019.rename(columns={'octubre':'10'}, inplace=True)
df_oil_2019.rename(columns={'noviembre':'11'}, inplace=True)
df_oil_2019.rename(columns={'diciembre':'12'}, inplace=True)


# In[155]:


# cambiar el nombre enero a 01 de df_oil_2020
df_oil_2020.rename(columns={'enero':'01'}, inplace=True)
df_oil_2020.rename(columns={'febrero':'02'}, inplace=True)
df_oil_2020.rename(columns={'marzo':'03'}, inplace=True)
df_oil_2020.rename(columns={'abril':'04'}, inplace=True)
df_oil_2020.rename(columns={'mayo':'05'}, inplace=True)
df_oil_2020.rename(columns={'junio':'06'}, inplace=True)
df_oil_2020.rename(columns={'julio':'07'}, inplace=True)
df_oil_2020.rename(columns={'agosto':'08'}, inplace=True)
df_oil_2020.rename(columns={'septiembre':'09'}, inplace=True)
df_oil_2020.rename(columns={'octubre':'10'}, inplace=True)
df_oil_2020.rename(columns={'noviembre':'11'}, inplace=True)
df_oil_2020.rename(columns={'diciembre':'12'}, inplace=True)

# cambiar el nombre enero a 01 de df_oil_2021
df_oil_2021.rename(columns={'enero':'01'}, inplace=True)
df_oil_2021.rename(columns={'febrero':'02'}, inplace=True)
df_oil_2021.rename(columns={'marzo':'03'}, inplace=True)
df_oil_2021.rename(columns={'abril':'04'}, inplace=True)
df_oil_2021.rename(columns={'mayo':'05'}, inplace=True)
df_oil_2021.rename(columns={'junio':'06'}, inplace=True)
df_oil_2021.rename(columns={'julio':'07'}, inplace=True)
df_oil_2021.rename(columns={'agosto':'08'}, inplace=True)
df_oil_2021.rename(columns={'septiembre':'09'}, inplace=True)
df_oil_2021.rename(columns={'octubre':'10'}, inplace=True)
df_oil_2021.rename(columns={'noviembre':'11'}, inplace=True)
df_oil_2021.rename(columns={'diciembre':'12'}, inplace=True)

# cambiar el nombre enero a 01 de df_oil_2022
df_oil_2022.rename(columns={'enero':'01'}, inplace=True)
df_oil_2022.rename(columns={'febrero':'02'}, inplace=True)
df_oil_2022.rename(columns={'marzo':'03'}, inplace=True)
df_oil_2022.rename(columns={'abril':'04'}, inplace=True)
df_oil_2022.rename(columns={'mayo':'05'}, inplace=True)
df_oil_2022.rename(columns={'junio':'06'}, inplace=True)
df_oil_2022.rename(columns={'julio':'07'}, inplace=True)
df_oil_2022.rename(columns={'agosto':'08'}, inplace=True)
df_oil_2022.rename(columns={'septiembre':'09'}, inplace=True)
df_oil_2022.rename(columns={'octubre':'10'}, inplace=True)
df_oil_2022.rename(columns={'noviembre':'11'}, inplace=True)
df_oil_2022.rename(columns={'diciembre':'12'}, inplace=True)

# cambiar el nombre enero a 01 de df_oil_2023
df_oil_2023.rename(columns={'enero':'01'}, inplace=True)
df_oil_2023.rename(columns={'febrero':'02'}, inplace=True)
df_oil_2023.rename(columns={'marzo':'03'}, inplace=True)
df_oil_2023.rename(columns={'abril':'04'}, inplace=True)


# In[156]:


df_oil_2019.info()


# In[157]:


df_unpivoted_2014 = pd.melt(df_oil_2014, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_unpivoted_2015 = pd.melt(df_oil_2015, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_unpivoted_2016 = pd.melt(df_oil_2016, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_unpivoted_2017 = pd.melt(df_oil_2017, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_unpivoted_2018 = pd.melt(df_oil_2018, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_unpivoted_2019 = pd.melt(df_oil_2019, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_unpivoted_2020 = pd.melt(df_oil_2020, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_unpivoted_2021 = pd.melt(df_oil_2021, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_unpivoted_2022 = pd.melt(df_oil_2022, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_unpivoted_2023 = pd.melt(df_oil_2023, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')


# In[158]:


df_oil_2019


# In[159]:


df_unpivoted_2014


# In[160]:


# # Agrega ' 2014' a cada valor en la columna 'mes' y conviértelo en fecha
df_unpivoted_2014['Mes'] = df_unpivoted_2014['Mes'] + '/2014'
df_unpivoted_2014['Mes'] = pd.to_datetime(df_unpivoted_2014['Mes'], format='%m/%Y')

# # Agrega ' 2015     ' a cada valor en la columna 'mes' y conviértelo en fecha
df_unpivoted_2015['Mes'] = df_unpivoted_2015['Mes'] + '/2015'
df_unpivoted_2015['Mes'] = pd.to_datetime(df_unpivoted_2015['Mes'], format='%m/%Y')

# # Agrega ' 2016     ' a cada valor en la columna 'mes' y conviértelo en fecha
df_unpivoted_2016['Mes'] = df_unpivoted_2016['Mes'] + '/2016'
df_unpivoted_2016['Mes'] = pd.to_datetime(df_unpivoted_2016['Mes'], format='%m/%Y')

# # Agrega ' 2017     ' a cada valor en la columna 'mes' y conviértelo en fecha
df_unpivoted_2017['Mes'] = df_unpivoted_2017['Mes'] + '/2017'
df_unpivoted_2017['Mes'] = pd.to_datetime(df_unpivoted_2017['Mes'], format='%m/%Y')

# # Agrega ' 2018     ' a cada valor en la columna 'mes' y conviértelo en fecha
df_unpivoted_2018['Mes'] = df_unpivoted_2018['Mes'] + '/2018'
df_unpivoted_2018['Mes'] = pd.to_datetime(df_unpivoted_2018['Mes'], format='%m/%Y')

# # Agrega ' 2019     ' a cada valor en la columna 'mes' y conviértelo en fecha
df_unpivoted_2019['Mes'] = df_unpivoted_2019['Mes'] + '/2019'
df_unpivoted_2019['Mes'] = pd.to_datetime(df_unpivoted_2019['Mes'], format='%m/%Y')


# In[161]:


# Agrega ' 2020' a cada valor en la columna 'mes' y conviértelo en fecha
df_unpivoted_2020['Mes'] = df_unpivoted_2020['Mes'] + '/2020'
df_unpivoted_2020['Mes'] = pd.to_datetime(df_unpivoted_2020['Mes'], format='%m/%Y')

# Agrega ' 2021' a cada valor en la columna 'mes' y conviértelo en fecha
df_unpivoted_2021['Mes'] = df_unpivoted_2021['Mes'] + '/2021'
df_unpivoted_2021['Mes'] = pd.to_datetime(df_unpivoted_2021['Mes'], format='%m/%Y')

# Agrega ' 2022' a cada valor en la columna 'mes' y conviértelo en fecha
df_unpivoted_2022['Mes'] = df_unpivoted_2022['Mes'] + '/2022'
df_unpivoted_2022['Mes'] = pd.to_datetime(df_unpivoted_2022['Mes'], format='%m/%Y')

# Agrega ' 2023' a cada valor en la columna 'mes' y conviértelo en fecha
df_unpivoted_2023['Mes'] = df_unpivoted_2023['Mes'] + '/2023'
df_unpivoted_2023['Mes'] = pd.to_datetime(df_unpivoted_2023['Mes'], format='%m/%Y')


# In[162]:


df_unpivoted_2019[['Mes']]


# Preprocesamiento de datos de Gas

# In[163]:


df_gas_2018.rename(columns={'enero':'01'}, inplace=True)
df_gas_2018.rename(columns={'febrero':'02'}, inplace=True)
df_gas_2018.rename(columns={'marzo':'03'}, inplace=True)
df_gas_2018.rename(columns={'abril':'04'}, inplace=True)
df_gas_2018.rename(columns={'mayo':'05'}, inplace=True)
df_gas_2018.rename(columns={'junio':'06'}, inplace=True)
df_gas_2018.rename(columns={'julio':'07'}, inplace=True)
df_gas_2018.rename(columns={'agosto':'08'}, inplace=True)
df_gas_2018.rename(columns={'septiembre':'09'}, inplace=True)
df_gas_2018.rename(columns={'octubre':'10'}, inplace=True)
df_gas_2018.rename(columns={'noviembre':'11'}, inplace=True)
df_gas_2018.rename(columns={'diciembre':'12'}, inplace=True)

df_gas_2019.rename(columns={'enero':'01'}, inplace=True)
df_gas_2019.rename(columns={'febrero':'02'}, inplace=True)
df_gas_2019.rename(columns={'marzo':'03'}, inplace=True)
df_gas_2019.rename(columns={'abril':'04'}, inplace=True)
df_gas_2019.rename(columns={'mayo':'05'}, inplace=True)
df_gas_2019.rename(columns={'junio':'06'}, inplace=True)
df_gas_2019.rename(columns={'julio':'07'}, inplace=True)
df_gas_2019.rename(columns={'agosto':'08'}, inplace=True)
df_gas_2019.rename(columns={'septiembre':'09'}, inplace=True)
df_gas_2019.rename(columns={'octubre':'10'}, inplace=True)
df_gas_2019.rename(columns={'noviembre':'11'}, inplace=True)
df_gas_2019.rename(columns={'diciembre':'12'}, inplace=True)

df_gas_2020.rename(columns={'enero':'01'}, inplace=True)
df_gas_2020.rename(columns={'febrero':'02'}, inplace=True)
df_gas_2020.rename(columns={'marzo':'03'}, inplace=True)
df_gas_2020.rename(columns={'abril':'04'}, inplace=True)
df_gas_2020.rename(columns={'mayo':'05'}, inplace=True)
df_gas_2020.rename(columns={'junio':'06'}, inplace=True)
df_gas_2020.rename(columns={'julio':'07'}, inplace=True)
df_gas_2020.rename(columns={'agosto':'08'}, inplace=True)
df_gas_2020.rename(columns={'septiembre':'09'}, inplace=True)
df_gas_2020.rename(columns={'octubre':'10'}, inplace=True)
df_gas_2020.rename(columns={'noviembre':'11'}, inplace=True)
df_gas_2020.rename(columns={'diciembre':'12'}, inplace=True)

df_gas_2021.rename(columns={'enero':'01'}, inplace=True)
df_gas_2021.rename(columns={'febrero':'02'}, inplace=True)
df_gas_2021.rename(columns={'marzo':'03'}, inplace=True)
df_gas_2021.rename(columns={'abril':'04'}, inplace=True)
df_gas_2021.rename(columns={'mayo':'05'}, inplace=True)
df_gas_2021.rename(columns={'junio':'06'}, inplace=True)
df_gas_2021.rename(columns={'julio':'07'}, inplace=True)
df_gas_2021.rename(columns={'agosto':'08'}, inplace=True)
df_gas_2021.rename(columns={'septiembre':'09'}, inplace=True)
df_gas_2021.rename(columns={'octubre':'10'}, inplace=True)
df_gas_2021.rename(columns={'noviembre':'11'}, inplace=True)
df_gas_2021.rename(columns={'diciembre':'12'}, inplace=True)

df_gas_2022.rename(columns={'enero':'01'}, inplace=True)
df_gas_2022.rename(columns={'febrero':'02'}, inplace=True)
df_gas_2022.rename(columns={'marzo':'03'}, inplace=True)
df_gas_2022.rename(columns={'abril':'04'}, inplace=True)
df_gas_2022.rename(columns={'mayo':'05'}, inplace=True)
df_gas_2022.rename(columns={'junio':'06'}, inplace=True)
df_gas_2022.rename(columns={'julio':'07'}, inplace=True)
df_gas_2022.rename(columns={'agosto':'08'}, inplace=True)
df_gas_2022.rename(columns={'septiembre':'09'}, inplace=True)
df_gas_2022.rename(columns={'octubre':'10'}, inplace=True)
df_gas_2022.rename(columns={'noviembre':'11'}, inplace=True)
df_gas_2022.rename(columns={'diciembre':'12'}, inplace=True)

df_gas_2023.rename(columns={'enero':'01'}, inplace=True)
df_gas_2023.rename(columns={'febrero':'02'}, inplace=True)
df_gas_2023.rename(columns={'marzo':'03'}, inplace=True)
df_gas_2023.rename(columns={'abril':'04'}, inplace=True)


# In[164]:


df_gas_unpivoted_2018 = pd.melt(df_gas_2018, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_gas_unpivoted_2019 = pd.melt(df_gas_2019, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_gas_unpivoted_2020 = pd.melt(df_gas_2020, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_gas_unpivoted_2021 = pd.melt(df_gas_2021, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_gas_unpivoted_2022 = pd.melt(df_gas_2022, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')
df_gas_unpivoted_2023 = pd.melt(df_gas_2023, id_vars=['Departamento', 'Municipio', 'Operadora', 'Campo', 'Contrato'], var_name='Mes', value_name='Produccion')


# In[165]:


# # Agrega '2018' a cada valor en la columna 'mes' y conviértelo en fecha
df_gas_unpivoted_2018['Mes'] = df_gas_unpivoted_2018['Mes'] + '/2018'
df_gas_unpivoted_2018['Mes'] = pd.to_datetime(df_gas_unpivoted_2018['Mes'], format='%m/%Y')

# # Agrega '2019 a cada valor en la columna 'mes' y conviértelo en fecha
df_gas_unpivoted_2019['Mes'] = df_gas_unpivoted_2019['Mes'] + '/2019'
df_gas_unpivoted_2019['Mes'] = pd.to_datetime(df_gas_unpivoted_2019['Mes'], format='%m/%Y')

# # Agrega '2020' a cada valor en la columna 'mes' y conviértelo en fecha
df_gas_unpivoted_2020['Mes'] = df_gas_unpivoted_2020['Mes'] + '/2020'
df_gas_unpivoted_2020['Mes'] = pd.to_datetime(df_gas_unpivoted_2020['Mes'], format='%m/%Y')

# # Agrega '2021' a cada valor en la columna 'mes' y conviértelo en fecha
df_gas_unpivoted_2021['Mes'] = df_gas_unpivoted_2021['Mes'] + '/2021'
df_gas_unpivoted_2021['Mes'] = pd.to_datetime(df_gas_unpivoted_2021['Mes'], format='%m/%Y')

# # Agrega '2022' a cada valor en la columna 'mes' y conviértelo en fecha
df_gas_unpivoted_2022['Mes'] = df_gas_unpivoted_2022['Mes'] + '/2022'
df_gas_unpivoted_2022['Mes'] = pd.to_datetime(df_gas_unpivoted_2022['Mes'], format='%m/%Y')

# # Agrega '2023' a cada valor en la columna 'mes' y conviértelo en fecha
df_gas_unpivoted_2023['Mes'] = df_gas_unpivoted_2023['Mes'] + '/2023'
df_gas_unpivoted_2023['Mes'] = pd.to_datetime(df_gas_unpivoted_2023['Mes'], format='%m/%Y')


# Uniendo dataframes

# In[166]:


# concat 

df_gas= pd.concat([df_gas_unpivoted_2018, df_gas_unpivoted_2019, df_gas_unpivoted_2020, df_gas_unpivoted_2021, df_gas_unpivoted_2022, df_gas_unpivoted_2023], axis=0)


# In[167]:


# from object to float
df_gas['Produccion'] = df_gas['Produccion'].astype(float)


# In[168]:


df_gas.info()


# In[169]:


# concat four df 

df_oil = pd.concat([  df_unpivoted_2018, df_unpivoted_2019, df_unpivoted_2020, df_unpivoted_2021, df_unpivoted_2022, df_unpivoted_2023], ignore_index=True)


# In[170]:


# replace ' -   ' with 0
df_oil['Produccion'] = df_oil['Produccion'].replace(' -   ', 0)


# In[171]:


df_oil['Produccion'] = df_oil['Produccion'].astype(float)


# In[172]:


df_oil.info()

