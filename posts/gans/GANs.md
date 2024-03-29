# Generative Adversarial Networks 

## Table of contents
- What are Generative Models
- Generative vs Discriminative models
- Types of Generative Models
- Essentials of Deep Learning
- Generator
- Discriminator 

## What are Generative Models

Examples of Generative Models    
- Zebra and a horse.   
- Doodles to pictures  
- Pictures/paintings to video
- Adobe: Next gen photoshop 
- Google: Text Generation 
- Snapchat, TickTok: Image filters   
- Disney: Super resolution  

This person does not exist

### CycleGAN  
e.g. FaceApp
- Uses unsupervised image translation models
- Generating photos from paintings (artistic and realistic images)
- Object transformation/ transformation between images of horses and zebra
- Transforming human faces into different age groups
- Transforming winter and summer image 

### StyleGAN
E.g. https://thispersondoesnotexist.com/

## DiscoGAN

## IsGAN 

The GAN Zoo
https://github.com/hindupuravinash/the-gan-zoo


## Genertive vs Discriminative Models

|Generative Models | Discriminative Models|
|---|---|
|P(XY)|P(YX)|
|[Noise: 3.5, -5, 1.2 ]E, [ 'dog' ]Y->X [features: wet nose, pointy ears]|[features: wet nose, purrs] X-> Y [ 'dog'/''cat']|
|Learns to create a realistic image using noise input |Distinguishes between fake and real images to identify which one is real/fake|
|Creates fakes that look real, improves based on scores assigned by discriminator |Looks at real and fake images, makes guesses and gets feedback on whether its guess was right or wrong. |


## Types of Generative Models
- Variational Autoencoders 
- Geneartive Adversarial Networks

### Variational Autoencoders 
Encoder - Decoder
Variational Autoencoders are composed of two models that compete with each other in order to produce a good distribution over the __latent space__.

### Generative Adversarial Networks 
Geneartive Adversarial Networks are composed of two models that compete with each other in order to reach a point where realistic examples are produced by the generator.


- Essentials of Deep Learning

Before we continue, here are some quick refreshers on Machine Learning needed to implement a Generative Adversarial Network: 

- [Tensorflow](https://github.com/blessinvarkey/musings/blob/main/posts/generativeadversarialmodels/dl.md)
- Neural Networks 
- Weights 
- Cost Functions
- PyTorch 

## Discriminator
A classifier distinguishes between classes. (i.e. cat/ not cat)
Neural Network classifier: 

P (y|x)
Discriminators find the probability of class y(real or fake) given input features x

[1]Input features X -> [2] compute non linearity -> [3] (prediction Y^ vs Label Y compared with a BCE Loss. If not the same, repeat [2] with updates ) -> [4] Output Label Y 

Discriminator checks which class does the fake and real image fall into. e.g. probability: 0.85% fake, 0.15 real. 

## Generator

A generator creates examples of a class. [a different image from the class - a different cat]

[1]Input features + Noise vectors X -> [2] compute non linearity -> [3] Output Label Y 

## BCE Loss
