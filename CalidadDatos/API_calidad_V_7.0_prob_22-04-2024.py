# 1. importando los paquetes
from st_aggrid import AgGrid 
import streamlit as st
import pandas as pd 
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
from  PIL import Image
import os
import re
import numpy as np


# 1. Funciones 


# from pathlib import Path

# def convertir_a_xlsx(archivo):
#     # Determina el nombre del archivo y la extensión
#     nombre_archivo = Path(archivo.name).stem
#     extension = Path(archivo.name).suffix.lower()
    
#     # Lee el archivo según su extensión
#     if extension == '.csv':
#         datos = pd.read_csv(archivo)
#     elif extension == '.xlsx':
#         datos = pd.read_excel(archivo)
        
#     elif extension == '.txt':
#         datos = pd.read_csv(archivo, sep='\t')  # Suponiendo que el archivo .txt está separado por tabulaciones
#     else:
#         st.error("Formato de archivo no compatible. Por favor, carga un archivo CSV, Excel (xlsx) o TXT.")
#         return
    
#     # Guarda los datos en un archivo .xlsx
#     nombre_xlsx = f"{nombre_archivo}.xlsx"
#     datos.to_excel(nombre_xlsx, index=False)
    
#     st.success(f"Archivo convertido a {nombre_xlsx} correctamente.")
#     # Lee el archivo recién convertido y vuélvelo a cargar a la aplicación
#     with open(nombre_xlsx, 'rb') as f:
#         archivo_xlsx = BytesIO(f.read())
    
#     return archivo_xlsx





def generar_grafica_estrellas(calificacion):
    # Definir los símbolos para cada fracción de estrella
    simbolos = {
        0: '☆',                # Estrella vacía
        0.2: '✫',              # Estrella rellena a un quinto
        0.4: '✬',              # Estrella rellena a dos quintos
        0.6: '✭',              # Estrella rellena a tres quintos
        0.8: '✮',              # Estrella rellena a cuatro quintos
        1: '★',                # Estrella llena
    }

    # Crear el símbolo de estrella basado en la calificación
    estrellas = ''
    for i in range(5):
        fraccion_estrella = round(calificacion - i, 2)  # Redondear a 2 decimales
        if fraccion_estrella >= 1:
            estrellas += simbolos[1]
        elif fraccion_estrella > 0:
            estrellas += simbolos[min(simbolos.keys(), key=lambda x: abs(x - fraccion_estrella))]
        else:
            estrellas += simbolos[0]

    # Devolver el símbolo de estrella como HTML
    return f'{estrellas}'




def add_rating_graph(df, column_name):
    # Verificar que la columna de calificaciones exista en el DataFrame
    if column_name not in df.columns:
        st.error(f"La columna '{column_name}' no existe en el DataFrame.")
        return df
    


def cantidad_duplicados_pandas(df, eje=0, numero=False, numero_filas=30000): # Funcion de duplucados para calidad de datos 
    """
    Retorna el porcentaje/número de filas o columnas duplicadas (repetidas) en el dataframe.

    :param df: (DataFrame de pandas) El DataFrame de pandas que se va a analizar.
    :param eje: (int) {1, 0} Valor por defecto: 0. Si el valor es `1` la validación se realiza por columnas.
                Si el valor es `0` la validación se realiza por filas.
    :param numero: (bool) {True, False} Valor por defecto: False. Si el valor es `False` el resultado se expresa como
                   un cociente, si el valor es `True` el valor se expresa como una cantidad de registros (número entero).
    :param numero_filas: (int) Valor por defecto: 30000. Número de filas que tendrá cada columna cuando se verifiquen
                         los duplicados por columna (cuando 'eje = 1'). Se utiliza para agilizar el proceso de verificación
                         de duplicados de columnas, el cual puede resultar extremadamente lento para un conjunto de datos
                         con muchas filas.
    :return: (int o float) Resultado de unicidad.
    """
    if not isinstance(numero, bool): # Verificacion que sea un numero booleano 0 o 1, si pone otro saldrá el error descrito en ValueError
        raise ValueError("'numero' debe ser booleano. {True, False}.")# Describe el error al no cumplirse la condicion del if de la linea anterior
    if eje not in [0, 1]: # condicional de validacion si no es 0 y 1 da error de ValueError
        raise ValueError("'eje' solo puede ser 0 o 1.")# Describe el error al no cumplirse la condicion del if de la linea anterior

    # Proporcion (decimal) de columnas repetidas
    if eje == 1:
        if df.shape[0] <= numero_filas:
            no_unic_columnas = df.T.duplicated()
        else:
            tercio = numero_filas // 3
            mitad = numero_filas // 2

            idx_mini = pd.Index(
                list(range(tercio)) + list(range(mitad, mitad + tercio)) + list(range(numero_filas - tercio, numero_filas))
            )

            no_unic_columnas = df.iloc[idx_mini].T.duplicated()

        if numero:
            cols = no_unic_columnas.sum()
        else:
            cols = no_unic_columnas.sum() / df.shape[1]

    # Proporción de filas repetidas
    else:
        no_unic_filas = df.duplicated()
        if numero:
            cols = no_unic_filas.sum()
        else:
            cols = no_unic_filas.sum() / df.shape[0]

    return cols


def valores_faltantes_dataframe(dataframe, numero=False):
    """
    Calcula el porcentaje/número de valores faltantes de cada columna del DataFrame.

    :param dataframe: DataFrame de Pandas. El DataFrame que se va a analizar.
    :param numero: (bool) {True, False} Valor por defecto: False. Si el valor es `False` el resultado se expresa como un cociente, si el valor es `True` el valor se expresa como una cantidad de registros (número entero).
    :return: Serie de pandas con la cantidad/cociente de valores faltantes de cada columna.
    """

    if not isinstance(dataframe, pd.DataFrame):
        raise ValueError("El parámetro 'dataframe' debe ser un DataFrame de Pandas.")

    if not isinstance(numero, bool):
        raise ValueError("'numero' debe ser booleano. {True, False}.")

    if numero:
        missing_columnas = pd.isnull(dataframe).sum()
    else:
        missing_columnas = pd.isnull(dataframe).sum() / len(dataframe)

    return missing_columnas



def calificacion_completitud(dataframe):
    """
    Calcula la fracción de valores faltantes totales en todo el DataFrame, dividida por el total de registros.

    :param dataframe: DataFrame de Pandas. El DataFrame que se va a analizar.
    :return: Fracción de valores faltantes totales en el DataFrame.
    """

    if not isinstance(dataframe, pd.DataFrame):
        raise ValueError("El parámetro 'dataframe' debe ser un DataFrame de Pandas.")

    total_valores = dataframe.shape[0] * dataframe.shape[1]
    total_valores_faltantes = dataframe.isnull().sum().sum()

    fraccion_faltantes_totales = total_valores_faltantes / total_valores
    fraccion_completitud=1-fraccion_faltantes_totales

    ## cálculo de calificación de completitud

    calificacion_completitud = 5 * fraccion_completitud
    return calificacion_completitud



def tipo_columnas(df, tipoGeneral=True, tipoGeneralPython=True, tipoEspecifico=True):
    """
    Retorna el tipo de dato de cada columna del dataframe.

    :param df: DataFrame de pandas.
    :param tipoGeneral: (bool) {True, False}, valor por defecto: True.
        Incluye el tipo general de cada columna. Los tipos son: numérico,
        texto, booleano, otro.
    :param tipoGeneralPython: (bool) {True, False}, valor por defecto:
        True. Incluye el tipo general de cada columna dado por el método
        'pandas.dtypes' de Pandas
    :param tipoEspecifico: (bool) {True, False}, valor por defecto: True.
        Incluye el porcentaje de los tres tipos más frecuentes de cada
        columna. Se aplica la función nativa 'type' de Python para cada
        observación.

    :return: Dataframe de pandas con los tipos de dato de cada columna.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' debe ser un DataFrame de pandas.")

    if not isinstance(tipoGeneral, bool):
        raise ValueError("'tipoGeneral' debe ser booleano. {True, False}")

    if not isinstance(tipoGeneralPython, bool):
        raise ValueError("'tipoGeneralPython' debe ser booleano. {True, False}")

    if not isinstance(tipoEspecifico, bool):
        raise ValueError("'tipoEspecifico' debe ser booleano. {True, False}")

    if not (tipoGeneral or tipoGeneralPython or tipoEspecifico):
        raise ValueError("Al menos uno de los parámetros tipoGeneral, tipoGeneralPython o tipoEspecifico debe ser True")

    lista_nombres = df.columns
    tipos_dtypes = df.dtypes.apply(str)
    tipo_datos = dict()

    # Tipo general en español
    if tipoGeneral:
        dic_tipo = {
            "int": "Numérico",
            "float": "Numérico",
            "str": "Texto",
            "bool": "Booleano",
            "datetime64[ns]": "Fecha",
            "object": "Otro",
        }
        general = [dic_tipo.get(tipo, "Otro") for tipo in tipos_dtypes]
        tipo_datos["tipo_general"] = general

    # Tipo general de Python
    if tipoGeneralPython:
        tipo_datos["tipo_general_python"] = tipos_dtypes.tolist()

    # Tipo específico Python
    if tipoEspecifico:
        temp_list = []
        for columna in lista_nombres:
            tip = df[columna].apply(type).value_counts(normalize=True, dropna=False)

            nombre_tipo = [
                re.findall("'(.*)'", str(t))[0] for t in tip.index.tolist()
            ]

            temp_dic = {}
            for i, (nom, t) in enumerate(zip(nombre_tipo, tip)):
                key = f"tipo_especifico_{i + 1}"
                temp_dic[key] = [f"'{nom}': {round(t*100,2)}%"]
            temp_list.append(temp_dic)

        max_keys = max(temp_list, key=len).keys()
        for d in temp_list:
            for key in max_keys:
                if key not in d:
                    d[key] = [""]

            for k, v in d.items():
                if k in tipo_datos:
                    tipo_datos[k].extend(v)
                else:
                    tipo_datos[k] = v

    tips = pd.DataFrame.from_dict(tipo_datos, orient="index", columns=lista_nombres).T

    return tips


def f_calificacion_calidad_datos(df_):
    ### Dimension de completitud
    ## calificaicon completitud
    cal_complet=calificacion_completitud(df)

    ### Dimension de unicidad
    ## calificacion unicidad
    # unicidad columnas calificacion
    fraccion_dupl_col=cantidad_duplicados_pandas(df, eje=1, numero=False, numero_filas=30000)
    fraccion_unicidad_col=1-fraccion_dupl_col
    calificacion_unicid_col=fraccion_unicidad_col*5

    # calificacion unicidad filas
    fraccion_depl_filas=cantidad_duplicados_pandas(df, eje=0, numero=False, numero_filas=30000)
    fraccion_unicidad_fil= 1-fraccion_depl_filas
    calificacion_unicid_fil=fraccion_unicidad_fil*5

    #calificacion gobal unicidad
    calificacion_global_unicidad= (calificacion_unicid_fil+calificacion_unicid_col)/2
    
    ###Dimension exactitud
    df_tipos=tipo_columnas(df, tipoGeneral=True, tipoGeneralPython=True, tipoEspecifico=True)
    df_tipos['calificacion_exactitud_col'] = (df_tipos['tipo_especifico_1'].apply(lambda x: float(re.findall(r"[-+]?\d*\.\d+|\d+", x)[0])) / 100)*5
    calificacion_exactitud = df_tipos['calificacion_exactitud_col'].mean()

    ###Dimensiones minimas
        # Dimensión de precisión

    ## Calculo de minimo de filas
    minima_cant_filas = df.shape[0] / 50

    # Verificamos si minima_cant_filas es mayor que 1
    if minima_cant_filas > 1:
        frac_min_cant_filas = 1
    else:
        frac_min_cant_filas = 0

    ## Cálculo de minimo de columnas

    minima_cant_colum = df.shape[1] / 3

    # Verificamos si minima_cant_filas es mayor que 1
    if minima_cant_colum > 1:
        frac_min_cant_col = 1
    else:
        frac_min_cant_col = 0

    ## Fracción de dimensión minima

    media_fracciones_min_dim_df = (frac_min_cant_filas + frac_min_cant_col) / 2

    # Cálculo de calificación de dimensión mínima

    calificacion_dim_min_df = 5 * media_fracciones_min_dim_df

    ### Calificación total
    calificacion_total_df = (calificacion_global_unicidad + cal_complet + calificacion_exactitud + calificacion_dim_min_df) / 4

    ## creando DF de calificaciones y Total

    df_calificaciones_calidad = {'Dimensiones de calidad': ['Unicidad',
                                                            'Completitud',
                                                            'Exactitud',  
                                                            'Dimensiones minimas',
                                                            'Total'],
                                 'Calificaciones': [calificacion_global_unicidad,
                                                    cal_complet,
                                                    calificacion_exactitud,
                                                    calificacion_dim_min_df,
                                                    calificacion_total_df]
                                 }

    df_calificaciones_calidad = pd.DataFrame(df_calificaciones_calidad)

    ## agregando columna de salida gráfica de estrellas por calificación

    # Agregar una columna con las gráficas de estrellas
    df_calificaciones_calidad['Gráfica calificación'] = df_calificaciones_calidad['Calificaciones'].apply(generar_grafica_estrellas)
    #df_calificaciones_calidad = add_rating_graph(df_calificaciones_calidad, 'Calificaciones')
    # creando tabla HTML

    tabla_html = df_calificaciones_calidad.to_html(index=False)

    # Retornar un diccionario con los DataFrames y la tabla HTML
    return tabla_html, df_calificaciones_calidad





#1.1. f_cargar_archivo: función permite identificar el tipo de archivo cargado y permite leerlo.




def download_profile(profile, output_file="profile_report.html"):
    profile.to_file(output_file)
    with open(output_file, "rb") as file:
        profile_bytes = file.read()
    return profile_bytes




def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Archivo '{file_path}' eliminado correctamente.")
    except FileNotFoundError:
        print(f"El archivo '{file_path}' no existe.")
    except PermissionError:
        print(f"No tienes permiso para eliminar el archivo '{file_path}'.")
    except Exception as e:
        print(f"Se produjo un error al eliminar el archivo '{file_path}': {e}")


# Function to save profile report
def save_profile_report(profile, folder_path):
    profile_path = folder_path + "/profile_report.html"
    profile.to_file(profile_path)
    st.success(f"Profile report saved successfully at {profile_path}")

# Function to get folder path
# def get_folder_path():
#     root = tk.Tk()
#     root.withdraw()
#     folder_path = filedialog.askdirectory()
#     return folder_path
    


def f_cargar_archivo(uploaded_file): 
    # Se obtiene la extensión del archivo cargado
    extension = uploaded_file.name.split(".")[-1].lower()

    #Condicionales para verificar el tipo de archivo y cargar los datos según corresponda
    if extension == "csv":
        df = pd.read_csv(uploaded_file)
    elif extension == "xlsx" or extension == "xls":
        df = pd.read_excel(uploaded_file)
    elif extension == "txt":
        df = pd.read_csv(uploaded_file, delimiter="\t")  # Puedes ajustar el delimitador según sea necesario

    # si el archivo no se ajusta a ningún formato CSV, EXCEL O TXT se devuelve un mensaje.
    else:
        raise ValueError(f"Formato de archivo no compatible: {extension}. Solo se admiten archivos CSV, Excel o TXT.")

    return df



# 1.2.f_exportar_perfil: esta función permite exportar profiles elaborados en pandas profile en diferentes formatos como JSON, HTML y PDF
def f_exportar_perfil(profile, formato):
    # Se utiliza try-except para manejar posibles errores al exportar el perfil
    try:
        # Determinar el formato de exportación
        if formato == 'PDF':
            # Exportar el perfil a PDF
            profile.to_file("perfil_reporte.pdf")
            st.success("El perfil ha sido exportado exitosamente en formato PDF como 'perfil_reporte.pdf'")
        elif formato == 'HTML':
            # Exportar el perfil a HTML
            profile.to_file("perfil_reporte.html")
            st.success("El perfil ha sido exportado exitosamente en formato HTML como 'perfil_reporte.html'")
        elif formato == 'JSON':
            # Exportar el perfil a JSON
            profile.to_file("perfil_reporte.json")
            st.success("El perfil ha sido exportado exitosamente en formato JSON como 'perfil_reporte.json'")
        else:
            st.error("Formato de exportación no válido. Por favor, seleccione PDF, HTML o JSON.")
    except Exception as e:
        st.error(f"Ocurrió un error al exportar el perfil: {e}")


#------------------------
#2. configurando la disposición de la página
#hay mas modos como:
# Centered: Coloca el contenido en el centro de la página.
# Narrow: Un diseño más estrecho que wide.
# Wide: Un diseño amplio (el que ya conoces).
# Fullscreen: Muestra la aplicación en pantalla completa, eliminando cualquier barra de desplazamiento o interfaz del navegador.

st.set_page_config(layout='wide') 	
#------------------------
#3. Añadiendo logo
logo = Image.open(r'Min_justicia.png')	
st.sidebar.image(logo,  width=300)

#-------------------------
#4. Añadiendo expander 
# se añado un expander dentro de una sidebar, es decir la barra que se despliega de izquierda a derecha	
# Cuando se utiliza with, Python se asegura de que los recursos asociados con el expander
# se liberen adecuadamente una vez que el bloque with termine de ejecutarse. 
# En el caso de st.sidebar.expander, esto podría incluir la liberación de memoria
# o la eliminación del expander de la barra lateral.
# En resumen, el uso de with garantiza una gestión adecuada
# de los recursos asociados con el expander

st.sidebar.write("""	
    **Descripción App:**

    Mediante esta App puede hacer un análisis exploratorio de sus datos, cargando un archivo en diferentes formatos como: Excel, CSV, etc.
    La aplicación tiene dos modos, el modo mínimo que es el recomendado y
    el modo completo donde se puede corroborar correlación o interacción entre variables.
""")




#4. Agregando un titulo al estilo CSS 
     
#st.markdown(): Esta función permite mostrar texto formateado con Markdown dentro de la interfaz de Streamlit
#""": Al usar tres comillas dobles, se indica que el código dentro es un string multi-línea, lo cual es útil para escribir el código CSS sin problemas de sangrado.
#<style>: Esta etiqueta HTML inicia un bloque de código CSS que define estilos para elementos.
# .font: Esto define un clase CSS llamada "font" que aplicará los estilos definidos a cualquier elemento con dicha clase.
# font-size: 30px: Establece el tamaño de la fuente a 30 píxeles.
# font-family: 'Cooper Black': Establece la fuente a "Cooper Black", se puede personalizar por otros tipos de letra
# color: #FF9633: Define el color del texto con un código hexadecimal
#unsafe_allow_html=True dentro de la función st.markdown() tiene un rol crucial al permitir la interpretación de código HTML dentro del markdown que se está 
#mostrando. Sin esta configuración, el código HTML se interpretaría como texto plano y no se ejecutaría.

# st.markdown(""" <style> .font {                                          	
#     font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 	
#     </style> """, unsafe_allow_html=True)	

#st.markdown(): Esta función permite mostrar texto formateado con Markdown dentro de la interfaz de Streamlit
#<p>: Esta etiqueta HTML crea un párrafo.
# class="font": Aquí se asigna la clase "font" al párrafo, de forma que heredará los estilos definidos anteriormente.
# Import your data and generate a Pandas data profiling report easily...</p>: Este es el texto que se visualizará dentro del párrafo con los estilos aplicados
#unsafe_allow_html=True dentro de la función st.markdown() tiene un rol crucial al permitir la interpretación de código HTML dentro del markdown que se está 
#mostrando. Sin esta configuración, el código HTML se interpretaría como texto plano y no se ejecutaría.

# st.markdown('<p class="font">Import your data and generate a Pandas data profiling report easily...</p>', unsafe_allow_html=True)

#### EJEMPLO DE COMO PONER DOS LINEAS DE TEXTO CON DIFERENTE FORMATO
     


st.markdown("""
    <style>
        .font {
            font-size: 30px;
            font-family: 'Cooper Black';
            color: #FF9633;
        }
        .font2 {
            font-size: 30px;
            font-family: 'Cooper Black';
            color: #007BFF; /* Cambia el color aquí */
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('''
    <h1 style="color: black; font-size: 40px; font-weight: bold;">Subdirección de Gestión de Información en Justicia</h1>
    <h2 style="color: black; font-size: 30px; font-weight: bold;">Evalue la calida de los datos</h2>
''', unsafe_allow_html=True)


#5. crea un widget de carga de archivos en la aplicación Streamlit que permite a los usuarios subir un archivo CSV
# st.file_uploader: Esta función de Streamlit crea un widget de carga de archivos
# "Cargar archivo CSV:" Este es el texto que se muestra al usuario como título del widget
# type=['csv']: Esta opción indica que solo se aceptarán archivos con la extensión .csv.

#uploaded_file = st.file_uploader("Cargar archivo CSV:", type=['csv'])	

# Nota
# quitar el limite de registros hasta donde aguante. (2MM a 3 MM)
# hacer función para que lea CSV, XLSX, TXT 
# Mirar la librería del DNP que usa estrellas para mirar evaluar la calidad de los datos "LAYLA" https://github.com/ucd-dnp/leila



# def main():
#     #st.sidebar.title("Mensaje Emergente")

#     # Variable de estado para controlar la visibilidad del mensaje
#     mostrar_mensaje = st.session_state.get("mostrar_mensaje", False)

#     # Botón para mostrar u ocultar el mensaje emergente
#     if st.sidebar.button("Instructivo"):
#         mostrar_mensaje = not mostrar_mensaje

#     # Mostrar el mensaje emergente si la variable mostrar_mensaje es True
#     if mostrar_mensaje:
#         st.sidebar.info("""**Validity** refers </br> to whether data values are consistent with a defined domain of values. A domain of 
# values may be a defined set of valid values (such as in a reference table), a range of values, or 
# value that can be determined via rules. The data type, format, and precision of expected values 
# must be accounted for in defining the domain. Data may also only be valid for a specific length of 
# time, for example data that is generated from RFID (radio frequency ID) or some scientific data 
# sets. Validate data by comparing it to domain constraints. Keep in mind that data may be valid 
# (i.e., it may meet doma.""")

#     # Actualizar la variable de estado
#     st.session_state.mostrar_mensaje = mostrar_mensaje

# if __name__ == "__main__":
#     main()




def main():
    # Variable de estado para controlar la visibilidad del mensaje
    mostrar_mensaje = st.session_state.get("mostrar_mensaje", False)

    # Botón para mostrar u ocultar el mensaje emergente
    if st.sidebar.button("Instructivo"):
        mostrar_mensaje = not mostrar_mensaje

    # Mostrar el mensaje emergente si la variable mostrar_mensaje es True
    if mostrar_mensaje:
        # Obtener el mensaje actual de la barra lateral
        mensaje_actual = st.session_state.get("mensaje_actual", None)
        
        # Verificar si el mensaje actual es None o no es de tipo info
        if mensaje_actual is None or mensaje_actual["format"] != "info":
            # Cambiar el mensaje a uno en formato markdown
            st.sidebar.markdown("""
            **Validity** refers to whether data values are consistent with a defined domain of values. A domain of values may be a defined set of valid values (such as in a reference table), a range of values, or  
            value that can be determined via rules. The data type, format, and precision of expected values  
            must be accounted for in defining the domain. Data may also only be valid for a specific length of  
            time, for example data that is generated from RFID (radio frequency ID) or some scientific data  
            sets. Validate data by comparing it to domain constraints. Keep in mind that data may be valid  
            (i.e., it may meet domain constraints) but still be incorrect.
            """)
            # Actualizar la variable de estado
            st.session_state.mensaje_actual = {"format": "markdown"}
        else:
            # Mostrar el mensaje actual
            st.sidebar.info(mensaje_actual["content"])

    # Actualizar la variable de estado
    st.session_state.mostrar_mensaje = mostrar_mensaje

if __name__ == "__main__":
    main()





### alternativa para que reciba mas tipos de archivos diferentes al CSV 
uploaded_file = st.file_uploader("Cargar archivo:", type=['csv', 'xlsx', 'txt'])

# if uploaded_file is not None:
#     # Obtiene la ruta del archivo
#     ruta = uploaded_file.name
if uploaded_file is not None:	#comprueba si el usuario ha cargado un archivo
#    df=pd.read_csv(uploaded_file)	# lee el archivo en formato csv 
    df = f_cargar_archivo(uploaded_file)
#---------------- 
    
    option1=st.sidebar.radio(	
     '¿Qué columnas desea incluir en el informe?',	
     ('Todas las columnas', 'Un subconjuto de columnas'))	  # da el nombre a las opciones radio que se pongan, aqui se pone el número de n opciones que puede tomar el radio, hay que tener cuidado porque el condicional de las opciones debe llevar estos mismos nombres para que sirva
    if option1=='Todas las columnas': # como se observa en esta linea el condicional de la opcion 1 tiene el mismo nombre que en la linea de arriba, así debe ser para que funcione. 
        df=df	# n este caso, no se modifica el DataFrame df ya que se quieren analizar todas las variables del archivo
    	
    elif option1=='Un subconjuto de columnas':	# en esta linea se establece una segunda condicion para la opcion 1, recordar que se llama igual a como se dejó arriba en el boton de radio
        var_list=list(df.columns)	# se crea una lista con todas las columnas del DataFrame
        option3=st.sidebar.multiselect(	
            'Seleccione las variables que quiera incluir en el análisis',	
            var_list)	# Esta función de Streamlit crea un widget de selección múltiple dentro de la barra lateral ".sidebar" es para asignar lo que sea a una barra lateral, el ".multiselect" crea un multiselector
                        #normalmente el multiselector recibe dentro de su estructura ("label", "opciones"). el label en este caso es 'Seleccione las variables que quiera incluir en el análisis',
                        #Las opciones son var_list, que es una lista que proviene de los nombre de las columnas del df de entrada, lo cual se saca con list(df.columns)
        df=df[option3]  # esta parte es la que realmente hace que la función de seleccionar haga algo en el df, sin esto simplemente se ve en el multiselector las opciones seleccionadas sin alterar el df
                        # se observa que lo que uno escoja de la lista con el multislector va a quedar guardado en la variable option3 que a su vez en esta linea "df=df[option3]",
                        # se carga en la seleccion de columnas del df
    

    #8. Creando condicional selector selectorbox para el analisis minimo o completo que propone en los siguientes condiocionales usando AgrGrid
    
    # en el caso de option2 es importante recordar la estructura ('label',( 'opc1','opc2'))
    option2 = st.sidebar.selectbox(	
     'Choose Minimal Mode or Complete Mode',	
     ('Minimal Mode', 'Complete Mode'))	
    
    # perimer condicional que dá como resultado la ejecución de la selección de la opción 'Complete Mode'
    if option2=='Complete Mode':	
        mode='complete'	
        st.sidebar.warning('''El modo mínimo predeterminado desactiva calculos adicionales, como correlaciones y detección de filas duplicadas.
                            Cambiar al modo completo puede hacer que la aplicación génere mayor gasto computacional, depende del tamaño del conjunto de datos.''')	
    
    
    elif option2=='Minimal Mode': # si se selecciona minimal mode, en la variable mode se selecciana 'minimal	
        mode='minimal'	

#9. Se crea un objero AgGrid llamado grid_response
# grid_response: esta variable contiene información sobre la cuadrícula, incluyendo los datos actualizados por el usuario
    grid_response = AgGrid(	
        df,	# aquí va el df del cual se están domando los datos
        editable=True, #Este parámetro indica que la cuadrícula AG-Grid será editable. Esto significa que los usuarios pueden editar los valores directamente en la cuadrícula si así lo desean
        height=300, #la altura de la cuadrícula AG-Grid en píxeles
        width='100%', #Este parámetro establece el ancho de la cuadrícula AG-Grid
        )	
    updated = grid_response['data']	# extrae los datos actualizados de la cuadrícula AG-Grid
    df1 = pd.DataFrame(updated) # crea un nuevo dataframe con los datos actualizados
  
# 10. Se crea un boton con un label "Generate Report", si el usuario ejecuta le botón ejecuta el código if o el elif, todo depende de la condición que se cumpla,
# darse cuenta de la sintaxis despues de los ":"  
if st.button('Generar Reporte'):
# aplicando funcion de calificación
    
    tabla_html, df_calificaciones_calidad=f_calificacion_calidad_datos(df)
    st.write(df_calificaciones_calidad)
    #st.markdown(tabla_html, unsafe_allow_html=True)
# 10.1. primer condicional, el objetivo es hacer un analisis completo 
    # En el analisis completo hay un error porque si ud modifica los datos en este caso no se va a ver afectado el df de objeto de analisis, por eso se modificó a df1
    if mode=='complete':
        # se crea la variable profile, con el eda que saca la función ProfileReport
        # al parecer el modo complete viene por defecto en el EDA, por lo que en este bloque de código no se hace un enfasis en este parametro
        profile=ProfileReport( # ProfileReport, es una función que permite hacer un analisis exploratorio EDA  a partir de un dataframe de pandas, contiene los siguientes parámetros:
            df1, # df del que provienen los datos
            title="User uploaded table", #título del reporte
            progress_bar=True, #  Indica si se debe mostrar una barra de progreso durante la generación del reporte
            dataset={ #diccionario que proporciona metadatos sobre el dataset analizado
                "description": 'This profiling report was generated by Insights Bees',
                "copyright_holder": 'Insights Bees',
                "copyright_year": '2022'
            }) 
        st_profile_report(profile) #se utiliza para mostrar un reporte de análisis exploratorio de datos (EDA) generado por la librería pandas-profiling en la interfaz de Streamlit
                                   #De eliminarse esta línea o no correrse, simplemente la aplicación no mostrará ningún EDA, ni siquierea la progress_bar



        file = download_profile(profile, output_file="profile_report.html")

        st.download_button(
            label="Download Profile Report",
            data=file,
            file_name="profile_report.html",
            mime="text/html"
            )   
        delete_file('profile_report.html')


# 10.2 segundo condicional, el objetivos es hacer un analisis mínimo, en este tipo de analisis no se tienen en cuenta cosas como la auto correlación, simplemente es un EDA muy sencillo con diagramas de 
        #barras señalando frecuencias en los dato, datos perdidos y algunas medidas de tendencia central. 
    elif mode=='minimal':# empieza el condicional cuando es igual el boton a minimal se ejecutará el código de abajo, a continuación se describen los parametros de ProfileReport para el caso de descripcion minimal:
        profile=ProfileReport(df1, # se toma el df1, que recordando las lineas anteriores, es el df que guarda cualquier modificación hecha por el usuario en la pantalla posterior a la carga de datos
            minimal=True, #en este caso hay que especificar en el paremetro minimal True, dado que por defecto viene en complete, para que haga un EDA básico.
            title="User uploaded table", #título del reporte
            progress_bar=True, #  Indica si se debe mostrar una barra de progreso durante la generación del reporte
            dataset={ #diccionario que proporciona metadatos sobre el dataset analizado
                "description": 'This profiling report was generated by Insights Bees',
                "copyright_holder": 'Insights Bees',
                "copyright_year": '2022'
            }) 
        
        st_profile_report(profile)#se utiliza para mostrar un reporte de análisis exploratorio de datos (EDA) generado por la librería pandas-profiling en la interfaz de Streamlit
                                  #De eliminarse esta línea o no correrse, simplemente la aplicación no mostrará ningún EDA, ni siquierea la progress_bar

        file = download_profile(profile, output_file="profile_report.html")

        # incertar tabla de calificaciones
        # Leer el contenido del archivo profile_report.html
        with open("profile_report.html", "r", encoding="utf-8") as f:
            contenido_html = f.read()
        # Ubicación donde deseas insertar la tabla HTML en el archivo profile_report.html
        indice_insercion = contenido_html.find("<body>") + len("<body>")
        # Insertar la tabla HTML en el contenido HTML
        contenido_modificado = (
            contenido_html[:indice_insercion]
            + tabla_html
            + contenido_html[indice_insercion:]
            )
         
        # Escribir el contenido modificado en un nuevo archivo HTML
        with open("profile_report.html", "w", encoding="utf-8") as f:
            f.write(contenido_modificado)

        st.download_button(
            label="Download Profile Report",
            data=file,
            file_name="profile_report.html",
            mime="text/html"
            )   

        # elimina el archivo fuente
        delete_file('profile_report.html')








## 11. AGREGAR un boton de descarga con el formato final que la gente quiera.

