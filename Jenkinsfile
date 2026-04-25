pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("event-app")
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 event-app'
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