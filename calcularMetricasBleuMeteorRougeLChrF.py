import pandas as pd
from nltk.translate.meteor_score import meteor_score
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk.translate.chrf_score import corpus_chrf
from rouge_score import rouge_scorer
import nltk

# Descargar los recursos necesarios para METEOR
nltk.download('wordnet')

# Cargar el archivo de Excel
df = pd.read_excel(r"C:\Python\muestra_366_final_w.xlsx")  # Reemplaza con la ruta de tu archivo

# Función para calcular METEOR
def calculate_meteor(row):
    reference = [str(token) for token in row['docstring_tokens']]  # Convertimos a lista de strings
    candidate = row['outcome'].split()  # Tokenizar el texto generado
    return meteor_score([reference], candidate)  # Pasamos ambas como listas de strings

# Función para calcular BLEU con suavizado
def calculate_bleu(row):
    reference = [row['docstring_tokens']]  # Referencia como lista de tokens
    candidate = row['outcome'].split()  # Tokenizar el texto generado
    smoothing_function = SmoothingFunction().method1  # Usar la función de suavizado
    return sentence_bleu(reference, candidate, smoothing_function=smoothing_function)  # BLEU con suavizado

# Función para calcular ROUGE-L
def calculate_rouge_l(row):
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    reference = ' '.join(row['docstring_tokens'])  # Unimos los tokens en un string para la referencia
    candidate = row['outcome']  # Texto generado
    score = scorer.score(reference, candidate)
    return score['rougeL'].fmeasure  # Devuelve el F1-score de ROUGE-L

# Función para calcular chrF
def calculate_chrf(row):
    reference = [' '.join(row['docstring_tokens'])]  # Unimos los tokens en una sola cadena
    candidate = row['outcome']  # Texto generado
    return corpus_chrf(reference, [candidate])  # chrF a nivel de caracteres

# Aplicar las funciones a cada fila para calcular las métricas METEOR, BLEU, ROUGE-L y chrF
df['bleu'] = df.apply(calculate_bleu, axis=1)
df['meteor'] = df.apply(calculate_meteor, axis=1)
df['rouge-l'] = df.apply(calculate_rouge_l, axis=1)
df['chrf'] = df.apply(calculate_chrf, axis=1)

# Reordenar las columnas, poniendo 'bleu', 'meteor', 'rouge-l' y luego 'chrf'
column_order = ['repo', 'path', 'func_name', 'original_string', 'language', 'code', 'code_tokens', 'docstring', 
                'docstring_tokens', 'sha', 'url', 'partition', 'prompt', 'outcome', 'execution_time', 'bleu', 'meteor', 'rouge-l', 'chrf']
df = df[column_order]

# Guardar el archivo actualizado con las nuevas columnas 'bleu', 'meteor', 'rouge-l' y 'chrf'
df.to_excel(r"C:\Python\muestra_366_final_w_metrics.xlsx", index=False)  # Reemplaza con la ruta de salida

print("Cálculo de BLEU, METEOR, ROUGE-L y chrF completado y guardado en el archivo.")
