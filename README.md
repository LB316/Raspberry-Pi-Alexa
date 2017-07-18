# Raspberry-Pi-Alexa
This is the repository for creating a Raspberry Pi that can be controlled by the Alexa service

1.) Download and install alexa onto your raspberry pi using this service:
http://lifehacker.com/how-to-build-your-own-amazon-echo-with-a-raspberry-pi-1787726931

2.) Update Python and Install Flask-Ask using these commands:

sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python2.7-dev python-dev python-pip
sudo pip install Flask flask-ask

3.) Install && Run NGrok
Download files from here: https://ngrok.com/download
type unzip /home/pi/ngrok-stable-linux-arm.zip in home directory
sudo ./ngrok http 5000

4.) Open Python File
nano gpio_control.py

5.) Copy and paste python file from repo then run it
sudo python gpio_control.py

6.) Login/Create Amazon Alexa Account
https://developer.amazon.com/

7.) Create a new Alexa skill. 
Name of Project and Invoction name are up to your choosing.
I used "raspberry pi" as my invoction name.

8.) Copy and paste interaction schema and invoction from repo

9.) Add custom slot GPIO_CONTROL with variables on and off

10.) Go to Configuration and select HTTPS

11.) Copy the HTTPS address from the NGrok terminal.

12.) For certification you should select the second option that says:
My development endpoint is a sub-domain of a domain that has a wildcard certificate from a certificate authority

13.) Finally you can test the pins on the last page
