#!/usr/bin/python

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from subprocess import * 
from time import sleep, strftime
from datetime import datetime
from mpd import *
import threading
import signal
import sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PLAY=0
PAUSE=1
STOP=2
VOL=3

lcd = Adafruit_CharLCDPlate()
client = MPDClient()           # create client object
server = HTTPServer(('',80), pimp3clock_HTTPRequesthandler)
lock = threading.Lock()

class pimp3clock_HTTPRequesthandler(BaseHTTPRequestHandler):
  def do_GET(self):
    try:
      self.send_response(200)
      self.send_header('Content-type',	'text/html')
      self.end_headers()
      
      self.wfile.write("hey, today is the" + str(time.localtime()[7]))
      self.wfile.write(" day in the year " + str(time.localtime()[0]))
      return
    
    return
    
    except IOError:
      self.send_error(404,'File Not Found: %s' % self.path)
      
  def do_POST(self):
  try:
  except:
    pass
  

def display_lcd(title_a,st_a,vol_a):

  lcd.backlight(lcd.BLUE);
  lcd.clear()
  lcd.begin(16,1)

  play=[
    0b10000,
    0b11000,
    0b11100,
    0b11110,
    0b11100,
    0b11000,
    0b10000,
    0b00000
    ]
  lcd.createChar(PLAY,play)
  
  pause=[
    0b11011,
    0b11011,
    0b11011,
    0b11011,
    0b11011,
    0b11011,
    0b11011,
    0b11011
    ]
  lcd.createChar(PAUSE,pause)
  
  stop=[
    0b00000,
    0b11111,
    0b10001,
    0b10001,
    0b10001,
    0b10001,
    0b11111,
    0b00000
    ]
  lcd.createChar(STOP,stop)

  
  t=0
  i=0
  fr=1
  oldtitle=""

  while 1:
    lock.acquire()
    vol=[None]

    vol.append([0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000])
    vol.append([0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b10000,0b10000])
    vol.append([0b00000,0b00000,0b00000,0b00000,0b00000,0b01000,0b11000,0b11000])
    vol.append([0b00000,0b00000,0b00000,0b00000,0b00100,0b01100,0b11100,0b11100])
    vol.append([0b00000,0b00000,0b00000,0b00010,0b00110,0b01110,0b11110,0b11110])
    vol.append([0b00000,0b00000,0b00001,0b00011,0b00111,0b01111,0b11111,0b11111])
    
    lcd.createChar(VOL,vol[int((vol_a[0]+5)/(100/6))])  

    try:
      if (t % 2) == 0:
        lcd.home()
        lcd.write(VOL,True) # Special Characters
        lcd.message(datetime.now().strftime('%d.%b %H:%M:%S'))
      else:
        title=title_a[0]
        if title != oldtitle:
          fr=1
          i=0
        oldtitle=title
        st=st_a[0]
        lcd.clear()
        lcd.write(VOL,True) # Special Characters
        lcd.message(datetime.now().strftime('%d.%b %H %M %S\n'))
        lcd.write(st,True) # Special Characters
        lcd.message('%s' % (title[i:15+i]) )
        
        if fr==1:
          i=i+1
        else:
          i=i-1
          
        if i>len(title)-15:
          fr=0
        if i==0:
          fr=1
          
    finally:
      lock.release()
      
    t=t+1
    sleep(0.5)
 
def webserver():
  server.serve_forever()

def main_loop():
  i=0;
  title_a=[None]
  st_a=[None]
  vol_a=[None]
  
  title_a[0]=""
  st_a[0]=STOP
  vol_a[0]=100

  display_thread = threading.Thread(target=display_lcd, args=(title_a,st_a,vol_a))
  display_thread.daemon=True  # Causing thread to stop when main process ends.
  display_thread.start()

  webserver_thread = threading.Thread(target=webserver, args=())
  webserver_thread.daemon=True  # Causing thread to stop when main process ends.
  webserver_thread.start()

  client.connect("localhost", 6600)  # connect to localhost:6600

  # Load Database into current playlist
  client.update()
  client.clear()
  database=client.listall("/")
  for (i) in range(len(database)):
    if 'file' in database[i]:
      client.add(database[i]['file'])
  client.random(1)
  client.shuffle(1)
  client.crossfade(2)

  last_button=100;

  while 1:
        status = client.status()
        vol_a[0]=int(status['volume'])
        if (i % 5) == 0:
          song = client.currentsong()
          if song == {}:
            title_a[0]=""
          else:
            title_a[0]=song['artist'] + " - " + song['title']
          if status['state'] == "stop":
            st_a[0]=STOP
          elif status['state'] == "play":
            st_a[0]=PLAY
          elif status['state'] == "pause":
            st_a[0]=PAUSE
          
        lock.acquire()
        try:
          button = lcd.buttons()
        finally:
          lock.release()
          
        if ((button & 1) == 1) and (last_button != button): # SELECT
           if status['state'] == "stop":
             client.play()
           elif status['state'] == "play":
             client.pause(1)
           elif status['state'] == "pause":
             client.pause(0)
        elif ((button & 2) == 2) and (last_button != button):  # RIGHT
          client.next()
        elif (button & 4) == 4:  # DOWN
          if int(status['volume']) >0:
            client.setvol(int(status['volume']) - 1)
        elif (button & 8) == 8:  # UP
          if int(status['volume']) <100:
            client.setvol(int(status['volume']) + 1)
        elif ((button & 16) == 16) and (last_button != button):  # LEFT
          client.previous()

        last_button=button

        i=i+1;
	sleep(0.1)


def shutdown():
  client.stop()
  client.close()                     # send the close command
  client.disconnect()                # disconnect from the server
  lcd.clear();
  lcd.stop();
  
def sig_handler(signum = None, frame = None):
  shutdown()
  sys.exit(0)
  
try:
  for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]:
    signal.signal(sig, sig_handler)
    
  main_loop()
except (KeyboardInterrupt, SystemExit):
  shutdown()

