pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: [
                'smoke',
                'regression',
                'api',
                'ui',
                'db',
                'e2e',
                'all'
            ],
            description: 'Select which test suite to execute'
        )
    }

    environment {
        SLACK_CHANNEL = '#all-qa-automation-lab'
        PYTHON_EXE = 'C:\\PythonProjects\\.venv\\Scripts\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sefit45/selenium-pytest-jenkins.git'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat '''
                    cd /d "%WORKSPACE%"
                    if exist allure-results rmdir /s /q allure-results
                    '''

                    def pytestCommand = ""

                    if (params.TEST_SUITE == "all") {
                        pytestCommand = "%PYTHON_EXE% -m pytest Tests -v -n 2 --alluredir=allure-results --cache-clear"
                    } else {
                        pytestCommand = "%PYTHON_EXE% -m pytest Tests -v -m ${params.TEST_SUITE} -n 2 --alluredir=allure-results --cache-clear"
                    }

                    echo "Running: ${pytestCommand}"

                    def firstRunStatus = bat(
                        script: """
                        cd /d "%WORKSPACE%"
                        ${pytestCommand}
                        """,
                        returnStatus: true
                    )

                    if (firstRunStatus != 0) {
                        echo 'Some tests failed. Running failed tests again...'

                        def rerunStatus = bat(
                            script: '''
                            cd /d "%WORKSPACE%"
                            %PYTHON_EXE% -m pytest Tests -v --lf --alluredir=allure-results
                            ''',
                            returnStatus: true
                        )

                        if (rerunStatus != 0) {
                            error('Tests failed after rerun')
                        }
                    }
                }
            }
        }

        stage('Generate Test Summary') {
            steps {
                bat '''
                cd /d "%WORKSPACE%"
                %PYTHON_EXE% utils\\print_summary.py
                '''
            }
        }

        stage('Generate Executive QA Dashboard') {
            steps {
                bat '''
                cd /d "%WORKSPACE%"
                %PYTHON_EXE% utils\\executive_report.py
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

            archiveArtifacts artifacts: 'executive_qa_dashboard.html',
                allowEmptyArchive: true
        }

        success {
            slackSend(
                channel: "${SLACK_CHANNEL}",
                color: 'good',
                message: """✅ SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}

Suite Executed:
${params.TEST_SUITE}

Build URL:
${env.BUILD_URL}

Allure Report:
${env.BUILD_URL}allure

Executive QA Dashboard:
${env.BUILD_URL}artifact/executive_qa_dashboard.html

Execution completed successfully."""
            )
        }

        failure {
            slackSend(
                channel: "${SLACK_CHANNEL}",
                color: 'danger',
                message: """❌ FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}

Suite Executed:
${params.TEST_SUITE}

Build URL:
${env.BUILD_URL}

Allure Report:
${env.BUILD_URL}allure

Executive QA Dashboard:
${env.BUILD_URL}artifact/executive_qa_dashboard.html

Tests failed after rerun.
Check Jenkins + Allure report."""
            )
        }
    }
}