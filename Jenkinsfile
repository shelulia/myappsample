
pipeline{
    agent any
    environment
   {
       GitHubUser = credentials('f985fcee-4a24-4156-a51d-2cb27b6e62c4')
   }
    stages{
        stage('Running test scripts'){
            steps{
              print("Running test scripts")
              sh 'python3 main.py'
        }
           }
        stage('Create PreProd branch'){
            steps{
              sh 'git checkout dev'
              sh 'git checkout -b PPR_${BUILD_TIMESTAMP}'
              sh 'git push -u https://$GitHubUser_USR:$GitHubUser_PSW@github.com/shelulia/myappsample.git PPR_${BUILD_TIMESTAMP}'}}
    }
}
