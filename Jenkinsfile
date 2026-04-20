pipeline{
    agent any
    environment{
        IMAGE_NAME="myapp"
        DOCKER_HUB_USER="afrin56"
        FULL_IMAGE="${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
    }
    stages{
        stage('checkout'){
            steps{
                echo "already checkout from git"
            }
        }
        stage('build image'){
            steps{
                sh '''
                    docker build -t $FULL_IMAGE .
                '''
            }
        }
        stage('login to docker'){
            steps{
                withCredentials([
                    usernamePassword(
                        credentialsId: "dockerhub-creds",
                        usernameVariable: "DOCKER_USER",
                        passwordVariable: "DOCKER_PASS"
                    )
                ]){
                    sh ''' 
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                     '''
                }
            }
        }
        stage('push'){
            steps{
                sh '''
                    docker push $FULL_IMAGE
                '''
            }
        }
        stage('Deploy'){
            steps{
                sh '''
                    docker stop myapp || true
                    docker rm myapp || true
                    docker run -d --name myapp -p 5000:5000 $FULL_IMAGE
                '''
            }
        }
    }
    post{
        success{
            echo "Completed"
        }
        failure{
            echo "failed"
        }
    }
}