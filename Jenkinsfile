pipeline {
    // Selecting an agent to use, identified by the label
    agent {
        node {
            label 'python-agent'
        }
    }
    // Setting up what triggers this pipeline
    triggers {
        // Polling is not ideal, I'll need to learn other methods
        pollSCM '* * * * *'
    }
    // Env. variables used for notifying users of failed step
    environment {
        FAIL_STAGE = ''
        ERROR_CODE = ''
    }
    // Defining the pipeline stages
    stages {
        // Build stage
        stage('Build') {
            steps {
                // Tries to build, catches error if fails
                script{
                    try{
                        echo 'Build Stage'
                        sh '''
                        cd myapp
                        pip install -r requirements.txt
                        '''
                    } catch (err) {
                        // Throws error to the console, sets env vars for logging
                        echo "Error: ${err}"
                        FAIL_STAGE = 'Build'
                        ERROR_CODE = err
                    }
                    
                }
            }
        }
        // Test stage
        stage('Test') {
            steps {
                // Runs basic tests on app.py
                script{
                    try{
                        echo 'Test Stage'
                        sh '''
                        cd myapp
                        python3 app.py
                        python3 app.py --args=(foo,bar)
                        '''
                    } catch (err) {
                        // Throws error to the console, sets env vars for logging
                        echo "Error: ${err}"
                        FAIL_STAGE = 'Test'
                        ERROR_CODE = err
                    }
                    
                }
            }
        }
        // Delivery stage
        stage('Deliver') {
            steps {
                /* Currently just throws message to console, catches errors etc.
                   Will be updated once I know more about delivery.*/
                script{
                    try{
                        echo 'Deliver Stage'
                        sh '''
                        echo "Delivering lol"
                        '''
                    } catch (err) {
                        echo "Error: ${err}"
                        FAIL_STAGE = 'Deliver'
                        ERROR_CODE = err
                    }
                    
                }
            }
        }
    }
    // Post pipeline actions, runs this stuff after the stages
    post {
        // Always, self-explanatory
        always {
            echo 'Pipeline finished.'
        }
        // Runs on successful pipeline
        success {
            echo 'Pipeline succesfully executed.'
        }
        // Runs on pipeline failure
        failure {
            echo "Pipeline failed."
            echo "{$env.JOB_NAME} Build #{$env.BUILD_NUMBER}"
            // Just echoing this to the console, but with mail plugin can send e-mail
            echo "\n\nDummy E-Mail System"
            echo "mailto: user@example.co.uk"
            echo "subject: 'Pipeline Failed: {$env.JOB_NAME} Build #{$env.BUILD_NUMBER}'"
            echo "body: \n\n'Hello,\nJob {$env.JOB_NAME} Build #{$env.BUILD_NUMBER} has failed at the ${FAILED_STAGE} stage. More details are available on the Jenkins console ({$env.BUILD_URL}).\nThanks,\nJenkins.'"
        }
    }
}