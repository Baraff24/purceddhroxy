- Run the "docker build" command to create the Docker image, using the Dockerfile you just created:
`docker-compose build -t purceddhroxy .`

- Run the "docker run" command to start a Docker container from the newly created image (on port 5000):
`docker-compose run -d --net=host purceddhroxy`

- Run the "docker ps" command to see the running container:
`docker-compose ps`

- Run the "docker stop" command to stop the running container:
`docker-compose stop`

- Run the Docker Compose file using the docker-compose up command:
`docker-compose up`
