pipeline {
    agent {
        docker {
            image 'python:latest'
        }
    }
    
    stages {
        stage("install deps") {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage("test") {
            steps {
                sh 'python -m nose2'
            }
        }
    }
}