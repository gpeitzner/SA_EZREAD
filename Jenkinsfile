pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                python3 ./src/backend/autenticacion/login/test.py
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
