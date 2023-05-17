from transformers import ViltProcessor, ViltForQuestionAnswering
from transformers import pipeline

from PIL import Image
from io import BytesIO

from flask import Flask, request, send_file, make_response

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


#porta 5000

#definição de modelos de IA

print("carregando modelos")

image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

print("modelos carregados")

#definições de funções de inferencia

#inferencia de decricao

image = None

def descricao(imagem):
    saida = image_to_text(imagem)[0]['generated_text']
    return saida

#inferencia de pergunta

def pergunta(text):
    
    # prepare inputs
    encoding = processor(image, text, return_tensors="pt")

    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    return model.config.id2label[idx]

#definição de servidor http




@app.route('/descricao', methods=['POST'])
def description():

    global image
    data = request.data

    image = Image.open(BytesIO(data))
    #image.show()
    response = descricao(image)
    print(response)
    
    return response
            
@app.route('/pergunta', methods=['POST'])
def question():
    global image
    data = request.data            
    #image.show()
    response = pergunta(data.decode('utf-8'))
    print(response)

    return response


@app.route('/')
def index():
    return send_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,ssl_context='adhoc')#ssl_context='adhoc')



