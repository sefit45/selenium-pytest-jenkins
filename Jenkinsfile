pipeline {
    agent any

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
        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])
        }
    }
}
