restart: delete-worker
	kubectl scale deploy workshop-release-webserver --replicas=0
	kubectl scale deploy workshop-release-scheduler --replicas=0 
	sleep 2;
	kubectl scale deploy workshop-release-webserver --replicas=1
	kubectl scale deploy workshop-release-scheduler --replicas=1 

forward:
	kubectl port-forward svc/workshop-release-webserver 8080

context:
	kubectl config set-context --namespace=workshop --cluster=minikube --user=minikube --current

# if there are logs not showing
delete-worker: 
	kubectl delete po workshop-release-worker-0

build:
	eval $(minikube docker-env)
	docker build -t mydags:v1 -f airflow.Dockerfile .

debug:
	kubectl exec -it workshop-release-worker-0 sh

watch:
	kubectl get po -w