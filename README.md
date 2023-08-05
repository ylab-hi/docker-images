# docker-images
docker-images

## Multi-architectural images  

Create new builder 
```
docker buildx create --name mybuilder --use
```
and switch to it 
```
docker buildx use mybuilder
```
Then build the dockerfile 
```
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t username/demo:latest --push .
```
