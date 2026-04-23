pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sefit45/selenium-pytest-jenkins.git'
            }
        }

        stage('Run Full Test Suite') {
            steps {
                bat '''
                cd /d "%WORKSPACE%"
                
                if exist allure-results rmdir /s /q allure-results
                if exist failed_tests.txt del failed_tests.txt

                C:\\PythonProjects\\.venv\\Scripts\\python.exe -m pytest Tests -v ^
                --alluredir=allure-results ^
                --last-failed-no-failures all ^
                --cache-clear || exit /b 0
                '''
            }
        }

        stage('Rerun Failed Tests') {
            steps {
                bat '''
                cd /d "%WORKSPACE%"

                C:\\PythonProjects\\.venv\\Scripts\\python.exe -m pytest Tests -v ^
                --alluredir=allure-results ^
                --last-failed || exit /b 0
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
