# Wireless Audio Transmission using Li-Fi

<p align="center">
  <img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Main_Photo.jpg" alt="Cover"/>
</p>

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
- <img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/Modulator_Setup.jpg" alt="mod"/>

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

### Solar Cell 1 Response
<img src="https://github.com/yeshvanth-m/Wireless-Audio-Transmission-using-Li-Fi/blob/main/Photos/graphs3.jpg" alt="mod" width="50%"/>

### Solar Cell 1 Response
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


## D

### H

<img src="" width="100%" alt=""/>
<a href=""><img src="" /></a>


