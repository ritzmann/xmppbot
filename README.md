# xmppbot

## Introduction

xmppbot acts as a XMPP client. It logs into a MUC (multi-user chat, AKA as chat room), observes all nickname changes and
logs each message in the MUC with the full JID (Jabber ID) of the author in the file xmppmessages.log.

Normal XMPP clients tend to display and log only the nickname of an author in a MUC and they do not log nickname
changes. That allows a participant to change their nickname, send a message, log off and there is no way to find out
what user really sent that message other than using this bot.

## Requirements

Python 3.2 or later and Python virtualenv.

## Installation

1. Create a virtualenv:
    
        virtualenv xmppbot
        . ./xmppbot/bin/activate
    
2. Install required Python libraries:
 
        cd <directory where you downloaded xmppbot>
        pip install -r requirements.txt
        
## Running

1. Activate virtualenv:

        . ./xmppbot/bin/activate
        
2. Run xmppbot:

        ./xmppbot.py <parameters>
        
    If you want to run xmppbot permanently, use:
    
        nohup ./xmppbot.py <parameters> 2>&1 >/dev/null &
        
    or if you are using fish:

        nohup ./xmppbot.py <parameters> ^/dev/null >/dev/null &

You must set the following command line parameters, otherwise the bot will ask for them on the terminal:
* -j jid: The JID of a user with moderator permissions (regular users may not be allowed to see JIDs in a MUC).
* -p password: The user password.
* -r muc-jid: The address of the MUC. Usually something like mucname@conference.jabberserver.domain.
* -n nick: Nickname that this bot will use in the MUC.

xmppbot creates two log files:
* xmppbot.log: Application log file. Should mostly be empty except for a successful login entry unless the bot has
               connectivity issues. The file is rotated daily and removed after 7 days.
* xmppmessages.log: Each message to the MUC is appended to this file together with the JID of the author and a
                    timestamp. The file is rotated daily and removed after 30 days.
                    
The logging configuration can easily be altered by editing the file logging.yaml. See 
https://docs.python.org/3/library/logging.config.html for detailed instructions.

## Improvements

* The bot seems to reconnect nicely when it loses a connections but it would need further testing.

* The bot maps each nickname to a JID and stores it in a hashtable. That hashtable could grow very big over time. 
  It should be replaced by a cache that would expire each entry that hasn't been updated in a couple of weeks.
  
* Implement unit testing.

* Bot happily connects and never complains when you misspell the MUC address.
