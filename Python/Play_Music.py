import sys
import redpitaya_scpi as scpi
import time

rp_s = scpi.scpi(sys.argv[1])


# Initialze the Red Pitaya RF Output Channel 1
def rp_init(wave_form, freq, ampl):
    rp_s.tx_txt('GEN:RST')
    rp_s.tx_txt('SOUR1:FUNC ' + str(wave_form).upper())
    rp_s.tx_txt('SOUR1:FREQ:FIX ' + str(freq))
    rp_s.tx_txt('SOUR1:VOLT ' + str(ampl))
    rp_s.tx_txt('OUTPUT1:STATE ON')

# Send the desired output frequency to SCPI Server
def send_frequency(f):
    rp_s.tx_txt('SOUR1:FREQ:FIX ' + str(f))
    time.sleep(0.5)

# Play the Tone
def play_tone(n):
    match n:
        case "c":
            send_frequency(523)
        case "c#":
            send_frequency(554)
        case "d":
            send_frequency(587)
        case "d#":
            send_frequency(622)
        case "e":
            send_frequency(660)
        case "f":
            send_frequency(698)
        case "f#":
            send_frequency(740)
        case "g":
            send_frequency(784)
        case "g#":
            send_frequency(830)
        case "a":
            send_frequency(880)
        case "a#":
            send_frequency(932)
        case "b":
            send_frequency(988)
        case ",":
            time.sleep(0.3)
        case ".":
            time.sleep(0.5)
        case _:        
            return 0   # 0 is the default case if x is not found


# Set Waveform, Amplitutde and inital frequency
wave_form = 'square'
ampl = 1
freq = 1000

rp_init(wave_form, freq, ampl)

# Notes for London Bridge is falling down
#notes = "g a g f e f g , d e f , e f g , g a g f e f g . d , g . e c"

# Notes for Mary had a little lamb
notes = "e d c d e e e , d d d , e e e , e d c d e e e e d d e d c"

# Split the string to get a single note
note = notes.split()

print("Playing Music")

# Play the notes
for n in note:
    play_tone(n)
