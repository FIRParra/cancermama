# Cáncer de mama

Para este análisis vamos a utilizar el dataset disponible en https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/ correspondiente al Breast Cancer Wisconsin (Diagnostic) Data Set (Datos de cáncer de seno del repositorio "UCI Machine Learning").

En estos datos los médicos han extraído características de los procedimientos de cáncer de mama, y las han anotado.

Recordemos que en este proceso un falso positivo no es tan preocupante como un falso negativo, ya que en el futuro se les hacen más pruebas a las pacientes y hay oportunidades de descubrir si estábamos en un falso positivo.

Sin embargo, un falso negativo puede llevar a que el cáncer se desarrolle sin supervisión durante más tiempo del necesario y podría llevar a daños más graves o incluso la muerte de la paciente.

Con esta directiva se procede a realizar tres modelos para escoger el que tenga un mejor acierto en la detección de los Canceres Malignos y se escogió según los resultados de los datos de prueba, ya que son los aciertos realizados sobre datos que el modelo no conocía.

Se definen tres funciones con el modelo de Machine Learning a ejecutar siendo:<br>
  modeloRegLog: función para realizar el modelo según el método de Regresión Logarítmica<br>
  modeloBagg: función para realizar el modelo según el método Bagging<br>
  modeloArbDes: función para realizar el modelo según el método de Árbol de decisión con 4 niveles<br>
cabe anotar que en la función de cada modelo se procede a guardar el modelo con su nombre acorde a las características que se ejecutan, por lo que si hago un modelado con el método de Regresión Logarítmica usando balanceo por over sampler, entonces se guardará un archivo llamado “RegLog Over Sampler.pkl”, este archivo se guardará en la misma carpeta de la aplicación.

También tiene una función para ejecutar la matriz de confusión en la que se puede enviar el título a mostrar, así como la información de clasificación de la matriz, también se puede escoger si se muestra la figura (plot) de la matriz, y por ultimo si se muestra la información de la precisión en la predicción de los tumores malignos.

Para poder hacer las pruebas con los modelos se hace previamente un balanceo de datos por varios métodos, como Over sampler, Under Sampler, SMOTE Sampler, y en cada balanceo se envía a ejecutar cada modelo, luego se recibe el porcentaje de precisión de la predicción del cáncer maligno y se selecciona el que tiene la mejor tasa de predicción.

Cuando se ejecuta la aplicación se sobre escriben los archivos de modelo guardados por lo que si al ejecutarlo encuentra un modelo que quiere conservar se recomienda copiarlo con otro nombre para que al volver a ejecutar se mantenga algún modelo que deseé guardar en particular.
