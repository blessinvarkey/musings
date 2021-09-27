# DevOps: 

## CI ToolChain

1. Version Control (Github)
2. CI System (Jenkins)
3. Build (Maven, Gulp, Packer)
4. Unit Testing (JUnit, Golint, Gofmt, RuboCop)
5. Integration Testing (Robot, Protractor, Cucumber, Sauce Labs, Kitchen CI, Apache, Gauntlt)
6. Artifact Repository (Artifactory, Nexus, Docker Hub, Amazon S3)
7. Deployment (Rundeck, UrbanCode ThoughtWorks, Deployinator)

## Continous Integration Practices

__Code -> Build -> Unit Tests -> Code Validation -> Packaging -> Artifact__

1. All build should pass the coffee test (less than 5 minutes)
2. Commit really small bits. 
3. Don't leave the build broken.
4. Use a trunk based development flow
    - No long running branches
    - Multiple commits each day 
    - Ensures code is reviewed and checked 
5. Don't allow flaky tests, fix them! 
6. The build should return a status, a log and an artifact 


## Continous Delivary 

__Code -> VCS-> CI System creates build -> Artifact added to central repo (Staging -> Testing ) -> Production__

1. Only build artifacts once. 
2. Artifacts should be immutable: Trust between teams & Auditability  
3. Staging should be a copy of production.
4. Stop deploys if a previous step fails.
5. Deployments should be [idempotent](https://en.wikipedia.org/wiki/Idempotence).

## Testing | QA
1. Unit Testing 
2. Code Hygiene
3. Integration Testing
4. TDD, BDD, ATDD
    - Test Driven Development
    - Behaviour Driven Development
    - Acceptance Test Driven Development 
6. Infrastructure Testing
7. Performance Testing
8. Security Testing
9. Local Testing (Vagrant, Otto, Docker Compose)


