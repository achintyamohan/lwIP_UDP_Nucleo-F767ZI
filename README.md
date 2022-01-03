# lwIP_UDP_Nucleo-F767ZI

This repo contains a basic example of UDP communication using the lwIP stack (no RTOS) on a Nucleo-F767ZI board. The folder `CubeIDE-F767-UDP-echo/` is a STM32CubeIDE project and contains all the embedded code. 

The file `UDP_echo.py` is a basic Python script that can be used to test the functionality.

Note: The microcontroller assumes that the machine it is communicating to has a static IPv4 address of `192.168.0.11`. You can change this (and other things like the port number) in the file `main.h`. Also, make sure that there are no firewalls/anti-virus softwares blocking the messages being sent and received.
