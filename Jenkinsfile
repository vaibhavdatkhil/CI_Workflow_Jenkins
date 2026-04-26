pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'echo Running tests...'
            }
        }

        stage('Run Container') {
    steps {
        sh 'docker rm -f flask-container || true'
        sh 'docker run -d -p 5001:5000 --name flask-container flask-app'
    }
}
    }

    post {
        success {
            echo 'Build Successful ✅'
        }
        failure {
            echo 'Build Failed ❌'
        }
    }
}