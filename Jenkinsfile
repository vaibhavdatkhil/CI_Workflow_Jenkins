pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/vaibhavdatkhil/CI_Workflow_Jenkins.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("ci-python-app")
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 ci-python-app'
            }
        }
    }
}