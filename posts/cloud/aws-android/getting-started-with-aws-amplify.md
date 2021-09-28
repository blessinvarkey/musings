# Getting Started With AWS Amplify

### 1. Official documentation
Follow the documentation provided by AWS [first](https://docs.amplify.aws/lib/project-setup/create-application/q/platform/android). When you get a multidex error, go to step 2.


### 2. Update dependencies for multidex: 
```
android {
    compileSdkVersion 22
    buildToolsVersion "23.0.0"

         defaultConfig {
             minSdkVersion 14 //lower than 14 doesn't support multidex
             targetSdkVersion 22

             // Enabling multidex support.
             multiDexEnabled true
         }
}

dependencies {
    compile 'com.android.support:multidex:1.0.0'
}
 ```
[i.e. step 1 & 2 ](https://skillz.zendesk.com/hc/en-us/articles/215105466-Add-Multidex-to-your-Android-Application). Sync now

### 3. 
 amplify add auth
 amplify push

### 4. 
 ```
 dependencies {
    implementation 'com.amplifyframework:aws-api:1.18.0'
    implementation 'com.amplifyframework:aws-datastore:1.18.0'
    implementation 'com.amplifyframework:core:1.4.0'
    implementation 'com.amplifyframework:aws-auth-cognito:1.4.0'
}
 ```
### 5. Initialize Amplify
https://docs.amplify.aws/lib/project-setup/create-application/q/platform/android#next-steps

### 6. 
GraphQL
 ```
? Please select from one of the below mentioned services: GraphQL
? Provide API name: myAgileGQL
? Choose the default authorization type for the API Amazon Cognito User Pool
Use a Cognito user pool configured as a part of this project.
? Do you want to configure advanced settings for the GraphQL API No, I am done.
? Do you have an annotated GraphQL schema? No
 ```

