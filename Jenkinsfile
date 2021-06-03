pipeline {
    agent any

    stages {
        stage('Unit Testing') {
            steps {
                sh 'python3 ./src/backend/autenticacion/login/test.py'
                sh 'python3 ./src/backend/autenticacion/registro/test.py'
                sh 'python3 ./src/backend/usuario/crear/test.py'
                sh 'python3 ./src/backend/usuario/editar/test.py'
                sh 'python3 ./src/backend/usuario/eliminar/test.py'
                sh 'python3 ./src/backend/usuario/obtener/test.py'
                sh 'python3 ./src/backend/libro/crear/test.py'
                sh 'python3 ./src/backend/libro/editar/test.py'
                sh 'python3 ./src/backend/libro/eliminar/test.py'
                sh 'python3 ./src/backend/libro/obtener/test.py'
                sh 'python3 ./src/backend/orden/crear/test.py'
                sh 'python3 ./src/backend/orden/editar/test.py'
                sh 'python3 ./src/backend/orden/eliminar/test.py'
                sh 'python3 ./src/backend/orden/obtener/test.py'
            }
        }
        stage('Building') {
            steps {
                echo 'Building..'
            }
        }
        stage('Integration Testing') {
            steps {
                echo 'Testing....'
            }
        }
        stage('Deploying') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
