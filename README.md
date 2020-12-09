# Deploy With Docker  
This is for reference  
Deploy python web-app/project using Docker and NginX  
  
  
The directory should be like in the reference  

\root  
|\_ \main_project  
|\_\_ \modules  
|\_\_\_\_ \_\_init\_\_.py  
|\_\_ Dockerfile  
|\_\_ main.py  
|\_\_ requirement.txt  
|\_ \nginx  
|\_\_ Dockerfile  
|\_\_ nginx.conf  
|\_\_ project.conf  
|\_ docker-compose.yml  
|\_ run_docker.sh  


Finally, exec: `bash root\run_docker.sh`  
  
Note:  
 - Docker service should be always:restart to maintain all the container to run after crashing or losing power
 - Container will always re-start, hence, no need to adjust more about auto restart image
