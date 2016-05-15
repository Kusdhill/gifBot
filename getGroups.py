import os
import sys
import argparse

reload(sys)
sys.setdefaultencoding("utf-8")

import requests
import json



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('botID')

    args = parser.parse_args()
    
    botID = args.botID

    postBot(botID)



def randomGiphy():

  endpoint = 'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=random'
  r = requests.get(endpoint)
  response = r.json()
 
  return(response['data']['id'])



def postBot(botID):

  gifID = randomGiphy()
  endpoint = 'https://api.groupme.com/v3/bots/post'
  r = requests.post(endpoint,
		json.dumps({
  			'bot_id' : botID,
  			'text' : 'https://media.giphy.com/media/'+gifID+'/giphy.gif'
		})
	)


if __name__ == '__main__':
    main()
    sys.exit(0)