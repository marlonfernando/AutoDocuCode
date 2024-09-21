
# AutoDocuCode: Google Cloud Function para Procesar Archivos Excel con Documentación Automática

Este proyecto fue desarrollado como parte del trabajo de tesis para la **Maestría en Tecnologías de la Información y Comunicación** en la **Universidad de San Carlos de Guatemala**. El objetivo de **AutoDocuCode** es automatizar la **generación de documentación de código fuente** utilizando **técnicas de Prompt Engineering** con **modelos de lenguaje de gran tamaño (LLM)**, desplegando una solución basada en **Google Cloud Functions**.

## Contexto de la Tesis

La falta de documentación clara y precisa en el código fuente es uno de los mayores problemas que enfrentan los desarrolladores, lo que afecta la mantenibilidad y la calidad del software. **AutoDocuCode** propone una herramienta automatizada para generar documentación de manera eficiente y precisa utilizando la API de **OpenAI** para analizar fragmentos de código contenidos en archivos Excel.

### Objetivos del Proyecto

1. **Automatizar el proceso de documentación de código fuente** en archivos Excel utilizando una función de Google Cloud.
2. **Evaluar la calidad de la documentación generada** utilizando métricas estándar como **BLEU**, **ROUGE-L**, y **METEOR**.
3. **Integrar técnicas de Prompt Engineering** para optimizar la generación de documentación mediante **Modelos de Lenguaje de Gran Tamaño**.
4. **Implementar una solución escalable** mediante **Google Cloud Functions** y **Google Cloud Storage** para el procesamiento y almacenamiento de los resultados.

## Requisitos Previos

Antes de empezar, asegúrate de tener configurado lo siguiente:

1. **Cuenta en Google Cloud**: Deberás tener acceso a Google Cloud Platform (GCP) con permisos para crear funciones de Cloud y buckets en Google Cloud Storage.
2. **Cuenta en OpenAI**: Para generar documentación automática, necesitarás una clave de API de OpenAI.
3. **Instalación de Google Cloud SDK**: El SDK de Google Cloud te permite interactuar con GCP desde la línea de comandos. Sigue las instrucciones [aquí](https://cloud.google.com/sdk/docs/install) para instalarlo en tu máquina.

## Estructura del Proyecto

- **main.py**: Código principal de la función que maneja los eventos de Google Cloud Storage, descarga archivos Excel, los procesa y genera documentación automática.
- **requirements.txt**: Lista de las dependencias del proyecto.
- **LICENSE**: Licencia bajo la cual se distribuye este proyecto (GPL v3).
- **muestra_366_final_prompt_engineering.xlsx**: Archivo de ejemplo que puede usarse para probar el proyecto.

## Instalación Local

### Paso 1: Clonar el Repositorio

Primero, clona el repositorio en tu máquina local:

```
git clone https://github.com/tu-usuario/AutoDocuCode.git
cd AutoDocuCode
```

### Paso 2: Crear un Entorno Virtual e Instalar Dependencias

Para aislar las dependencias del proyecto, es recomendable crear un entorno virtual:

```
# Crear un entorno virtual (puedes usar virtualenv o venv)
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate  # Para Linux/Mac
# venv\Scriptsctivate  # Para Windows

# Instalar las dependencias del proyecto
pip install -r requirements.txt
```

### Paso 3: Configurar las Variables de Entorno

Configura la clave de la API de OpenAI como variable de entorno para que la función pueda acceder a ella:

```
export adc_openai_api_key="TU-CLAVE-API-OPENAI"
```

Reemplaza **TU-CLAVE-API-OPENAI** con tu clave de API real proporcionada por OpenAI.

## Configuración en Google Cloud Platform (GCP)

### Paso 4: Crear Buckets en Google Cloud Storage

En Google Cloud Console, deberás crear dos buckets de Google Cloud Storage para almacenar los archivos Excel y la documentación generada:

1. **Bucket Fuente**: Este bucket almacenará los archivos Excel originales.
2. **Bucket Procesado**: Aquí se almacenarán los archivos procesados con la documentación generada.

Accede a **Google Cloud Storage** desde la consola de Google Cloud y crea los dos buckets. Anota los nombres de ambos buckets para usarlos más adelante en la configuración de la función.

### Paso 5: Desplegar la Función en Google Cloud Functions

Ahora desplegaremos la función en **Google Cloud Functions** usando el SDK de GCP desde la línea de comandos.

```
gcloud functions deploy process_excel     --runtime python39     --trigger-resource [TU-BUCKET-FUENTE]     --trigger-event google.storage.object.finalize     --entry-point process_excel     --set-env-vars adc_openai_api_key=[TU-CLAVE-API-OPENAI]
```

Reemplaza:

- **[TU-BUCKET-FUENTE]** con el nombre de tu bucket fuente.
- **[TU-CLAVE-API-OPENAI]** con tu clave de API de OpenAI.

### Paso 6: Configurar los Permisos Correctos

Asegúrate de que el bucket fuente tenga los permisos adecuados para que la función pueda acceder a los archivos. Puedes agregar permisos en la consola de **Google Cloud** en la sección de IAM (Identidad y Gestión de Accesos).

## Probar el Proyecto con el Archivo de Ejemplo

### Paso 7: Subir el Archivo de Ejemplo

Para probar la funcionalidad, utiliza el archivo de ejemplo **muestra_366_final_prompt_engineering.xlsx** que ya está disponible. Puedes descargarlo aquí.

Sube el archivo de ejemplo al bucket fuente:

1. Accede a **Google Cloud Storage**.
2. Sube el archivo **muestra_366_final_prompt_engineering.xlsx** al bucket que configuraste como bucket fuente.

### Paso 8: Ejecución de la Función

Una vez que el archivo de ejemplo se haya subido, la función **process_excel** se ejecutará automáticamente. La función descargará el archivo Excel, generará la documentación correspondiente utilizando OpenAI, y subirá el archivo procesado al bucket procesado.

### Paso 9: Verificar el Resultado

1. Accede a tu bucket procesado en **Google Cloud Storage** y busca el archivo procesado.
2. La documentación generada por OpenAI aparecerá en la columna **outcome** del archivo Excel procesado.
3. Si el archivo fue procesado correctamente, también se creará un archivo de marcador en el bucket fuente para evitar que el archivo sea reprocesado.

## Resultados del Proyecto de Tesis

Este proyecto ha demostrado ser eficaz en la generación automática de documentación de código fuente, logrando los siguientes resultados destacados:

- Reducción del tiempo dedicado a la documentación manual.
- Generación de documentación clara y precisa a partir de fragmentos de código con el uso de modelos de lenguaje de IA.
- Opiniones positivas de desarrolladores expertos, quienes evaluaron la utilidad y coherencia de la documentación generada.
- Se evaluaron diferentes métricas como **BLEU**, **ROUGE-L**, y **METEOR**, obteniendo resultados prometedores en términos de la calidad de la documentación generada automáticamente.

## Licencia

Este proyecto está licenciado bajo la **Licencia Pública General de GNU versión 3 (GPLv3)**. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

### **Pasos para subir el archivo actualizado `README.md`:**

1. **Guarda este contenido** en tu archivo `README.md`.
2. **Sube el archivo a GitHub** usando los siguientes comandos:

   ```
   git add README.md
   git commit -m "Actualizar README con todos los pasos para replicar AutoDocuCode"
   git push origin master
   ```

