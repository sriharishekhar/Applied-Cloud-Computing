FROM python:3.8
RUN apt-get update
RUN apt-get install wget
RUN pip3 install jupyter
ARG username=sriharishekhar
ENV username $username
RUN useradd -m $username
RUN mkdir /home/$username/notebooksdock
RUN wget https://github.com/sriharishekhar/Applied-Cloud-Computing/blob/main/Codelab2/CA_Crime_Classifier_V1.ipynb -P ./home/$username/notebooks/
RUN chown $username:$username ./home/$username/notebooks/*
RUN chmod u+w ./home/$username/notebooks/*
RUN pip3 install -r ./home/$username/notebooks/Requirements.txt
RUN su $username
WORKDIR /home/${username}/notebooks/

EXPOSE 8888
ENTRYPOINT ["jupyter", "notebook","./CA_Crime_Classifier_V1.ipynb", "--ip=0.0.0.0","--allow-root"]