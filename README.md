# Water My Plants Doing??

## Introduction
This was a little project I put together to help monitor a couple of my house plants' soil moisture content. One of the more difficult parts of having house plants is the guessing game that comes with knowing when to water them. I have overwatered my fair share of plants, and decided to use my knowledge. 

## Hardware Requirements
The hardware requirements for this project, along with links, are below:
- 1 x [Raspberry Pi Zero](https://www.adafruit.com/product/3708) 
- 1 x [Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor](https://www.adafruit.com/product/4026)
- 1 x [JST PH 4-Pin to Female Socket Cable](https://www.adafruit.com/product/3950)

You will also need to buy the MicroSD card and power brick for the Pi, which can also be found on Adafruit or a related site.

## Usage
If you're interested in quickly getting this project up and running, I recommend [this tutorial from Medium](https://medium.com/initial-state/how-to-use-a-soil-moisture-sensor-to-keep-your-plants-alive-51a2294b88e). It will help you get Python 3.X onto your Raspberry Pi, as well as hook up the moisture sensor to start getting temperature/moisture readings.

After the Pi and soil sensor are set up, you can simply clone this repo onto your local machine. On the command line, cd to the cloned directory and type in the below line to download all dependencies for this project:

```
pip install -r /requirements.txt
```

NOTE: The dependecies will likely be out of date, so please pay attention to later dependencies already installed on your machine.

## Project Challenges and Obstacles
This project was my first foray into combining my mechanical engineering degree with the skills I'm currently learning in my computer science degree. The largest problems for me, both to solve and implement, were:
- Finding a way to have the Pi read and then write the sensor data to *somewhere*
- Accessing the *somewhere* that my Pi would upload the sensor data to

In the end, I was able to figure things out very well, and currently now have the Pi reading sensor data for both of my plants at midnight and noon PST.

## Conclusion and Takeaway
Overall, I really enjoyed this project, both as a learning experience and as an actual tool I will utilize in my life. It gave me a lot of confidence working with the Raspberry Pi, and gives me some ideas for future projects that I can't wait to get working on.
