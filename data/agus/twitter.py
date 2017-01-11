import tweepy 
import time 
from tweepy import Stream 
from tweepy.auth import OAuthHandler 
from tweepy.streaming import StreamListener 

ckey='dH7wGLT9ZQp7pA9QBKxq6hBXE'
csecret='U0ZkvQ21dQw8zQ4VnvvOrK0DS5MDKB0gRDyYpyCp8w7FESXqOQ'
atoken='3181521055-tfcxyBJwQ2nHYQIhfbRR0wBvSga2IHfJKlbzKC6'
asecret='Qv6sYaSJ45xL6Tp1jvpSaT5YobH6rGhSVzkfE2r5svALB'

class listener(StreamListener): 
	def on_data(self,data): 
			tweet=data.split(',"text":"')[1].split('","source')[0]
			saveThis=tweet.lower()
			print saveThis
			simpanFile=open('agus2.csv','a')
			simpanFile.write(saveThis)
			simpanFile.write('\n')
			simpanFile.close()
			return True
	def on_error(self,status): 
		print status
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["@AgusYudhoyono"])

