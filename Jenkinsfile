pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    sh 'pip3 install pyodbc'
                }
            }
            steps {
                sh 'python main.py'
            }
        }
    }
}