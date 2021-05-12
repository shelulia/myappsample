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
            }
        }
        stage('Run') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
                steps {
                    sh 'python main.py'
            }
        }
    }
}
