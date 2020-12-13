################################################################################
import argparse

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--episode", action="store_true", default=False,
    help="search for an episode by name to return a list of characters and actors")
parser.add_argument("-c", "--character", action="store_true", default=False,
    help="search for a character by name to return a list of actors and episodes")
parser.add_argument("-a", "--actor", action="store_true", default=False,
    help="search for an actor by name to return a list of characters and episodes")
parser.add_argument("name", help="the string to search")
args = parser.parse_args()

# Come back and add behaviors for each flag
if args.episode:
    pass
elif args.character:
    pass
elif args.actor:
    pass