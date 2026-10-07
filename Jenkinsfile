pipeline {
    agent any
    environment {
        REGION = 'ap-south-1'
        ACCOUNTID = '916218009247'
        REPO = 'image-regi'
        IMG = 'cloud-image'
        REGISTRY = "${ACCOUNTID}.dkr.ecr.${REGION}.amazonaws.com"
        ECRIMAGE = "${REGISTRY}/${REPO}:latest"
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build') {
            steps { sh 'python3 -m pip install --user -r requirements.txt' }
        }
        stage('Test') {
            steps { sh 'python3 -c "import ast; ast.parse(open(\'app.py\').read())"' }
        }
        stage('Docker Build') {
            steps { sh 'docker build -t ${IMG}:latest .' }
        }
        stage('ECR Login') {
            steps {
                sh '''
                aws ecr get-login-password --region ${REGION} | docker login --username AWS --password-stdin ${REGISTRY}
                '''
            }
        }
        stage('Docker Tag') {
            steps { sh 'docker tag ${IMG}:latest ${ECRIMAGE}' }
        }
        stage('Push to ECR') {
            steps { sh 'docker push ${ECRIMAGE}' }
        }
    }
    post {
        success { echo 'Pipeline completed successfully!' }
        failure { echo 'Pipeline failed!' }
    }
}
