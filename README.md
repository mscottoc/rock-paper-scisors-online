# Overview

I created two versions of the same rock paper scisors program. One client-server where the client plays against the server with the server recording wins and losses and a peer-to-peer version where you play against another person.

I wanted to learn the basics of networking and thought a simple game would provide a good challenge and incentive to learn.

[Software Demo Video](https://youtu.be/_8O88MveL7)

# Network Communication

I created both a client- server version and a peer-to-peer version

They are both TCP as I utilized socket with python and the syntax is shorter for TCP. Not only was it convienient but it was also reliable. Good for my simple small messages.

The messages are strings encoded with UTF-8

# Development Environment

It was programmed using VS Code being run through the command line.

It was written in python with the socket library for networking, the random library for number generation, and the json library for storing and retrieving information from files.

# Useful Websites

{Make a list of websites that you found helpful in this project}

* [W3 Schools - Python](https://www.w3schools.com/python)
* [Tutorials Point - Sockets](https://www.tutorialspoint.com/python/python_networking.htm)

# Future Work

* Have the ptp record wins and losses
* Have ptp record who you won and loss to in each game
* Find a way to connect peers automaticaly
