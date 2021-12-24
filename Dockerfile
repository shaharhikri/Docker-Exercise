FROM ubuntu
COPY my_app.py /home/
RUN /bin/bash -c 'apt-get update'
RUN /bin/bash -c 'apt-get upgrade -y'
RUN /bin/bash -c 'apt-get install python3.9 -y'
CMD /bin/bash -c 'python3.9 /home/my_app.py'
