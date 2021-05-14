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
              sh 'git checkout -b dev'
              sh 'git config --global user.email "shelulia@gmail.com"'
              sh 'git config --global user.name "shelulia"'
              sh 'git commit -m "Test push"'
              sh 'git push https://shelulia:GoodL1fe1@github.com/shelulia/myappsample/dev.git master'}}
    }
}
