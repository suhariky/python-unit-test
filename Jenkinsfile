pipeline{
    agent{
        docker{
            image "python:latest"
            args "-u root"
        }
    }
    stages{
        stage("deps"){
            steps{
                sh "pip install -r requirements.txt"
            }
        }
        stage("coverage"){
            steps{
                sh "coverage run -m nose2"
            }
        }
	stage("reports"){
	    steps{
		sh "coverage report"
		sh "coverage html"
		sh "coverage xml"
	    }
	}
	post {        
	    success {                
		archiveArtifacts 'htmlcov/*'                
		recordCoverage(tools: [[parser: 'COBERTURA', pattern: 'coverage.xml']],                    
		    id: 'COBERTURA', name: 'COBERTURA Coverage',                    
		    sourceCodeRetention: 'EVERY_BUILD')        
	    }    
	}
    }
}
