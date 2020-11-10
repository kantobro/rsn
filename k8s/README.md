# Install and start minikube
  # https://minikube.sigs.k8s.io/docs/start/
  # minikube status

# Create rsn namespace
  # kubectl create ns rsn
# Deploy rsn app
  # DOCKERHUBID=<docker-id>
  # kubectl create deployment rsn --image=$DOCKERHUBID/rsn-webapp:0.1 -n rsn

# Expose rsn app 
  # Using NodePort
    # Create rsn service
      # kubectl expose deployment rsn --type=NodePort --port=80 -n rsn
    # Find minikube node IP
      # NODEIP=`kubectl get nodes -n rsn -o json | jq -r '.items[] | .status .addresses[] | select(.type=="InternalIP") | .address'`
      # NODEPORT=`kubectl get svc rsn -n rsn -o json | jq -r '.spec .ports[] | .nodePort'`  
    # Verify if rsn app is up
      # curl http://$NODEIP:$NODEPORT
  # Using LoadBalancer
    # Delete old rsn service
      # kubectl delete service rsn -n rsn
    # Create rsn service
      # kubectl expose deployment rsn --type=LoadBalancer --port=80 -n rsn
    # Start the tunnel
      # minikube tunnel
    # Get External IP
      # LBIP=`kubectl get service rsn -n rsn -o json | jq -r '.status.loadBalancer.ingress[].ip'`
    # Verify if rsn app is up
      # curl http://$LBIP

# AKS (Azure Kubernetes Service) with azure free account
  # Create Azure free account
  # Install azure cli https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
  # Create aks cluster using Azure GUI or "az aks create"
  # Add AKS admin or co-admin role to your account using Azure GUI or "az role assignment create"
  # Login to Azure cloud
    # az login
  # AZSUBSCRIPTION=<my_azure_subscription>
  # Get AKS credentials
    # az aks get-credentials --name rsn-aks --resource-group rsn-rg --subscription $AZSUBSCRIPTION
  # Switch to AKS kubernetes context
    # kubectl config use-context rsn-aks
  # Switch to namespace rsn
    # kubectl config set-context --current --namespace rsn
  # Create rsn namespace
    # kubectl create ns rsn
  # Create rsn deployment in AKS
    # kubectl create -f rsn-deployment.yaml
  # Create rsn service in AKS
    # kubectl create -f rsn-service.yaml
  # Get service public IP
    # kubectl describe service rsn -n rsn
