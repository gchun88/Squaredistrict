from coinbase.wallet.client import Client

from coinbase.wallet.client import OAuthClient
import requests

ClientId="77d5af4941ffd6d5f0c9149e2e303a1c28d9f44c09b63694d6f2f608c60947c0"
Clientsecret="4395c36b93aa972ab4c6da2278cdca48f93e8551d0b13ee502552e249db90eb4"
access_token = "7e2da6a9cf25cec34dfda9e7951aeb6e862f47a291805f3c28af29951e5d9cd0"

r=requests.get("https://www.coinbase.com/oauth/authorize?response_type=code&client_id="+ClientId+"&redirect_uri=http://www.coinqual.com/&state=SECURE_RANDOM&scope=wallet:accounts:read")

code="089270d9ce1944069d6b52f35d15e6157c010a3c34b12e5df20e8e56f2472fae"
r2=requests.post("https://api.coinbase.com/oauth/token",data ={"grant_type":"authorization_code","code":code,"client_id":ClientId,"client_secret":Clientsecret,"redirect_uri":"http://www.coinqual.com/"})
r2=requests.post("https://api.coinbase.com/oauth/token",data ={"grant_type":"authorization_code","code":code,"Client_id":ClientId,"Client_secret":Clientsecret,"redirect_uri":"http://www.coinqual.com/"})
access_token="9d5a6c73082100b0f7729881191b3ca2d8f0682dcf3c09d187256d5db8e5bd8b"
refresh_token="9de1d38bc1f5a7814313cc5df960b9ed5ff7261093f2d0fb5f5f8d28bdb83309"

r=requests.get("https://www.coinbase.com/oauth/authorize?response_type=code&client_id="+ClientId+"&redirect_uri=http://www.coinqual.com/buy&state=SECURE_RANDOM&scope=wallet:accounts:read")

access_token="5bcfb256b661e4d2c61cced32ca6efb71e277f38503757693175d56349f9eeb1"

refresh_token="c22eca1d846b571dac86bb85f1fc75bfd86cb9fca61fe4f3eccf03e5cd720ef2"
qwdqwdqw