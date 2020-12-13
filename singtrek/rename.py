################################################################################
import stapi
import types
import json
from pprint import pprint
from operator import itemgetter

def getPerformer(performer_name="Nana Visitor"):
    criteria = stapi.search_criteria.PerformerSearchCriteria(0, 1, "",
        name=performer_name)

    response = stapi.RestClient().performer.search(criteria) # returns dictonary 
    performers = response["performers"]
    
    if len(performers) == 1:
        performer = performers[0]
    else:
        raise NameError

    rest_client = stapi.RestClient()
    return rest_client.performer.get(performer["uid"])

def getEpisode(episode_name="The Storyteller"):
    criteria = stapi.search_criteria.EpisodeSearchCriteria(0, 1, "",
        title=episode_name)
    response = stapi.RestClient().episode.search(criteria)
    episodes = response["episodes"]
    episode = episodes[0]

    rest_client = stapi.RestClient()

    return rest_client.episode.get(episode["uid"])

def getCharacter(character_name="Kira Nerys"):
    criteria = stapi.search_criteria.CharacterSearchCriteria(0, 1, "",
        name=character_name)
    response = stapi.RestClient().character.search(criteria)
    characters = response["characters"]
    if len(characters) == 1:
        character = characters[0]
    else:
        character = characters[0]   # change so it includes entries besides the first

    rest_client = stapi.RestClient()
    
    return rest_client.character.get(character["uid"])
