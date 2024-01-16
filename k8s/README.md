# Voting App with Kubernetes Deployment

> This repository contains a simple voting application (cats vs dogs) deployed using Kubernetes. The setup includes automated infrastructure provisioning, encrypted database credentials, data persistence, and automatic scaling.

## Prerequisites

Before you begin, ensure you have the following:
- Kubernetes cluster (EKS, Minikube, etc.).
- `kubectl` CLI installed and configured.

## Usage
Access the Flask app by visiting the LoadBalancer IP or URL.

## Setup instructions 

1. **to mointor the state for your application**

Create a Deployment file with two replicas of pods and with imaage "adhaammohammed/vote-task"

To Apply the Deployment:

  ```bash
    kubectl apply -f Deployment.yml  
  ```

2. **Encrypt Database Credentials**

   Create a secret file named `secrets.yml` with base64-encoded PostgreSQL username and password:

To Apply the secret:

  ```bash
    kubectl apply -f secrets.yml
  ```

3. **Persistent Data Storage**
   
    Create a Persistent Volume (PV) for PostgreSQL to create a pool and you can separate it to many PVCs in `pv.yml`:
    Create a Persistent Volume Claim (PVC) for PostgreSQL in `pvc.yml`:
    Use Sc to assign the pod to a specific PVC

To Apply the PVC:

  ```bash
    kubectl apply -f pvc.yml
  ```
  
   Modify your PostgreSQL deployment (`Statefulset_db.yml`) to use this PVC.

4. **Auto-Scaling**

   Create a Horizontal Pod Autoscaler(HPA) to scale up or scle down automatically based on load with minimun number of pods and maximum number of pods for the Flask application in `hpa.yml`:

To Apply the HPA:

  ```bash
    kubectl apply -f hpa.yml
  ```
 5. **To expose the application**
    
    Service and Ingress are resources used to expose applications to the external world or within the cluster.

    **Service**
    
    A Service in Kubernetes provides a stable endpoint (IP address and port) to access a set of Pods. Services are used to enable communication between different parts of an application and can also serve as a point of entry for external traffic. There are several types of services in Kubernetes, including ClusterIP, NodePort, and LoadBalancer.

      - CluserIP : is the default service type , it exposes the service within the cluster.
      - NodePort : exposes the service on a specific port on all nodes in the cluster , it exposes the service from outside the cluster
      - LoadBalancer : requests a cloud provider's load balancer to distribute external traffic.
   
 To Apply the service:       

   ```bash
    kubectl apply -f deplo-services.yml
   ```
    

  **Ingress**
    An Ingress in Kubernetes allows you to expose services to the external world, typically over HTTP or HTTPS.  Ingress also convert the IP address to URL.

 To Apply the Ingress:
  ```bash
    kubectl apply -f ingress.yml
  ```
### Imperative VS Declarative

In Kubernetes, the terms "imperative" and "declarative" refer to two different approaches for managing and defining the desired state of resources within the cluster.

- Imperative: using command lines such as
  
  ```bash
     kubectl get pods
     kubectl create deployment 'name of deployment' --image 'imageYouWant' --replicas 'number of pods you want' --prot 'port'
  ```
- Declarative: using yaml files

 aslo you can make a yaml files from Imperative way by redirection

 ```bash
kubectl create deployment 'name of deployment' --image 'imageYouWant' --replicas 'number of pods you want' --prot 'port' -o yaml > dep.yml
 ```
 then 
 
```bash
vim dep.yml
```
and you will show the deployment you created but in Declarative format
  
  
