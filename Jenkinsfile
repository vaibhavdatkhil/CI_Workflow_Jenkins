pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ci-python-app .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm ci-python-app pytest test_app.py'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f myapp || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name myapp ci-python-app'
            }
        }
    }
}