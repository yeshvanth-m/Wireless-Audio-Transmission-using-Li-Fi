# Wireless Audio Transmission using Li-Fi

## Introduction to Li-Fi
Li-Fi (also written as LiFi) acronym for Light Fidelity is a wireless communication technology which utilizes light to transmit data and position between devices. 
It is capable of transmitting data at high speeds over the visible light, ultraviolet, and infrared spectrums. In its present state, only LED lamps can be used for the transmission of data in visible light. In terms of its end use, the technology is similar to Wi-Fi — the key technical difference being that Wi-Fi uses radio frequency to induce a voltage in an antenna to transmit data, whereas Li-Fi uses the modulation of light intensity to transmit data. Li-Fi can theoretically transmit at speeds of up to 100 Gbit/s. Li-Fi's ability to safely function in areas otherwise susceptible to electromagnetic interference (e.g. aircraft cabins, hospitals, military) is an advantage. The technology is being developed by several organizations across the globe.

## Li-Fi Modulator
The Red Pitaya has 2 Fast Analog RF Outputs as shown below in the block diagram:
<p>
  <img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Block_Diagram.PNG" alt="Block Diagram" width="75%"/>
</p>

- The laser diode can transmit light pulses only in digital form, that is 1s and 0s, it's a 1 if the laser diode is ON and it's a 0 if the laser diode is OFF.
- The specification of the RF Outputs are ± 1V Max. amplitude and DC-40MHz.
- Thus, to power the Laser Module, a transistor is used as a switch. 

### Circuit Diagram of Li-Fi Modulator
<p>
  <img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Circuit.png" alt="Circuit Diagram" width="50%"/>
</p>

### Things required for Li-Fi Modulator
- Red Pitaya STEMlab 125-10 Starter Kit
- Perf Board and Soldering Kit
- BNC Connector
- Micro-BNC to BNC Converter
- Laser Diode Module
- NPN Transistor (BC547)
- Resistor (1k)
- Wires and Jumpers

### Building the Li-Fi Modulator
1. Take a BNC connector and connect wires to it's terminals 
- <img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/BNC_with_Wire.jpg" alt="Circuit Diagram" width="40%"/>
2. Take a perf board and solder the components including the BNC with wires to it according to the circuit diagram
- <img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Components_with_Perf_Board_Mod_Li_Fi.jpg" alt="Circuit Diagram" width="40%"/>
3. Connect the Micro-BNC to BNC connector to Red Pitaya
- <img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/RP_with_Connector.jpg" alt="rp"/>
4. Finally connect the BNC of the mudulator to Red Pitaya
- <img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Modulator_Setup.jpg" alt="mod" width="60%"/>

## Analysing the performance of Solar Cell for Li-Fi
### Choosing the right solar cell
<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Choosing%20the%20right%20Solar%20Cell.jpg" alt="mod" width="25%"/>

Different solar cells give different output powers, and so does the amount of noise in the output of the demodulator. 
Connect the solar cell that is to be analyzed to the input probe and open the oscilloscope and function generator app and analyze the output waveform to different frequencies

<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Analysis_Setup.jpg" alt="mod" width="50%"/>

Same way analyze the output for different solar cells

<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Comparison.png" alt="mod" width="50%"/>

<p> Click on the image below to play the video. </p>

[![Performace](https://img.youtube.com/vi/Nkylwls0E3c/0.jpg)](http://www.youtube.com/watch?v=Nkylwls0E3c)

### Solar Cell #1 Response
<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/graphs3.jpg" alt="mod" width="50%"/>

### Solar Cell #2 Response
<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/graphs1.jpg" alt="mod" width="50%"/>

## Li-Fi Demodulator
The Li-Fi demodulator is a standalone device with Audio Amplifier and the solar cell to demodulate the received light signals. 
A potentiometer is required to adjust the level of the input signal depending on the solar cell and environment. This is also to reduce the noise level. 
The solar cell receives converts the received light signals into corresponding voltage levels which is fed into the amplifier which provides the required gain and then the amplified signal is fed into the speaker, when the frequency is in the audible range to human ears - about 20 Hz to 20 kHz we will be able to hear the sound.

### Circuit Diagram of Li-Fi Demodulator
<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Li-Fi-Receiver-Circuit.png" alt="mod" width="50%"/>

### Things required for Li-Fi Modulator
- Perf Board and Soldering Kit / Bread Board
- LM386 Audio Amplifier IC
- Solar Cell
- 10k Potentiometer (Preset)
- Capacitors - 1 × 0.047uF, 3 × 10uF, 1 × 220uF 
- Resistor - 10 Ohms
- Speaker 8 Ohms, 0.5W
- 9V Battery and Cap
- Wires and Jumpers
- 4 Ohms Coil if using 4 Ohms Speaker

### Building the Prototype
Gather the components and prototype using the breadboard

<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Demod_test_components.jpg" alt="mod" width="50%"/>

Assembled Prototype

<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Demodulator_Testing.jpg" alt="mod" width="50%"/>

### Testing the prototype with Red Pitaya Function Generator 

Test Setup

<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Demod_setup.jpg" alt="mod" width="50%"/>

### Frequency Test upto 20kHz 

<p> Click on the image below to play the video. </p>

[![Performace](https://img.youtube.com/vi/0lLrks1bQIg/0.jpg)](http://www.youtube.com/watch?v=0lLrks1bQIg)

The above video shows the frequency response of the Li-Fi system. Next stage is building the Li-Fi Receiver 

### Building the Li-Fi Demodulator

Assemble the circuit in a perf board and finish the soldering. 

<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Receiver_2.jpg" alt="mod" width="50%"/>

## Generating Piano Music using Python

### SCPI Server

Red Pitaya board can be controlled remotely over LAN or wireless interface using MATLAB, LabVIEW, Scilab or Python via Red Pitaya SCPI (Standard Commands for Programmable Instrumentation) list of commands. SCPI interface/environment is commonly used to control T&M instruments for development, research or test automation purposes. SCPI uses a set of SCPI commands that are recognized by the instruments to enable specific actions to be taken (e.g.: acquiring data from fast analog inputs, generating signals and controlling other periphery of the Red Pitaya platform). The SCPI commands are extremely useful when complex signal analysis is required where SW environment such as MATLAB provides powerful data analysis tools and SCPI commands simple access to raw data acquired on Red Pitaya board.

Features
- Quickly write control routines and programs using MATLAB, LabVIEW, Scilab or Python
- Write testing scripts and routines
- Take quick measurements directly with your PC

Block Diagram explaining SCPI on Red Pitaya

<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/SCPI.png" alt="mod" width="75%"/>

### SCPI Commands over Python

The Red Pitaya Module in Python provides methods which are easy to implement.
Refer the documentation for more information on SCPI.

This SCPI command is used to set the frequency of the fast analog output channel: rp_s.tx_txt('SOUR1:FREQ:FIX ' + str(f))
Where f is desired frequency to be outputted.

### Playing tones

To play the keyboard notes, we need to know the frequency of each note. 
For simplicity reasons I took the 5th octave. 

Here's an image from Digilent's Reference:

<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Frequencies.PNG" alt="Cover"/>

The respective frequencies of the keyboard notes for a song with required delay is to be sent to the SCPI server. 
Refer to the code in the Python Directory of this repository. 

### Testing the Li-Fi Audio System
Click on the image below to play the video.

[![Performace](https://img.youtube.com/vi/oaPoHxmlVdA/0.jpg)](http://www.youtube.com/watch?v=oaPoHxmlVdA)

## Li-Fi Audio System with Multiple Receivers

### Reflective Solar Cell
To have multiple receivers to same light signal, a reflective solar cell is required as shown in the image below.

<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/RSC.png" alt="RSC" width="50%"/>

This specific type of Solar Cell absorbs some light falling on it and reflects the rest. Thus multiple receivers can be used by using this type of solar cell.

### Block Diagram of the Multiple Receiver Setup

<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Multiple_Receiver_Block_Diagram.png" alt="BD"/>

*When light is reflected from a surface, the angle of incidence is always equal to the angle of reflection, where both angles are measured from the path of the light to the normal to the surface at the point at which light strikes the surface.* This is called the law of reflection. Thus multiple receivers can be used by proper placement of Solar Cells. 

Two sets of receivers are to be built for this model

<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Receiver_1&2.jpg" alt="BD" width="50%">

### Final Setup

<p align="center">
  <img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Main_Photo.jpg" alt="Cover"/>
</p>

## Working of the Li-Fi Audio System with Multiple Receivers Model
 
[![Performace](https://img.youtube.com/vi/_GhAeeB7jKg/0.jpg)](http://www.youtube.com/watch?v=_GhAeeB7jKg)

# Software Requirements
- Python version 3.10.0 or above
 
# Installation 

1. Once you're done with the hardware, make sure you give the right connections as mentioned in the circuit diagrams.
2. Go to the Red Pitaya's Home Page > Development > Run
3. Note down the IP address in which the SCPI server is hosted. 
4. Create a directory in your local machine and clone this repository using the command
```
$ git clone https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi.git
```
5. Navigate to the Python Folder and then run the following command, say the IP address of the SCPI server is "192.168.137.43"
```
$ python Play_Music.py 192.168.137.43
```

# How to Use the Code

The Play_Music.py file contains the code for generating the Piano Music.
I've set the frequencies corresponding to the 5th Octave, how ever you may modify the code and add additional functionalities.

The string notes contains the keyboard notes and the delays for a particular song. You can play any music of your choice just by editing the notes string.
For example, the Piano Notes for London Bridge is falling down is given as 

```
notes = "g a g f e f g , d e f , e f g , g a g f e f g . d , g . e c"
```

And, the notes for Mary Had a Little Lamb is give as
```
notes = "e d c d e e e , d d d , e e e , e d c d e e e e d d e d c"
```

You can write notes for any other piano song the same way.

# Acknowledgements

I would like to thank the Red Pitaya team for sending me the STEMlab 125-10 Starter Kit and giving me this oppurtunity to explore and learn new things!


