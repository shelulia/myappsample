pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    sh 'apt-get install -y python3-pip'
                }
            }
            steps {
                sh 'pyp3 install pyodbc'
            }
            }
            stage('Run') {
            steps {
                sh 'python main.py'
            }
        }
    }
}