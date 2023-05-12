#Datapad Program

import random

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
        data[system[0]]=[system[1].split(','),system[2],system[3],system[4]]

    while True:
#What do you want to do?
        do=str.lower(input('Input: '))
        print()
        print('------------------------------')
#Search for system
        if do=='search':
            search=input('Enter System: ')
            print()
#Print information 
            print(search,end='')
            try:
                ec_level=len(data[search][0])
                print()
                print('Economy Level:',ec_level)
            except:
                print(' System not on the Records')
                print('------------------------------')
                print()
            else:
                for i in data[search]:
                    print(i)
                print('------------------------------')
                print()
#Add system
        elif do=='add' or do=='add system':
            add=input('Enter System: ')
            x=int(input('How many items?: '))
            items=[]
            for i in range(x):
                item=input('Enter item: ')
                items+=[item]
            color=input('Enter Star Color: ')
            species=input('Enter Dominant Species: ')
            information=input('Enter Economy Color: ')
            data[add]=[items,color,species,information]
            items_string=''
            counter=1
            for i in items:
                items_string=items_string+i
                if counter!=x:
                    items_string=items_string+','
                    counter+=1
                else:
                    break
            adding=open('Systems.txt','a')
            adding.write('\n'+add+'/'+items_string+'/'+color+'/'+species+'/'+information)
            adding.close()
            print('------------------------------')
            print()
#Show all Systems
        elif do=='all systems' or do=='show all systems' or do=='systems':
            for i in data:
                print(i)
            print()
            print('Total of',len(data),'Systems Discoverd')
            print('------------------------------')
            print()
#Show systems per Economy Color
        elif do=='show economy' or do=='economy' or do=='systems by economy':
            color=input('Enter Economy Color: ')
            print()
            counter=0
            for i in data:
                if data[i][-1]==color:
                    print(i)
                    counter+=1
                else:
                    continue
            print()
            print(counter,'Registerd Systems with Economy Color',color)
            print('------------------------------')
            print()
#Create Trading Routs
        elif do=='trade' or do=='trading routs':
            which=input('Select Rout Length (3/4): ')
            print()
            if which=='3':
                purple1=[]
                purple2=[]
                blue1=[]
                blue2=[]
                green1=[]
                green2=[]
                for i in data:
                    if data[i][-1]=='Purple':
                        purple1+=[i]
                        purple2+=[len(data[i][0])]
                    elif data[i][-1]=='Blue':
                        blue1+=[i]
                        blue2+=[len(data[i][0])]
                    elif data[i][-1]=='Green':
                        green1+=[i]
                        green2+=[len(data[i][0])]
                best_purple=max(purple2)
                best_blue=max(blue2)
                best_green=max(green2)
                print(purple1[purple2.index(best_purple)],'-->',blue1[blue2.index(best_blue)],'-->',green1[green2.index(best_green)])
            if which=='4':
                lblue1=[]
                lblue2=[]
                red1=[]
                red2=[]
                orange1=[]
                orange2=[]
                yellow1=[]
                yellow2=[]
                for i in data:
                    if data[i][-1]=='Light Blue':
                        lblue1+=[i]
                        lblue2+=[len(data[i][0])]
                    elif data[i][-1]=='Red':
                        red1+=[i]
                        red2+=[len(data[i][0])]
                    elif data[i][-1]=='Orange':
                        orange1+=[i]
                        orange2+=[len(data[i][0])]
                    elif data[i][-1]=='Yellow':
                        yellow1+=[i]
                        yellow2+=[len(data[i][0])]
                best_lblue=max(lblue2)
                best_red=max(red2)
                best_orange=max(orange2)
                best_yellow=max(yellow2)
                print(lblue1[lblue2.index(best_lblue)],'-->',red1[red2.index(best_red)],'-->',orange1[orange2.index(best_orange)],'-->',yellow1[yellow2.index(best_yellow)])
            print('------------------------------')
            print()
#Search by Species
        elif do=='species' or do=='by species' or do=='systems species':
            species=input('Enter Species: ')
            counter=0
            for i in data:
                if data[i][-2]==species:
                    print(i)
                    counter+=1
                else:
                    continue
            print()
            if species=='No Habitants':
                print(counter,'Registerd Systems dominated by',species)
            else:
                print(counter,'Registerd Systems dominated by the',species)
            print('------------------------------')
            print()
#Search by Systems that buy well
        elif do=='sell':
            what=input('Enter item to sell: ')
            print()
            lblue=['Autonomus Positioning Unit', 'Ion Capacitor', 'Decomissioned Circuit Board', 'Welding Soap', 'Quantum Accelerator']
            red=['Spark Canisters', 'Industrial Grade Battery', 'Ohmic Gel', 'Experimental Power Fluid']
            orange=['Dirt', 'Unrefined Pyrite Grease', 'Bromide Salt', 'Pychromatic Zircondium']
            yellow=['Non-Stick Piston', 'Enormous Metal Cog', 'Six Pronged Mesh Decoupler', 'Holographic Crankshaft']
            purple=['Nanotube Crate', 'Self Repairing Heridium', 'Optical Solvent', 'Five Dimensional Torus']
            blue=['De-Scented Pheromone Bottle', 'Neutron Microscope', 'Instability Injector', 'Organic Piping']
            green=['Decrypted User Data', 'Star Silk', 'Comet Droplets', 'Ion Sphere']
            if what in lblue:
                print('Good profit in Red Systems:')
                print()
                for i in data:
                    if data[i][-1]=='Red':
                        print(i)
            elif what in red:
                print('Good profit in Orange Systems:')
                print()
                for i in data:
                    if data[i][-1]=='Orange':
                        print(i)
            elif what in orange:
                print('Good profit in Yellow Systems:')
                print()
                for i in data:
                    if data[i][-1]=='Yellow':
                        print(i)
            elif what in yellow:
                print('Good profit in Light Blue Systems:')
                print()
                for i in data:
                    if data[i][-1]=='Light Blue':
                        print(i)
            elif what in purple:
                print('Good profit in Blue Systems:')
                print()
                for i in data:
                    if data[i][-1]=='Blue':
                        print(i)
            elif what in blue:
                print('Good profit in Green Systems:')
                print()
                for i in data:
                    if data[i][-1]=='Green':
                        print(i)
            elif what in green:
                print('Good profit in Purple Systems:')
                print()
                for i in data:
                    if data[i][-1]=='Purple':
                        print(i)
            else:
                print('No record of any System purchasing this')
            print('------------------------------')
            print()
#Show me all the lists of items
        elif do=='all items':
            for i in data:
                print(i)
                print(data[i][0])
                print()
            print('------------------------------')
            print()
#Show me what level of wealth means
        elif do=='wealth':
            level=str.lower(input('Enter Wealth: '))
            print()
            low=['declining','destitute','failing','fledgling','low supply','struggling','unsuccessful','unpromising']
            medium=['adequate','balanced','comfortable','developing','medium supply','promising','satisfactory','sustaiunable']
            high=['advanced','affluent','booming','flourishing','high supply','opulent','prosperous','wealthy']
            if level in low:
                print('Low Wealth Level')
            elif level in medium:
                print('Medium Wealth Level')
            elif level in high:
                print('High Wealth Level')
            elif level=='high':
                for i in high:
                    print(i)
            elif level=='medium':
                for i in medium:
                    print(i)
            elif level=='low':
                for i in low:
                    print(i)
            else:
                print('This level of wealth does not exist')
            print('------------------------------')
            print()
#Close Datapad
        elif do=='end' or do=='bye' or do=='close':
            break
    

main()
