pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3'
                    image 'python:2-alpine'
                    args '-u root:root'
                }
            }
            steps {
                sh 'pip3 install --user pypyodbc'
                sh 'python main.py'
            }
        }
        }
    }
