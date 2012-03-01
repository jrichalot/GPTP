#### twgrep.py #### 
#! /usr/bin/python 
import twitter 
import re 
import sys 

api = twitter.Api( 
    consumer_key = 'yourconsumerkeygoeshere', 
    consumer_secret = 'yourconsumersecretgoeshere', 
    access_token_key = 'yourconsumeraccesstokengoeshere', 
    access_token_secret = 'yourtokensecretgoeshere' 
    ) 

#only useful if you are searching api.GetUserTimeline(user) see below
user = 'enterausernamehere' 
patt = sys.argv[1] 

#timeline = api.GetUserTimeline(user) 
timeline = api.GetPublicTimeline() 


for t in timeline: 
        if (re.search(patt, t.text)): 
            print t.user.screen_name, "=>", t.text 

### E N D ### 
