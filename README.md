# sayImage

sayImage: Ferramenta de Áudio Descrição do Ambiente para Deficientes Visuais

#Descrição do Projeto

sayImage é uma ferramenta baseada em IA que fornece áudio descrição do ambiente em tempo real para auxiliar deficientes visuais na locomoção urbana. Através de técnicas avançadas de processamento de imagem e reconhecimento de padrões, a ferramenta é capaz de identificar e descrever objetos, obstáculos e outras informações relevantes do ambiente ao redor do usuário.

#Recursos Principais

    Geração de áudio descrição em tempo real do ambiente utilizando IA
    Reconhecimento de objetos, obstáculos e elementos relevantes do ambiente urbano
    Reconhecimento de caminhada para iniciar a descrição quando o usuario parar de caminhar
    Botão para iniciar o reconhecimento de voz,onde o usuario poderá realizar perguntas sobre o ambiente capturado na imagem

#Pré-requisitos

verifique se você possui os seguintes requisitos:

    Python 3.7 ou superior instalado
    Pacotes Python listados em requirements.txt instalados
    Conexão estável com a internet

#Instalação

    Clone o repositório do ÁudioVisão para o seu ambiente local:

    git clone https://github.com/CaioLimaViana/sayImage.git

Acesse o diretório do projeto:

    cd sayImage

Instale as dependências necessárias utilizando o pip:

    (opcional) criar um ambiente virtual python

    instalar as dependencias com o comando: pip install -r requirements.txt

#Uso

    Execute o script principal do sayImage:

    python3 server.py
    
    com um dispositivo movel conectado a mesma rede acesse: https://{ip-do-computador}:8000/
    
    é possivel usar uma vpn ou outros metodos para acesso de uma rede externa

#Contribuição

Contribuições são bem-vindas! Se você quiser contribuir com o ÁudioVisão, siga os passos abaixo:

    Fork o repositório
    Crie uma branch para sua feature (git checkout -b feature/nova-feature)
    Faça commit das suas alterações (git commit -am 'Adicionar nova feature')
    Faça push para a branch (git push origin feature/nova-feature)
    Abra um Pull Request

#Autores

    Caio Lima Viana
    Ana Lidia Gomes

#Licença

Este projeto está licenciado sob a Licença MIT.
Contato

Se você tiver alguma dúvida ou sugestão em relação ao sayImage, entre em contato conosco pelo email: Caio.projectmaster@gmail.com

#modelos usados:

https://huggingface.co/dandelin/vilt-b32-finetuned-vqa

https://huggingface.co/nlpconnect/vit-gpt2-image-captioning
