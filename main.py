# main.py
# Copyright (C) [2024] [Marlon Fernando Castillo Alfaro]
#
# Este programa es software libre: puedes redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General de GNU publicada
# por la Free Software Foundation, ya sea la versión 3 de la Licencia,
# o (a tu elección) cualquier versión posterior.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. 
# Consulta los detalles en la Licencia Pública General de GNU.
#
# Deberías haber recibido una copia de la Licencia Pública General de GNU
# junto con este programa. Si no, consulta <https://www.gnu.org/licenses/>.

from openai import OpenAI
import pandas as pd
from google.cloud import storage
import os
import time

def process_excel(event, context):
    try:
        # Configurar el cliente de OpenAI utilizando la clave API del entorno
        client = OpenAI(api_key=os.getenv('adc_openai_api_key'))

        # Obtener el nombre del archivo y el nombre del bucket del evento
        file_name = event['name']
        bucket_name = event['bucket']

        # Especificar el nombre del bucket fuente y el de procesados
        BUCKET_FUENTE = 'adc-code-excel-bucket'
        BUCKET_PROCESADO = 'adc-docu-excel-bucket'

        # Verificar si el archivo ya fue procesado previamente creando un archivo de marcador
        marker_file_name = f"{file_name}.processed.marker"
        marker_bucket = storage.Client().bucket(BUCKET_FUENTE)
        marker_blob = marker_bucket.blob(marker_file_name)

        # Si el archivo de marcador ya existe, ignorar este archivo
        if marker_blob.exists():
            print(f"El archivo {file_name} ya fue procesado previamente. Saltando procesamiento.")
            return

        # Verificar si el evento proviene del bucket fuente
        print(f"Evento recibido de bucket: {bucket_name}, archivo: {file_name}")
        if bucket_name != BUCKET_FUENTE:
            print(f"Evento ignorado: el archivo proviene de {bucket_name}, no de {BUCKET_FUENTE}")
            return

        # Descargar el archivo desde Cloud Storage
        print(f"Descargando archivo: {file_name} desde el bucket: {bucket_name}")
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        blob.download_to_filename('/tmp/temp.xlsx')

        # Leer el archivo Excel con el motor especificado manualmente
        print(f"Leyendo archivo Excel: /tmp/temp.xlsx")
        df = pd.read_excel('/tmp/temp.xlsx', engine='openpyxl')  # Solución del error de formato
        print(f"Archivo Excel leído correctamente. Filas totales: {len(df)}")

        # Procesar cada fila que contenga un prompt en la columna 'prompt'
        any_processed = False
        for index, row in df.iterrows():
            code_text = row['code']
            prompt_text = row['prompt']
            outcome_text = row.get('outcome', None)

            # Si ya existe una documentación en 'outcome', saltar esta fila
            if not pd.isna(outcome_text):
                print(f"Fila {index+1} ya tiene documentación, saltando.")
                continue

            print(f"Procesando fila {index+1}/{len(df)}")
            if pd.isna(code_text) or pd.isna(prompt_text):
                print(f"Fila {index+1} sin código o sin prompt, saltando.")
                continue  # Saltar filas sin código o sin prompt

            # Crear el prompt completo combinando el código y el prompt indicado
            full_prompt = f"{prompt_text}\n\n{code_text}"

            # Imprimir el código y el prompt para control
            ##print(f"Code en fila {index+1}:\n{code_text}")
            ##print(f"Prompt en fila {index+1}:\n{prompt_text}")

            # Medir el tiempo de inicio antes de la llamada a la API
            start_time = time.time()
            try:
                # Llamar a la API de OpenAI para generar la documentación en inglés
                print(f"Realizando llamada a la API de OpenAI para la fila {index+1}")
                chat_completion = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": full_prompt}],
                    max_tokens=2048  # Puedes ajustar el número de tokens si es necesario
                )
                # Medir el tiempo de finalización después de la llamada a la API
                end_time = time.time()
                # Calcular el tiempo de ejecución
                execution_time = end_time - start_time
                # Imprimir la respuesta de la API
                outcome_text = chat_completion.choices[0].message.content.strip()
                ##print(f"API Response para fila {index+1}:\n{outcome_text}")
                print(f"Execution time para fila {index+1}: {execution_time} seconds")  # Imprimir el tiempo de ejecución
                # Guardar la respuesta en la columna 'outcome'
                df.at[index, 'outcome'] = outcome_text
                # Guardar el tiempo de ejecución en una nueva columna 'execution_time'
                df.at[index, 'execution_time'] = execution_time
                any_processed = True

            except Exception as e:
                print(f"Error procesando fila {index+1}: {e}")

        if not any_processed:
            print("No se realizó ninguna llamada a la API de OpenAI. No se guardarán cambios.")
            return

        # Guardar el archivo Excel actualizado después de procesar todas las líneas
        output_file = '/tmp/processed_' + file_name
        df.to_excel(output_file, index=False)
        print(f"Guardando archivo procesado en: {output_file}")

        # Subir el archivo procesado al nuevo bucket de documentacion generada
        processed_bucket = storage_client.bucket(BUCKET_PROCESADO)
        output_blob = processed_bucket.blob(file_name)
        output_blob.upload_from_filename(output_file)
        print(f'Documentación generada y guardada en el bucket {BUCKET_PROCESADO} con el nombre: {file_name}')

        # Actualizar el archivo en el bucket fuente
        bucket.blob(file_name).upload_from_filename(output_file)
        print(f'Archivo actualizado en el bucket fuente {BUCKET_FUENTE}')

        # Crear el archivo de marcador para evitar el reprocesamiento
        marker_blob.upload_from_string('')
        print(f'Archivo de marca de procesado creado: {marker_file_name}')

    except Exception as e:
        print(f"An error occurred: {e}")
