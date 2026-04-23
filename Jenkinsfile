pipeline {
    agent any

    environment {
        SLACK_CHANNEL = '#all-qa-automation-lab'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sefit45/selenium-pytest-jenkins.git'
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                cd /d "%WORKSPACE%"
                if exist allure-results rmdir /s /q allure-results
                C:\\PythonProjects\\.venv\\Scripts\\python.exe -m pytest Tests -v --alluredir=allure-results
                '''
            }
        }
    }

    post {
        success {
            slackSend(
                channel: env.SLACK_CHANNEL,
                color: 'good',
                message: """✅ SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}
Build URL: ${env.BUILD_URL}
Allure Report: ${env.BUILD_URL}allure"""
            )
        }

        failure {
            slackSend(
                channel: env.SLACK_CHANNEL,
                color: 'danger',
                message: """❌ FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}
Build URL: ${env.BUILD_URL}
Check console output and Allure report."""
            )
        }

        unstable {
            slackSend(
                channel: env.SLACK_CHANNEL,
                color: 'warning',
                message: """⚠️ UNSTABLE: ${env.JOB_NAME} #${env.BUILD_NUMBER}
Build URL: ${env.BUILD_URL}
Allure Report: ${env.BUILD_URL}allure"""
            )
        }

        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])
        }
    }
}
