#!/bin/bash

# (a) Construire l'image basée sur le Dockerfile en la nommant im-nginx-lb
docker build -t im-nginx-lb .

# (b) Créer deux sous-dossiers shared1 et shared2
mkdir -p shared1 shared2

# (c) Y placer deux fichiers index.html contenant une ligne
echo "<h1>Hello 1</h1>" > shared1/index.html
echo "<h1>Hello 2</h1>" > shared2/index.html

# (d) Lancer deux conteneurs basés sur l'image nginx
docker run -d --name nginx1 -p 81:80 -v "$(pwd)/shared1:/usr/share/nginx/html" nginx:latest
docker run -d --name nginx2 -p 82:80 -v "$(pwd)/shared2:/usr/share/nginx/html" nginx:latest

# (e) Lancer un conteneur basé sur l'image im-nginx-lb
docker run -d --name nginx-lb -p 83:80 im-nginx-lb

