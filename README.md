# jenkins-101
Creating a simple pipeline with Jenkins, Python, and AWS EC2. 

## Pre-Requisites
- Jenkins Server
    - I'm running it on Docker using [devopsjourney1's docker image](https://github.com/devopsjourney1/jenkins-101/)
    - The server also needs the [EC2 plugin](https://plugins.jenkins.io/ec2/)
- GitHub repo
    - I'm using this repo
    - Python app and Jenkinsfile uploaded here
- Python app
    - I've written a simple (dead simple) script that accepts arguments
    - This script uses Python implementations of the wonderful [cowsay tool](https://pypi.org/project/cowsay/) and the ever brilliant [figlet (pyfiglet)](https://pypi.org/project/pyfiglet/).
