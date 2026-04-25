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

stage('Run Container') {
    steps {
        sh 'docker run -d -p 5008:5000 ci-python-app'
    }
}
    }
}