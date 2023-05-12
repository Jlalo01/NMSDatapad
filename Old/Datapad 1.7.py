#Datapad Program

import random
import Datapad_Modules

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
        data[system[0]]=[system[1].split(','),system[2],system[3],system[4],system[5]]
        
#Start app loop
    while True:
        do=str.lower(input('Input: '))
        print()
        print('------------------------------')
        
#Search for system
        if do=='search':
            Datapad_Modules.search(data)
            print('------------------------------')
            print()
                
#Add system
        elif do=='add' or do=='add system':
            Datapad_Modules.add(data)
            print('------------------------------')
            print()
            
#Show all Systems
        elif do=='all systems' or do=='show all systems' or do=='systems':
            Datapad_Modules.systems(data)
            print('------------------------------')
            print()
            
#Show systems per Economy Color
        elif do=='show economy' or do=='economy' or do=='systems by economy':
            Datapad_Modules.economy(data)
            print('------------------------------')
            print()
            
#Create Trading Routs
        elif do=='trade' or do=='trading routs':
            Datapad_Modules.trade(data)
            print('------------------------------')
            print()
            
#Search by Species
        elif do=='species' or do=='by species' or do=='systems species':
            Datapad_Modules.species(data)
            print('------------------------------')
            print()
            
#Search by Systems that buy well
        elif do=='sell':
            Datapad_Modules.sell(data)
            print('------------------------------')
            print()
            
#Show me all the lists of items
        elif do=='all items':
            Datapad_Modules.items(data)
            print('------------------------------')
            print()
            
#Show me what level of wealth means
        elif do=='wealth':
            Datapad_Modules.wealth(data)
            print('------------------------------')
            print()

#Change information on a system
        elif do=='change' or do=='re-do':
            Datapad_Modules.change(data)
            print('------------------------------')
            print()
                
#Close Datapad
        elif do=='end' or do=='bye' or do=='close':
            break
    

main()
