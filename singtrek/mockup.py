import argparse

"""Basic Database"""
class Episode:
    def __init__(self, series, season, episode, name):
        self.series = series
        self.season = season
        self.episode = episode
        self.name = name
    
    def __repr__(self):
        if self.series == "Movies":
            return self.name
        else:
            return self.series + " S" + str(self.season) + "E" + str("{:02d}".format(self.episode)) + " \"" + self.name + "\""

class Character:
    def __init__(self, name, episode_list):
        self.name = name
        self.episode_list = episode_list
    
    def __repr__(self):
        return str(self.name) + " appears in: " + str(self.episode_list)

class Actor:
    def __init__(self, l_name, f_name, char_list):
        self.l_name = l_name
        self.f_name = f_name
        self.char_list = char_list

    def __repr__(self):
        return self.f_name + " " + self.l_name + " plays: " + str(self.char_list)

brunt_list = [
    Episode("DS9", 3, 23, "Family Business"),
    Episode("DS9", 4, 16, "Bar Association"),
    Episode("DS9", 4, 25, "Body Parts"),
    Episode("DS9", 5, 20, "Ferengi Love Songs"),
    Episode("DS9", 6, 10, "The Magnificent Ferengi"),
    Episode("DS9", 6, 23, "Profit and Lace"),
    Episode("DS9", 7, 12, "The Emperor's New Cloak"),
    Episode("DS9", 7, 24, "The Dogs of War")
]
brunt = Character("Brunt", brunt_list)

krem_list = [Episode("ENT", 1, 19, "Acquisition")]
krem = Character("Krem", krem_list)

penk_list = [Episode("VOY", 6, 15, "Tsunkatse")]
penk = Character("Penk", penk_list)

shran_list = [
    Episode("ENT", 1, 7, "The Andorian Incident"),
    Episode("ENT", 1, 15, "Shadows of P'Jem"),
    Episode("ENT", 2, 15, "Cease Fire"),
    Episode("ENT", 3, 13, "Proving Ground"),
    Episode("ENT", 3, 24, "Zero Hour"),
    Episode("ENT", 4, 9, "Kir'Shara"),
    Episode("ENT", 4, 12, "Babel One"),
    Episode("ENT", 4, 13, "United"),
    Episode("ENT", 4, 14, "The Aenar"),
    Episode("ENT", 4, 22, "These Are the Voyages...")
]
shran = Character("Thy'lek Shran", shran_list)

tiron_list = [Episode("DS9", 3, 8, "Meridian")]
tiron = Character("Tiron", tiron_list)

j_combs_list = [brunt, krem, penk, shran, tiron]
j_combs = Actor("Combs", "Jeffrey", j_combs_list)

barclay_list = [
    Episode("TNG", 3, 21, "Hollow Pursuits"),
    Episode("TNG", 4, 19, "The Nth Degree"),
    Episode("TNG", 6, 2, "Realm of Fear"),
    Episode("TNG", 6, 12, "Ship in a Bottle"),
    Episode("TNG", 7, 19, "Genesis"),
    Episode("VOY", 2, 3, "Projections"),
    Episode("VOY", 6, 10, "Pathfinder"),
    Episode("VOY", 6, 24, "Life Line"),
    Episode("VOY", 7, 6, "Inside Man"),
    Episode("VOY", 7, 20, "Author, Author"),
    Episode("VOY", 7, 25, "Endgame"),
    Episode("Movies", 0, 0, "STAR TREK: FIRST CONTACT")
]
barclay = Character("Reginald Barclay", barclay_list)

d_schultz_list = [barclay]
d_schultz = Actor("Schultz", "Dwight", d_schultz_list)

"""Argument parsing"""
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--actor", action = "store_true", help = "search for an actor (instead of a character) in the database")
parser.add_argument("name", help = "the name to search")
args = parser.parse_args()

if args.actor:
    if args.name == d_schultz.l_name or args.name == d_schultz.f_name or args.name == d_schultz.f_name + " " + d_schultz.l_name or args.name == d_schultz.l_name + ", " + d_schultz.f_name:
        print(d_schultz)
    elif args.name == j_combs.l_name or args.name == j_combs.f_name or args.name == j_combs.f_name + " " + j_combs.l_name or args.name == j_combs.l_name + ", " + j_combs.f_name:
        print(j_combs)
    else:
        print("That name is not in the database. Please check the spelling.")
else:
    if args.name == "Brunt":
        print(brunt)
    else:
        print("That character is not in the database. Please check the spelling.")