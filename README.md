## Exercise Instructions
Create an image for a docker container with the following requirements:
Running a container from this image will print the following text to the standard output “My container is online!”,
print the first 50 members of the Fibonacci sequence and exit.
You can use either bash scripts / commands or create a small application (in any technology) and run it from the docker container.

## Solution Run Instructions
If you haven't installed docker:
Install docker desktop and login inside the app with your docker id and password
(if you don't have docker user - create one in https://hub.docker.com/ ).

Download the files: 'Dockerfile', ' my_app.py' 
and store them in any directory you wish (Starting from now this directory will be called '~/docker_directory/' ).
IMPORTANT: The files have to be stored in the same directory!


From PowerShell\terminal run the following commands:
(If you run in Windows open the PowerShell as administrator, 
   else if you running in Linux run 'sudo ' before every command).
```sh
cd ~/docker_directory/
docker build -t my-ubuntu-image .
docker run -it my-ubuntu-image
```
Congratulations! You're done.
For running again you will only need to run the third command (since the image is already stored locally on your computer).
