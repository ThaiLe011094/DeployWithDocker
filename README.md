# Deploy With Docker  
This is for reference  
Deploy python web-app/project using Docker and NginX  
  
  
The directory should be like in the reference  

\root  
...\main_project  
... ... \modules  
... ... ... \_\_init\_\_.py  
... ... Dockerfile  
... ... main.py  
... ... requirement.txt  
... \nginx  
... ... Dockerfile  
... ... nginx.conf  
... ... project.conf  
... docker-compose.yml  
... run_docker.sh  


Finally, exec: `bash root\run_docker.sh`  
  
Note:  
 - Docker service should be always:restart to maintain all the container to run after crashing or losing power
 - Container will always re-start, hence, no need to adjust more about auto restart image
