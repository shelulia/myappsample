pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'pyp3 install pyodbc'
            }
            steps {
                sh 'python main.py'
            }
        }
    }
}