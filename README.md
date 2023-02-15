- Run the "docker build" command to create the Docker image, using the Dockerfile you just created:
`docker build -t purceddhroxy .`

- Run the "docker run" command to start a Docker container from the newly created image (on port 5000):
`docker run -d --net=host purceddhroxy`
