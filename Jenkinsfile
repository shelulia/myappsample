pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2'
                    args '-u root:root'
                }
            }
            steps {
                sh 'pip install --user pyodbc'
                sh 'python2 main.py'
            }
        }
        }
    }
