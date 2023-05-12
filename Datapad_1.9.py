#Datapad Program

import random
import Datapad_Modules as dpm

def main():
#Import information
    systems=open('Systems.txt','r')
    read_systems=systems.read()
    systems.close()
#Interpret information into dictionary
    systems=read_systems.split('\n')
    data={}
    counter=0
    for i in systems:
        system=i.split('/')
        data[system[0]]=[system[1],system[2],system[3],system[4],system[5]]
        
#Start app loop
    while True:
        do=str.lower(input('Input: '))
        print()
        print('------------------------------')

#Help (Show all options)
        if do in ["help", "h"]:
            print()
            print("search / s -                                 Search Systems by Name and display all their information")
            print("add / add system / a -                       Add a new System to the Datapad")
            print("all systems / show all / systems -           Displays a list of all recorded Systems' names")
            print("show economy / economy / system economy -    Displays a list of all recorded Systems' names based on the desired economy")
            print("trade / trading routes -                     Displays a trading route based on System economies that yield the best profit")
            print("species / by sepcies / system species -      Displays a list of all recorded Systems' names based on the ruling species")
            print("sell -                                       Display a list of recorded Systems that buy a specific 'special' item (as recorded by the user)")
            print("wealth -                                     Displays the ranking of a specified wealth 'description'")
            print("change -                                     Change the information recorded for a specific System")
            print("other items -                                Show Systems that sell other non-specific items")
            print("end / close / e -                            Close Datapad")
            print()
            print('------------------------------')

        
#Search for system
        if do in ["search", "s"]:
            dpm.search(data)
            print('------------------------------')
            print()
                
#Add system
        elif do in ["add", "add system", "a"]:
            dpm.add(data)
            print('------------------------------')
            print()
            
#Show all Systems
        elif do in ['all systems', 'show all systems', 'systems']:
            dpm.systems(data)
            print('------------------------------')
            print()
            
#Show systems per Economy Color
        elif do in ['show economy', 'economy', 'system economy']:
            dpm.economy(data)
            print('------------------------------')
            print()
            
#Create Trading Routs
        elif do in ['trade', 'trading routes']:
            dpm.trade(data)
            print('------------------------------')
            print()
            
#Search by Species
        elif do in ['species', 'by species', 'system species']:
            dpm.species(data)
            print('------------------------------')
            print()
            
#Search by Systems that buy well
        elif do=='sell':
            dpm.sell(data)
            print('------------------------------')
            print()
            
#Show me what level of wealth means
        elif do=='wealth':
            dpm.wealth(data)
            print('------------------------------')
            print()

#Change information on a system
        elif do=='change':
            dpm.change(data)
            print('------------------------------')
            print()

#Search for other information
        elif do=='other items' or do=='other info' or do=='search other':
            dpm.other(data)
            print('------------------------------')
            print()
                
#Close Datapad
        elif do in ["end", "e", "close"]:
            break

"""
#Show me all the lists of items
        elif do=='all items':
            dpm.items(data)
            print('------------------------------')
            print()
"""
    

main()
