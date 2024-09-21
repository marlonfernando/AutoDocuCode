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

```bash
git clone https://github.com/tu-usuario/AutoDocuCode.git
cd AutoDocuCode
