# Introduction
This is my python port of Michael Rolig's [shark.c](https://raw.githubusercontent.com/benjaminmetzler/til/main/misc/archive/shark.c) code.  As that code was in the public domain, this code is also in the public domain.

There are plenty of software-defined radios available that offer a lot more functionality but they are all missing one critical feature: a fin shape.  The RadioSHARK, on the otherhand, receives AM, FM, and is fin shaped making it the best USB radio receiver ever produced.

Anyway, this python script will allow you to control a the first version of the RadioSHARK.

This script uses the [awelkie/pyhidapi](https://github.com/awelkie/pyhidapi) python module.


## Usage
```
usage: shark.py [-h] [-blue BLUE] [-pulse PULSE] [-red RED] [-fm FM] [-am AM]
                [--debug]

optional arguments:
  -h, --help    show this help message and exit
  -blue BLUE    turn on blue LED (0-127), e.g. '-blue 127'
  -pulse PULSE  turn on blue LED pulsing (0-127), e.g. '-pulse 64'
  -red RED      turn on/off red LED, e.g. '-red 1'
  -fm FM        set FM frequency, e.g. '-fm 91.5
  -am AM        set AM frequency, e.g. '-am 620
  --debug, -d
```

## Examples
```shell
$ python shark.py -fm 97.5 # tune FM station 97.5
$ python shark.py -blue 127 # turn on the blue LED to max brightness
$ python shark.py -blue 0 # turn off the blue LED
```

## RadioSHARK v2 support
Apparently the second version of the RadioSHARK used a different custom protocol.  The overall logic in this script should work with the v2, but the packets will need to be tweaked.  See Hisaaki Shibata [shark2.c](https://raw.githubusercontent.com/benjaminmetzler/til/main/misc/archive/shark2.c) for more information.  Since I just have the single v1 RadioSHARK, any work I do to support the v2 would be untested.
