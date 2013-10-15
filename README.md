pimp3clock.py
=============

![pimp3clock Image](pimp3clock.jpg)

pimp3clock is a simple MP3 Player/Clock for the Raspberry PI with an
Adafrut i2c 16x2 RGB LCP Plate (http://www.adafruit.com/products/716)
attached.

It is written in python and needs only one additional library:

- mpd (https://pypi.python.org/pypi/python-mpd/)

On raspbian you can install it with <sudo apt-get install python-mpd>

Additionaly to play the mp3 files you have to install and load mpd:

<sudo apt-get install mpd>

Copy mp3 files to: </var/lib/mpd/music>

The pimp3clock.py has to be started as root so it can access the i2c bus.



Adafruit_CharLCDPlate.py & Adafruit_I2C.py
------------------------------------------

Original can be found here: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_CharLCDPlate

Written by Limor Fried, Kevin Townsend and Mikey Sklar for Adafruit Industries.
  BSD license, all text above and below must be included in any redistribution

  To download, we suggest logging into your Pi with Internet accessibility and typing:
  git clone https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git

Copyright (c) 2012-2013 Limor Fried, Kevin Townsend and Mikey Sklar for Adafruit Industries.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
