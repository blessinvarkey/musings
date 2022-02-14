FROM python:3.6

# Example 1
# ADD helloworld.py .
# CMD ["python", "./helloworld.py"]

# Example 2
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
