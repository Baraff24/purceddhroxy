- Eseguire il comando "docker build" per creare l'immagine Docker, utilizzando il file Dockerfile appena creato:
`docker build -t purceddhroxy`

- Eseguire il comando "docker run" per avviare un container Docker dall'immagine appena creata (sulla porta 5000):
`docker run -p 5000:5000 purceddhroxy`