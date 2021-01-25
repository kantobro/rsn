# Verify Python Flask app
  # env FLASK_APP=hello.py flask run
  # curl http://127.0.0.1:5000/
# Build docker image
  # docker build -t rsn-webapp:0.1 .
# Run rsn app
  # docker run -p 8080:80 -t rsn-webapp:0.1

# Login to Docker Hub
# Tag the image
  # DOCKERHUBID=<docker-id>
  # docker tag rsn-webapp:0.1 $DOCKERHUBID/rsn-webapp:0.1
# Push the image to Docker Hub
  # docker push $DOCKERHUBID/rsn-webapp:0.1
