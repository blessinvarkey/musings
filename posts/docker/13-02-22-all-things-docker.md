## Docker 

### What is a Docker? 

Docker is a platform which enables developers to package applications into containers i.e. standardized executable components combining application source code with the operating system (OS) libraries and dependencies required to run that code in any environment. Containers simplify delivery of distributed applications, and have become increasingly popular as organizations shift to cloud-native development and hybrid multicloud environments. [[1]](https://www.ibm.com/in-en/cloud/learn/docker)

![](https://www.meme-arsenal.com/memes/6f421c7f32d39cac50982f0388050ca5.jpg)


 In simple terms, Docker is a software platform that simplifies the process of **building**, **running**, **managing** and **distributing** applications. It does this by virtualizing the operating system of the computer on which it is installed and running.


 Basically, it wraps & ships the application and the dependencies to avoid say a scenario where the code works perfectly on the developer's system, while the ops team is unable to execute the same. 

![](https://external-preview.redd.it/aR6WdUcsrEgld5xUlglgKX_0sC_NlryCPTXIHk5qdu8.jpg?auto=webp&s=5fe64dd318eec71711d87805d43def2765dd83cd)

Let's look at a simple example to understand docker: 

### # Example 1

To understand the basic syntax used, let's write a simple python file named: hello-world.py. The goal of this example is to understand how to 'ship' a file containing print ("hello world").

```
#Filename hello-world.py
print('Hello World')
```

Create a Dockerfile:

```
#Filename Dockerfile
FROM python:3.8
ADD hello-world.py . 
CMD ["python", "./hello-world.py"]
```

On the terminal: 
| | |
|--|--|
| docker -v | shows the version number
| docker build -t hello . | builds the image 'hello'; -t adds the tag to the image 
| docker run hello | runs docker |

```
$ docker -v
$ docker build -t hello .
$ docker run hello
```

### # Example 2

In the previous example, we saw how to run a file with a print() function.

For the second example, let's consider the fashion-mnist file from my Eco-Coding project. To use codecarbon for our eco-coding project, we need to create a virtual environment using ``` 
conda ``` for easier management of dependencies and packages. 




