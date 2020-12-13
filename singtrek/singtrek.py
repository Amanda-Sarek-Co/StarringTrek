################################################################################
import argparse

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--episode", action="store_true", default=False,
    help="search for an episode")
parser.add_argument("-c", "--character", action="store_true", default=False,
    help="search for a character")
parser.add_argument("-a", "--actor", action="store_true", default=False,
    help="search for an actor")
parser.add_argument("name", help="the name to search")
args = parser.parse_args()

# Come back and add behaviors for each flag
if args.episode:
    pass
elif args.character:
    pass
elif args.actor:
    pass