|   [HOME](https://github.com/blessinvarkey/musings)    |   [NEXT](https://github.com/blessinvarkey/musings/blob/main/posts/cloud/aws/theory/19-01-2022-exploring-aws-services.md)    |

## Docker 

### What is a Docker? 

Docker is a platform which enables developers to package applications into containers i.e. standardized executable components combining application source code with the operating system (OS) libraries and dependencies required to run that code in any environment. Containers simplify delivery of distributed applications, and have become increasingly popular as organizations shift to cloud-native development and hybrid multicloud environments. [[1]](https://www.ibm.com/in-en/cloud/learn/docker)


<img src= "https://www.meme-arsenal.com/memes/6f421c7f32d39cac50982f0388050ca5.jpg" alt="drawing" width="300"/>

 In simple terms, Docker is a software platform that simplifies the process of **building**, **running**, **managing** and **distributing** applications. It does this by virtualizing the operating system of the computer on which it is installed and running.


 Basically, it wraps & ships the application and the dependencies to avoid. Say a scenario where the code works perfectly on the developer's system, while the ops team is unable to execute the same. 


<img src= "https://external-preview.redd.it/aR6WdUcsrEgld5xUlglgKX_0sC_NlryCPTXIHk5qdu8.jpg?auto=webp&s=5fe64dd318eec71711d87805d43def2765dd83cd" alt="drawing" width="300"/>

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

<img src= "https://miro.medium.com/max/1400/1*p8k1b2DZTQEW_yf0hYniXw.png" alt="drawing" width="600"/>



### # Example 2

In the previous example, we saw how to run a file with a print() function.

For the second example, let's consider the fashion-mnist file from my Eco-Coding project. To use codecarbon for our eco-coding project, we need to create a virtual environment using ``` 
conda ``` for easier management of dependencies and packages. 

The py (Application) file can be accessed [here](eco-fmnist.py). 

Dockerfile (containing dependencies & application):

```
ADD eco-fmnist.py .
#COPY environment.yml .
#RUN conda env create -f environment.yml
# Make RUN commands use the new environment:
#SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
FROM continuumio/miniconda3
RUN conda create -n env python=3.6
RUN bash -i shell_script.sh
#RUN echo "source activate env" > ~/.bashrc
#ENV PATH /opt/conda/envs/env/bin:$PATH
# ADD environment.yml /tmp/environment.yml
# RUN conda env create -f /tmp/environment.yml
## Pull the environment name out of the environment.yml
# RUN echo "source activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" > ~/.bashrc
# ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH

RUN conda info
RUN pip install codecarbon
RUN conda create --name codecarbon python=3.6
RUN conda activate codecarbon
RUN conda install -c codecarbon 
RUN conda install -c conda-forge codecarbon
RUN pip install numpy
RUN pip install pandas
RUN pip install matplotlib
RUN pip install scikit-learn
RUN pip install tensorflow
CMD ["python", "./eco-fmnist.py"]

```
### List the containers
```
$ docker ps 
```

### Delete the image(s)
```
$ docker rmi <IMAGE ID>
```

### List the image(s)
```
$ docker image ls 
```

### To stop a docker
On the terminal:

```
$ docker stop <name of the container>
```
OR
```
$ docker kill <ID>
```

```
$ docker pull 
```

For setting up a CICD pipeline with Github Actions, check this [repo](https://github.com/blessinvarkey/docker-github-actions)

|   [HOME](https://github.com/blessinvarkey/musings)    |   [NEXT](https://github.com/blessinvarkey/musings/blob/main/posts/cloud/aws/theory/19-01-2022-exploring-aws-services.md)    |

### Run daemon
```
$ docker container run -d
```

### Remove/Delete the container name quantum
```
$ docker container run -d --rm --name quantum --publish mode = ingress, published=18080, target = 8080 spkane/quantum-game:latest
```
rm - remove
ingress - into the container
published - 
target - targeted port
spkane/quantum-game:latest

```
docker container ls
```
### Single dash 
```
-
```

### Double dash 
```
--
```
