PomoTextr is (currently) a python CLI program to send text messages to your phone to help you get an audio Pomodoro cue without having to stare at your phone. 

In its current styling, PomoTextr accepts one phone number (US, ten-digits with no formatting) and works through one classic Pomodoro cycle. (4 cycles of 25 min working with 5 min breaks). 

###**Notes for using PomoTextr**

####**1. Twilio**

In order to get PomoTextr working on your personal account, you'll need to sign up for a Twilio trial. You'll create one messaging service and tie the number you create into it. You'll then plug in your account SID, auth token, message service sid into send_sms (or make them local variables as given in the send_sms.py file). 

####**2. Cycles**
Currently, PomoTextr runs one classic Pomodoro cycle. 

####**3.Syntax**
`python <path to main.py> <ten-digit unformatted number ex:9999999999>`

