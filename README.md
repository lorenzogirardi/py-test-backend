# python rest api test application

Working most of the times (always) in Platform i'm usually play with the infrastructure, however sometimes to create prototype i need backends that are done for the specific purpose.  

GOALS:
 - The application must be a REST api
 - Run in kubernetes
<br/><br/>


The application is working with GET, POST, PUT, DELETE  
enouth to cover most of the usages based on rest api.  


Inside the docker path you can run easly as local docker  

```docker build --tag pytbak:0.1 .```  
```docker run -t -p 5000:5000 pytbak:0.1```  
and access on it with ```locahost:5000/api/```

instead if you want to run it in kubernetes ,  
starting from the main folder you can  apply the kubernetes folder on your environment  
```kubectl apply -f kubernetes/ ```  

```
$ kubectl  get pods -n pytbak
NAME                             READY   STATUS    RESTARTS   AGE
pytbak-stable-5dfb4fbfd4-n64kx   1/1     Running   0          40m
```

Remember to change the host in the ingress file configuration  
```
$ cat 03-ing-pytbak.yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: pytbak-ingress
  namespace: pytbak
  annotations:
    ingress.kubernetes.io/proxy-connect-timeout: "10"
    ingress.kubernetes.io/proxy-read-timeout: "30"
    ingress.kubernetes.io/proxy-send-timeout: "30"
spec:
  rules:
  - host: pytbak.ing.h4x0r3d.lan
    http:
      paths:
      - path: /
        backend:
          serviceName: pytbak-svc
          servicePort: 5000
```

*host: pytbak.ing.h4x0r3d.lan* this is my ingress dns resolution

TIPS: for ingress endpoints you can manage multiple namespace creating an A record in your DNS (as a subdomain) with a wildcard dedicated only for ingress matching the namespace and the host created

in my case i have the home dns as ```h4x0r3d.lan```  
and ```*.ing.h4x0r3d.lan``` as a record A of my kubernetes ingress  
in this way if i create a namespace *pippo* the dns that i have to call to reach it out will be *pippo.ing.4x0r3d.lan* with no change on DNS. 

