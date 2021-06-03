pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "BACKEND TEST ... "
                python3 ./src/backend/autenticacion/test.py
                python3 ./src/backend/libro/test.py
                python3 ./src/backend/orden/test.py
                python3 ./src/backend/usuario/test.py
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
