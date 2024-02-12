FROM openfabric/tee-python-cpu:latest

RUN mkdir application
WORKDIR /application

RUN apt-get install wget -y
RUN wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q3_K_S.gguf

COPY . .
RUN poetry install -vvv --no-dev
EXPOSE 5500
CMD ["sh","start.sh"]