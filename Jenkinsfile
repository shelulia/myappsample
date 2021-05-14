pipeline{
    agent any
    stages{
        stage('Test'){
            steps{
              sh 'python3 main.py'
        }
           }
        stage('Push to Git'){
            steps{
              sh 'git commit -m "Test push"'
              sh 'git push https://shelulia:GoodL1fe1@github.com/shelulia/myappsample/dev.git master'}}
    }
}
