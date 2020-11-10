# Verify Python Flask app
  # env FLASK_APP=hello.py flask run
  # curl http://127.0.0.1:5000/
# Build docker image
  # docker build -t rsn-webapp:0.1 .
# Run rsn app
  # docker run -p 8080:80 -t rsn-webapp:0.1

# Login to Docker Hub
# Tag the image
  # docker tag rsn-webapp:0.1 <docker-id>/rsn-webapp:0.1
# Push the image to Docker Hub
  # DOCKERHUBID=<docker-id>
  # docker push $DOCKERHUBID/rsn-webapp:0.1
