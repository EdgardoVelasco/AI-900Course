# ejecutar este comando para 
# usarlo en python pip install azure-ai-textanalytics

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

#Autenticación azure
key="1f3fb45cd598493ea9674e55dcecab6b"
endpoint= "https://pruebaenvf.cognitiveservices.azure.com/"

credencial= AzureKeyCredential(key)
cliente=TextAnalyticsClient(endpoint=endpoint, credential=credencial)

documentos=[
    "La pelicula fue muy mala no me gusto",
    "el restaurante es muy bueno y lleno de vida y actitud",
    "el restaurante no me impresinó mucho"
]

respuesta= cliente.analyze_sentiment(documents=documentos, language="es")
#print(respuesta)
resultado=[doc for doc in respuesta if not doc.is_error]

for doc in resultado:
    print("".center(30,"*"))
    print(f"Sentimiento  principal: {doc.sentiment}")
    print(f"Score positivo: {doc.confidence_scores.positive}")
    print(f"Score neutral: {doc.confidence_scores.neutral}")
    print(f"Score negativo: {doc.confidence_scores.negative}")

