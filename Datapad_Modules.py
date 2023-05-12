#Datapad Modules
import random


#Search for system
def search(data):
    search=input('Enter System: ')
    print()   
#Print information 
    if search in data:
        print(search)
        print('Economy Level:',data[search][0])
        print(data[search][1],'Sun')
        print(data[search][2],'Dominated')
        print(data[search][3],'Economy')
        print(data[search][4])
    else:
        print('No System by the name',search)
                
#Add system
def add(data):
    add=input('Enter System: ')
    while True:
        try:
            level=int(input('Enter Economy Level?: '))
        except:
            print('Invalid Number')
        else:
            break
    color=input('Enter Star Color: ')
    species=input('Enter Dominant Species: ')
    economy_color=input('Enter Economy Color: ')
    other_info=input('Other Information: ')
    data[add]=[level,color,species,economy_color,other_info]
    adding=open('Systems.txt','a')
    adding.write('\n'+add+'/'+str(level)+'/'+color+'/'+species+'/'+economy_color+'/'+other_info)
    adding.close()
            
#Show all Systems
def systems(data):
    for i in data:
        print(i)
    print()
    print('Total of',len(data),'Systems Discoverd')

#Show systems per Economy Color
def economy(data):
    enter=input('Enter Economy Color: ')
    color=''
    x=0
    for i in enter:
        if x==0:
            letter=i.upper()
            color+=letter
        else:
            color+=i
        x=1
    print()
    counter=0
    for i in data:
        if data[i][-2]==color:
            print(i)
            counter+=1
        else:
            continue
    print()
    print(counter,'Registerd Systems with Economy Color',color)
         
#Create Trading Routs
def trade(data):
    while True:
        length=int(input('Enter Route Length: '))
        if length==3:
            purp=[]
            blue=[]
            gren=[]
            for i in data:
                if data[i][-2]=='Purple' and data[i][0]=='5':
                    purp+=[i]
                elif data[i][-2]=='Blue' and data[i][0]=='5':
                    blue+=[i]
                elif data[i][-2]=='Green' and data[i][0]=='5':
                    gren+=[i]
            print(purp[random.randint(0,len(purp)-1)])
            print(blue[random.randint(0,len(blue)-1)])
            print(gren[random.randint(0,len(gren)-1)])
            break
        elif length==4:
            ltbl=[]
            red=[]
            orng=[]
            yelw=[]
            for i in data:
                if data[i][-2]=='Light Blue' and data[i][0]=='5':
                    ltbl+=[i]
                elif data[i][-2]=='Light Blue' and data[i][0]=='4':
                    ltbl+=[i]
                elif data[i][-2]=='Red' and data[i][0]=='5':
                    red+=[i]
                elif data[i][-2]=='Red' and data[i][0]=='4':
                    red+=[i]
                elif data[i][-2]=='Orange' and data[i][0]=='5':
                    orng+=[i]
                elif data[i][-2]=='Orange' and data[i][0]=='4':
                    orng+=[i]
                elif data[i][-2]=='Yellow' and data[i][0]=='5':
                    yelw+=[i]
            print(ltbl[random.randint(0,len(ltbl)-1)])
            print(red[random.randint(0,len(red)-1)])
            print(orng[random.randint(0,len(orng)-1)])
            print(yelw[random.randint(0,len(yelw)-1)])
            break
        else:
            print('No Routs of that Length')
            print()
            continue

#Search by Species
def species(data):
    species=input('Enter Species: ')
    counter=0
    for i in data:
        if data[i][-3]==species:
            print(i)
            counter+=1
        else:
            continue
    print()
    if species=='No Habitants':
        print(counter,'Registerd Systems dominated by',species)
    else:
        print(counter,'Registerd Systems dominated by the',species)
            
#Search by Systems that buy well
def sell(data):
    lblue_sell=['Autonomus Positioning Unit', 'Ion Capacitor', 'Decomissioned Circuit Board', 'Welding Soap', 'Quantum Accelerator']
    red_sell=['Spark Canisters', 'Industrial Grade Battery', 'Ohmic Gel', 'Experimental Power Fluid']
    orange_sell=['Dirt', 'Unrefined Pyrite Grease', 'Bromide Salt', 'Pychromatic Zircondium']
    yellow_sell=['Non-Stick Piston', 'Enormous Metal Cog', 'Six Pronged Mesh Decoupler', 'Holographic Crankshaft']
    purple_sell=['Nanotube Crate', 'Self Repairing Heridium', 'Optical Solvent', 'Five Dimensional Torus']
    blue_sell=['De-Scented Pheromone Bottle', 'Neutron Microscope', 'Instability Injector', 'Organic Piping']
    green_sell=['Decrypted User Data', 'Star silk', 'Comet droplets', 'Ion Sphere']
    what=str.lower(input('Enter item to sell: '))
    print()
    if what in lblue_sell:
        print('Good profit in Red Systems:')
        print()
        for i in data:
            if data[i][-2]=='Red':
                print(i)
    elif what in red_sell:
        print('Good profit in Orange Systems:')
        print()
        for i in data:
            if data[i][-2]=='Orange':
                print(i)
    elif what in orange_sell:
        print('Good profit in Yellow Systems:')
        print()
        for i in data:
            if data[i][-2]=='Yellow':
                print(i)
    elif what in yellow_sell:
        print('Good profit in Light Blue Systems:')
        print()
        for i in data:
            if data[i][-2]=='Light Blue':
                print(i)
    elif what in purple_sell:
        print('Good profit in Blue Systems:')
        print()
        for i in data:
            if data[i][-2]=='Blue':
                print(i)
    elif what in blue_sell:
        print('Good profit in Green Systems:')
        print()
        for i in data:
            if data[i][-2]=='Green':
                print(i)
    elif what in green_sell:
        print('Good profit in Purple Systems:')
        print()
        for i in data:
            if data[i][-2]=='Purple':
                print(i)
    else:
        print('No record of any System purchasing this')
            
#Show me what level of wealth means
def wealth(data):
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

#Change information on a system
def change(data):
    change=input('Enter System: ')
    if change in data:
        while True:
            try:
                level=int(input('Enter Economy Level: '))
            except:
                print('Invalid Number')
            else:
                break
        color=input('Enter Star Color: ')
        species=input('Enter Dominant Species: ')
        economy_color=input('Enter Economy Color: ')
        other_info=input('Other Information: ')
        data[change]=[level,color,species,economy_color,other_info]
    else:
        print(change,'System Not Registered')
#Changing outside file
    redo=open('Systems.txt','w')
    string=''
    counter=1
    for i in data:
        string+=i+'/'+str(data[i][0])+'/'+data[i][1]+'/'+data[i][2]+'/'+data[i][3]+'/'+data[i][4]
        if counter<len(data):
            string+='\n'
        else:
            break
        counter+=1
    redo.write(string)
    redo.close()

#Search other info
def other(data):
    item=input('Enter item you search: ')
    sells=[]
    for i in data:
        if item in data[i][-1].split(', '):
            sells+=[i]
    for i in sells:
        print(i)


