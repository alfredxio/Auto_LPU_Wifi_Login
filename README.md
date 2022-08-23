# Auto_LPU_Wifi_Login
A python based app that helps you in connecting to LPU college Wi-Fi (Hostel/ Wireless) and automatically logins with your given credentials.
Install the pyppeteer library -> pip install pyppeteer
This simple project is based on python, uses the pyppeteer and the os library. The os library helps in interacting with the operating system and connecting to desired wifi with SSID and XML configuration.
Connecting to college Wi-Fi is not the final step as we also have to login to college IP : 10.10.0.1
For that we use the pyppeteer library that is a chromium browser automation tool. It opens the IP address and automatically logs in using the provided data.

The fun part is once you enter the credentials for the first time it gets stored in a local file so from next time you dont need to enter them. Simply chose the Wi-Fi to connect and press connect. Done!

![image](https://user-images.githubusercontent.com/87885945/186269697-240fe5a2-9036-4a7d-9cad-8c01d06eb04a.png)
