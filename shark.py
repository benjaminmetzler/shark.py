#!/usr/bin/env python

# This code is a python port of Michael Rolig's shark.c and is considered to be 
# in the public domain 

import hidapi
import argparse

def SendCommand(packet_array):
    packets = chr(0x00) # pero need to pre-pad with 0x00 per hid_write docu
    for byte in packet_array:
        packets = packets + chr(int(byte, 16) )

    hidapi.hid_init()

    # Connect to the RadioSHARK
    dev=hidapi.hid_open(0x077d, 0x627a)
    # Write the packets
    packets_written = hidapi.hid_write(dev, packets)

    # Close out 
    hidapi.hid_close(dev)

    if(args.debug):
        print "Packet Array: %s" % packet_array
        print "Number of Packets Sent: %s" % str(1+len(packet_array))
        print "Number of Packets Written: %i" % packets_written


# Create a default empty packet array
packet_array = [ "0x00", "0x00", "0x00", "0x00", "0x00", "0x00" ]


# Grab the arguments from the command line
parser = argparse.ArgumentParser()
parser.add_argument('-blue', action='store', help="turn on blue LED (0-127), e.g. '-blue 127'")
parser.add_argument('-pulse', action='store', help="turn on blue LED pulsing (0-127), e.g. '-pulse 64'")
parser.add_argument('-red', action='store', help="turn on/off red LED, e.g. '-red 1'")
parser.add_argument('-fm', action='store', help="set FM frequency, e.g. '-fm 91.5")
parser.add_argument('-am', action='store', help="set AM frequency, e.g. '-am 620   ")
parser.add_argument('--debug','-d', action='store_true', default=False)
args = parser.parse_args()

# doesn't make much sense to tune to AM and FM
if args.am and args.fm:
    print "ERROR: You can't select am and fm at the same time"
    parser.print_usage()
    exit(1)

# Tune FM Station
if args.fm is not None:
    packet_array[0] = "0xC0"
    freqency = float(args.fm)
    encodedFreq  = int(((freqency * 1000) + 10700) / 12.5)
    encodedFreq += 3

    packet_array[2] = hex((encodedFreq >> 8) & 0xFF)
    packet_array[3] = hex(encodedFreq & 0xFF)

    SendCommand(packet_array)

# Tune AM Station
if args.am is not None:
    packet_array[0] = "0xC0"
    encodedFreq = 0
    freqency = float(args.am)
    encodedFreq = int(freqency)+450

    packet_array[1] = "0x12"
    packet_array[2] = hex((encodedFreq >> 8) & 0xFF)
    packet_array[3] = hex(encodedFreq & 0xFF)

    SendCommand(packet_array)

# Set the blue LED intensity (0-127)
if args.blue is not None:
    if(args.blue < 0 and args.blue > 127):
        print "ERROR: Blue intensity outside expected range (0-127)."
        parser.print_usage()
        exit(1)

    packet_array[0] = "0xA0"
    packet_array[1] = hex(int(args.blue))

    SendCommand(packet_array)

# Set the pulsing LED intensity (0-127)
if args.pulse is not None:
    if(args.pulse < 0 and args.pulse > 127):
        print "ERROR: Pulse intensity outside expected range (0-127)."
        parser.print_usage()
        exit(1)
    
    packet_array[0] = "0xA1"
    packet_array[1] = hex(int(args.pulse))

    SendCommand(packet_array)

# Turn the red LED on (1) or off (0)
if args.red is not None:
    # Red LED only supports on or off
    if int(args.red) >= 1:
        packet_array[0] = "0xA9"
    else:
        packet_array[0] = "0xA8"

    SendCommand(packet_array)
