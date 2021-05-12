pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3'
                    args '-u root:root'
                }
            }
            steps {
                sh 'pip3 install --user pypyodbc'
                sh 'main.py'
            }
        }
        }
    }
