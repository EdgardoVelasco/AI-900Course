from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

'''
1. Region: eastus
2. Key: 
3. endpoint: 
'''

region= "eastus"
key= "<key computer vision>"
endpoint="https://"+region+".api.cognitive.microsoft.com/"

#autenticación
credenciales=CognitiveServicesCredentials(key)
cliente=ComputerVisionClient(
    endpoint=endpoint,
    credentials=credenciales
)

#Analizar una imagen
url="https://storageenvf.blob.core.windows.net/clase/Analysis_6.jpg"
analisis= cliente.analyze_image(url, visual_features=[VisualFeatureTypes.faces])

for faces in analisis.faces:
    print(faces)







