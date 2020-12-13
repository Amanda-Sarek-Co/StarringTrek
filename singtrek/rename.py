import stapi
import types
import json
from pprint import pprint
from operator import itemgetter

def getPerformer(performer_name="Nana Visitor"):
    criteria = stapi.search_criteria.PerformerSearchCriteria(0,1,"", name="Nana Visitor") 
    response = stapi.RestClient().performer.search(criteria) # this returns a dictonary 
    performers = response['performers']
    
    if len(performers) == 1:
        performer = performers[0]
    else:
        raise NameError

    rest_client = stapi.RestClient()
    return rest_client.performer.get(performer["uid"])

def getEpisode(episode_name="The Storyteller"):
    criteria = stapi.search_criteria.EpisodeSearchCriteria(0,1,'', title="The Storyteller")
    response = stapi.RestClient().episode.search(criteria)
    episodes = response["episodes"]
    episode = episodes[0]

    rest_client = stapi.RestClient()

    return rest_client.episode.get(episode["uid"])