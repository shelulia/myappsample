pipeline{
    agent any
    stages{
        stage('Test'){
            steps{
              sh 'isql -v -k "DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1,1433;DATABASE=TRN;UID=sa;PWD=reallyStrongPwd123" '
        }}
    }
}
