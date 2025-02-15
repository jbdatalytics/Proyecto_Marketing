# Bank Marketing Campaign 

![BankMarketing](./assets/BankMarketing.png)

Este proyecto tiene como objetivo analizar las campañas de marketing directo realizadas por una institución bancaria portuguesa. Las campañas fueron realizadas mediante llamadas telefónicas para promocionar un depósito a plazo bancario.

## Descripción del Proyecto
El análisis busca encontrar patrones que permitan comprender qué factores influyen en la decisión de los clientes de suscribirse al depósito a plazo.

El dataset incluye información detallada sobre datos sociodemográficos, características económicas y comportamiento del cliente durante la campaña. Con esta información se ha desarrollado un análisis exploratorio de datos (EDA) y una serie de visualizaciones que nos permiten identificar los principales factores que afectan la conversión.

Al ser un dataset bastante amplio e informativo, el análisis final se basará en unas cuantas variables socio-económicas (job, marital, education, income, age, etc.), el nivel crediticio y el impacto de la duración de las llamadas en la suscripción del producto.

## Directorio

    Proyecto_Marketing/

    ├─── data_raw/
          ├── bank-additional.csv
          ├── customer-details.xlsx

    ├─── src/
          ├── sp_eda.py
          ├── sp_limpieza.py
          ├── sp_visualizacion.py
    
    ├─── data_processed/
          ├── ba_limpieza.csv
          ├── ba_transformacion.csv
          ├── cd_modificaciones.xlsx
          ├── data_merged.csv
    
    ├─── notebooks/
          ├── ba_categoricas.ipynb
          ├── ba_eda_preliminar.ipynb
          ├── ba_limpieza.ipynb
          ├── ba_numericas.ipynb
          ├── cd_eda_limpio.ipynb
          ├── data_combined.ipynb
          ├── informe_final.ipynb

    ├─── assets/
          ├── BankMarketing.png
    
    ├─── README.md

    

## Estructura de los Datos

El dataset consta de dos archivos:

Un primer archivo (bank-additional.csv) que contiene  43.000 filas y 23 columnas que brinda información sobre los clientes, sus características y los resultados de la campaña de marketing.

- **age**: Edad del cliente.
- **job**: Ocupación del cliente.
- **marital**: Estado civil del cliente.
- **education**: Nivel educativo.
- **default**: Historial de impagos (yes/no).
- **housing**: Tiene hipoteca (yes/no).
- **loan**: Tiene algún otro préstamo (yes/no).
- **contact**: Método de contacto.
- **duration**: Duración de la última llamada en segundos.
- **campaign**: Número de contactos realizados en la campaña actual.
- **pdays**: Días desde la última vez que se contactó al cliente.
- **previous**: Número de interacciones previas con el cliente.
- **poutcome**: Resultado de la campaña anterior.
- **emp.var.rate** : Tasa de variación del empleo.
- **cons.price.idx**: Índice de precios al consumidor.
- **cons.conf.idx**: Índice de confianza del consumidor.
- **euribor3m**: Tasa de interés del Euríbor a 3 meses.
- **nr.employed**: Número de empleados.
- **y**: Indica si el cliente suscribió el depósito a plazo.
- **date**: La fecha en la que se realizó la interacción con el cliente.
- **latitude**
- **longitude**
- **id**: Identificador único para cada registro.

El segundo archivo (customer-details.xlsx) contiene información adicional sobre los clientes del banco. Se encuentra dividido en 3 hojas de trabajo que se han unificado en un solo archivo de 43.170 filas y 6 columnas.

- **income** : Representa el ingreso anual del cliente en términos monetarios.
- **kidhome** : Indica el número de niños en el hogar del cliente.
- **teenhome** : Indica el número de adolescentes en el hogar del cliente.
- **Dt_Customer** : Fecha en que el cliente se convirtió en cliente del banco.
- **NumWebVisitsMonth** : Número de visitas mensuales al sitio web del banco.
- **id**: identificador único del cliente.


## Desarrollo del Proyecto

- Se realiza un primer análisis de los datos para entender su estructura.
- El archivo customer-details.xlsx no contiene nulos ni duplicados. El dataset está limpio y solo se hacen unas pequeñas normalizaciones.
- En el caso del archivo bank-additional.csv empezamos con la transformación de los datos, eliminando duplicados, agregando
nuevas columnas y normalizando los datos.
- Se continúa con el análisis descriptivo de las columnas categóricas y temporales. Se eliminan valores nulos con el método fillna.
- Se identifican y tratan valores nulos en variables clave como education, default y job.
- Se realiza el análisis descriptivo de las columnas numéricas. Se generan gráficas (boxplots) para verificar la presencia de outliers y eliminar nulos en función
de un umbral del 5%.
- Para los valores por debajo del umbral se imputa con el método fillna y las columnas con un porcentaje de nulos superior al umbral se imputan con el método iterativeimputer.
- Se convirtieron variables booleanas en formatos adecuados para el análisis (yes/no).
- Finalmente se unifican ambos archivos y se crean visualizaciones para representar patrones y tendencias clave.
- Recopilamos los insights que se han deducido del análisis.


## Conclusiones

### Factores que más influyen en la suscripción (Y = yes)

- **Edad** : Los clientes a partir de los 30 años y hasta pasados un poco los 40 muestran una mayor tasa de conversión.

- **Ocupación**: El estudio nos muestra que student (31%) y retired (25%) son las ocupaciones que más contratan el producto, sin embargo, esto está influenciado por los pocos valores que tienen respecto a la muestra total, lo que hace que unas pocas subscripciones eleven su porcentaje de conversión.

   En este caso, los trabajadores en el apartado admin, management y technician (con una mayor cantidad de datos) muestran mayor tasa de conversión.

- **Educacion** : Similar al análisis anterior, aquí se muestra a illiterate (22%) como cliente objetivo para llamar y realizar una suscripción, sin embargo, solo hay 18 muestras en este apartado.

  En este caso, university.degree (qué es el que mayor número de muestras tiene) representa la variable con mayor nivel de suscripción (13%).

- **Método de contacto**: Los gráficos nos muestran que el contacto hecho por cellular es mucho más efectivo (14,74%) respecto a los contactos hechos por telephone (5,16%) al momento de la suscripción del producto.

- **Duración de la llamada**: A medida que las llamadas aumentan en tiempo, la probabilidad de éxito es mayor. Así las llamadas que tienen una duración superior a los 10 minutos tienen un ratio de suscripción de casi el 50%.

- **Historial de impagos**: Los clientes que muestran impagos en su historial no contratan el producto en el 100% de los casos.


### Factores con menor o nulo impacto

- **Ingresos**: Se podría asumir que los clientes con niveles de ingresos medios-altos tendrían mayor probabilidad de suscribirse, sin embargo, el análisis nos muestra que no hay diferencias significativas y que el porcentaje de contratación es básicamente el mismo en todos los niveles de ingresos.

- **Estado civil**: En este caso hay una predominancia de suscripción por parte de los singles, pero no hay grandes diferencias porcentuales respecto a los otros grupos (divorced y married).

- **Hijos**: La tenencia de hijos (kidhome y teenhome) no afecta en absoluto las probabilidades de suscribir el depósito.

- **Clientes con hipoteca o préstamos**: Al igual que en el caso anterior, los clientes que ya tengan algún tipo de préstamo en vigor, no afecta en sus probabilidades de suscribir un nuevo producto.

###  Recomendaciones para futuras campañas
- **Optimizar la duración de las llamadas**: Las llamadas más largas tienen mayor tasa de conversión. Se recomienda personalizar el discurso y enfocarse en los clientes con mayor interés.

- **Segmentar clientes por edad, ocupación**: Centrarse en trabajadores a partir de los 30 años en ocupaciones admin, management y technician podría mejorar las conversiones.

- **Segmentar clientes por educación**: Concentrarse en clientes con un nivel educativo de university.degree para mejorar aun más los ratios de conversión.

## Contribuciones
Las contribuciones a este proyecto son bienvenidas. Si tienes alguna sugerencia, mejora o corrección, no dudes en ponerte en contacto o enviar tus ideas.

Cualquier tipo de contribución, ya sea código, documentación o feedback, será valorada.

¡Gracias por tu ayuda y colaboración!

## Autor
- Johnny [Github Profile](https://github.com/jbdatalytics)

