IMAGE_NAME="im-tp4"
DOCKERFILE_PATH="Dockerfile1"

echo "Construction de l'image Docker avec le nom: $IMAGE_NAME"
docker build -t $IMAGE_NAME -f $DOCKERFILE_PATH .

DEBIAN_SIZE=$(docker images debian:11 --format "{{.Size}}")
TP4_SIZE=$(docker images $IMAGE_NAME --format "{{.Size}}")

# Afficher la taille des images
echo "Taille de l'image Debian 11: $DEBIAN_SIZE"
echo "Taille de l'image $IMAGE_NAME: $TP4_SIZE"
