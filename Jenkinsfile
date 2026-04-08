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
                python3 cal.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
        scp -o StrictHostKeyChecking=no -i /var/lib/jenkins/key_2.pem cal.py ec2-user@ec2-13-51-170-1.eu-north-1.compute.amazonaws.com:/home/ec2-user
        '''    
            }
        }
    }
}
