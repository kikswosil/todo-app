## requirements: 
- docker-engine
- python
- pip

## download and install:
Firstly download the app as a .zip file, or clone the repository.\
Then build a docker image:\
`docker build -t <image name> .`\
And then run the app:\
`docker run -d -p 5000:5000 <image name>` \
the `-d` flag used above is optional - it makes the docker container \
run in the background. 

## stop the app:
To stop the app simply run:\
`docker ps`\
you should see something like this:\
```bash
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                       NAMES
<container id> <image name>   "gunicorn --bind 0.0…"   2 seconds ago   Up 2 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   reverent_pare
```
then simply run:\
`docker stop <container id>` \
if you want to check if it's still running \
simply run `docker ps` again
