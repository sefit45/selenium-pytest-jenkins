pipeline {
    agent any

    environment {
        SLACK_CHANNEL = '#all-qa-automation-lab'
        PYTHON_EXE = 'C:\\PythonProjects\\.venv\\Scripts\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sefit45/selenium-pytest-jenkins.git'
            }
        }

        stage('Run Full Test Suite') {
            steps {
                bat """
                cd /d "%WORKSPACE%"
                if exist allure-results rmdir /s /q allure-results
                ${PYTHON_EXE} -m pytest Tests -v -n 2 --alluredir=allure-results --cache-clear
                """
            }
        }

        stage('Rerun Failed Tests') {
            when {
                expression { currentBuild.currentResult == 'FAILURE' }
            }
            steps {
                bat """
                cd /d "%WORKSPACE%"
                ${PYTHON_EXE} -m pytest Tests -v --alluredir=allure-results --last-failed
                """
            }
        }
    }

    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])
        }

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
Allure Report: ${env.BUILD_URL}allure
Please review console logs and failed tests."""
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
    }
}
