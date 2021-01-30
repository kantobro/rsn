# How to start with Helm Charts

Install Helm
  - https://helm.sh/docs/intro/install/
Create rsn helm template
```
helm create rsn --namespace rsn
```
Update rsn helm values and Chart files
  - rsn/values.yaml
    -  Update image repository to rsn image
    - Update service type to LoadBalancer
  - rsn/Chart.yaml
    - Update appVersion
Check which Kubernetes context is used
```
  kubectl config view --minify 
```
Delete old rsn deployment and service
```
  kubectl delete deployment rsn -n rsn
  kubectl delete service rsn -n rsn
```
Install rsn helm chart
```
  helm install helm-rsn rsn/
```

