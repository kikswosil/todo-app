# Todo-app
This is a simple todo app i've made in flask.

## Requirements
- docker-engine

## Installation
Firstly download the app as a .zip file, or clone the repository.\
Then build a docker image:\
`docker build -t <image name> .`\
And then run the app:\
`docker run -d -p 5000:5000 <image name>` \
the `-d` flag used above is optional - it makes the docker container \
run in the background. Then open your web browser and go to:\
`http://localhost:5000/`, or `http://127.0.0.1:5000/`

## Running
To stop the app, run:\
`docker ps`\
you should see something like this:
```bash
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                       NAMES
<container id> <image name>   "gunicorn --bind 0.0…"   2 seconds ago   Up 2 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   reverent_pare
```
then simply run:\
`docker stop <container id>` \
if you want to check if it's still running \
simply run `docker ps` again
