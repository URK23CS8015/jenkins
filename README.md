1. docker rm jenkins
2. docker run -d --name jenkins -u root -p 8080:8080 -p 50000:50000 -v jenkins-data:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts
3. docker exec -u 0 -it jenkins bash
4. apt update
5. apt install -y docker.io
6. usermod -aG docker jenkins
7. exit
8. docker restart jenkins
9. docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

10. open : localhost:8080