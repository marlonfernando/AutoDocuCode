# Informe Final de Tesis - Generación Automática de Documentación de Código

## Resumen

Este informe presenta el desarrollo de una herramienta automatizada para la **generación de documentación de código fuente** utilizando **técnicas avanzadas de Prompt Engineering** e **inteligencia artificial (IA)**, implementado en **Google Cloud Platform (GCP)**. La documentación es generada automáticamente para fragmentos de código en **Python** mediante el uso de la **API de OpenAI**.

El estudio aborda la selección de fragmentos de código del corpus de **CodeSearchNet**, la implementación técnica de la herramienta, la evaluación de los resultados, y las opiniones de desarrolladores sobre la calidad y utilidad de la documentación generada automáticamente.

## Introducción

El objetivo de este trabajo es abordar el problema de la **falta de documentación en el código fuente** y proponer una solución que utilice modelos de lenguaje de gran tamaño (**LLMs**). Este enfoque permite que los desarrolladores ahorren tiempo en la creación de documentación, mejorando la mantenibilidad y claridad del código.

## Metodología

- **Selección del corpus**: Se utilizaron fragmentos de código **Python** extraídos de **CodeSearchNet**, un corpus reconocido por su diversidad y calidad en repositorios de código.
- **Proceso de muestreo**: Se seleccionó una muestra representativa de **366 fragmentos de código**, asegurando la presencia de docstrings estandarizados.
- **Generación de documentación**: La herramienta se implementó en **GCP**, utilizando **Google Cloud Functions** para la integración con la **API de OpenAI** y automatizando la generación de documentación basada en prompts predefinidos.

## Resultados

Los resultados muestran que la herramienta puede generar documentación útil y coherente de manera automática. Algunos de los puntos destacados incluyen:

- Reducción del tiempo dedicado a la documentación.
- La calidad de la documentación fue evaluada mediante las métricas **BLEU**, **ROUGE-L**, y **METEOR**.
- Opiniones de desarrolladores expertos sobre la utilidad de los comentarios generados automáticamente.

## Conclusiones

- La documentación automática de código fuente es una solución efectiva para proyectos con grandes cantidades de código.
- El uso de técnicas de **Prompt Engineering** y **modelos de lenguaje como GPT-4** pueden ofrecer una alternativa viable a la documentación manual.

## Recomendaciones

- Se sugiere continuar mejorando los prompts para incrementar la precisión de la documentación generada.
- Ampliar la herramienta a otros lenguajes de programación.
- Realizar estudios adicionales que incluyan más fragmentos de código para validar la generalización de los resultados.

## Referencias

- OpenAI API Documentation.
- CodeSearchNet Corpus.
- Google Cloud Platform Documentation.

