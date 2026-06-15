FROM jupyter/scipy-notebook:latest 
WORKDIR /home/jovyan/work 
COPY . . 
EXPOSE 8888 
