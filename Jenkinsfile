pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/2025sl93087/labsheet1-2025sl93087.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo Build Stage'
            }
        }

        stage('Test') {
            steps {
                sh '''
                python3 calculator.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo Deploy Stage'
            }
        }
    }
}
