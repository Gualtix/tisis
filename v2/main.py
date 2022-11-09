import time
#from turtle import width
#from DrawFile import Draw
#from LocatorFile import Locator
from DocHandlerFile import DocHandler
from SequencerFile import Sequencer

def main():
    
    json_url = './Docs/offerings.json'
    Sq = Sequencer(json_url)
    Sq.start_automata(json_url)

if __name__ == "__main__":
    main()