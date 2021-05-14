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
              sh 'git add .'
              sh 'git commit -m "Test push"'
              sh 'git push -f https://shelulia:GoodL1fe1@github.com/shelulia/myappsample.git dev --tags -f --no-verify'
              sh 'git init'
              sh 'git checkout -b PPR'
              sh 'git clone  https://shelulia:GoodL1fe1@github.com/shelulia/myappsample/PPR.git --branch dev'}}
    }
}
