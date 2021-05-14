pipeline{
    agent any
    stages{
        stage('Running test scripts'){
            steps{
              print("Running test scripts")
              sh 'python3 main.py'
        }
           }
        stage('Create PreProd branch'){
            steps{
              sh 'git config --global user.email "shelulia@gmail.com"'
              sh 'git config --global user.name "shelulia"'
              sh 'git checkout dev'
              sh 'git checkout -b PPR'
              sh 'git push -u https://shelulia:GoodL1fe1@github.com/shelulia/myappsample.git PPR'}}
    }
}
