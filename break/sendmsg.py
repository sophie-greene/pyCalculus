from twilio.rest import TwilioRestClient 
import twilio
print(twilio.__version__)
# put your own credentials here 
ACCOUNT_SID = "ACdb1ec0af4761757dbd2990f101bc7d62" 
AUTH_TOKEN = "cda736c44bd1b792bb382a22661c3c2b" 
 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
message=client.messages.create( 
    body_="Carol M: This is a message on behalf of Sophie Greene, informing you of the cancellation of the appointment you have with her" ,                         
    #to_="+447740721503" ,
     to_="+447535081347" ,
    from_="+441158241135"   
)
print(message.sid)