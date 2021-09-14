# DevOps:


| S. No. | Contents | Tags |
| ------------- | ------------- |------------- |  
| 1. | [Books](https://github.com/blessinvarkey/musings/blob/main/posts/devops/devops-continous-integration.md#books) |  |
| 2. | [Conferences](https://github.com/blessinvarkey/musings/blob/main/posts/devops/devops-continous-integration.md#conferences)  |  |
| 3. | [CI ToolChain](https://github.com/blessinvarkey/musings/blob/main/posts/devops/devops-continous-integration.md#ci-toolchain)|  |
| 4. | [CI Practices](https://github.com/blessinvarkey/musings/blob/main/posts/devops/devops-continous-integration.md#continous-integration-practices) |  |
| 5. | [Continuous Delivery](https://github.com/blessinvarkey/musings/blob/main/posts/devops/devops-continous-integration.md#continuous-delivery) |  |
| 6. | [Testing/ QA](https://github.com/blessinvarkey/musings/blob/main/posts/devops/devops-continous-integration.md#testing--qa) |  | 
| 7. | Websites |  |


## Books
1. DevOps Handbook by Gene Kim, Jez Humble, Patrick Debois, John Willis
2. Leading the Transformation by Tommy Mouser and Gary Gruver
3. The Phoenix Project by Gene Kim, Kevin Behr, George Spafford
4. Continuous Delivery by Jez Humble and David Farley
5. Release it! by Micheal T Nygard
6. Effective DevOps by Jennifer Davis and Ryn Daniels
7. Lean Software Development by Mary and Tom Poppendieck
8. Web Operations by John Allspaw and Jesse Robbins
9. The practice of cloud system administration by Thomas Limoncelli, Strata Chalup and Christina Hogan


## Conferences
1. Velocity]()
2. DevOps Days

## CI ToolChain

1. Version Control (Github)
2. CI System (Jenkins)
3. Build (Maven, Gulp, Packer)
4. Testing
    - Unit Testing (JUnit, Golint, Gofmt, RuboCop)
    - Integration Testing (Robot, Protractor, Cucumber, Sauce Labs, Kitchen CI, Apache, Gauntlt)
5. Artifact Repository (Artifactory, Nexus, Docker Hub, Amazon S3)
6. Deployment (Rundeck, UrbanCode ThoughtWorks, Deployinator)

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


## Continuous Delivery

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
