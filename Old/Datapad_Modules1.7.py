#Datapad Modules


#Search for system
def search(data):
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
    else:
        for i in data[search]:
            print(i)
                
#Add system
def add(data):
    add=input('Enter System: ')
    while True:
        try:
            x=int(input('How many items?: '))
        except:
            print('Invalid Number')
        else:
            break
    items=[]
    for i in range(x):
        item=input('Enter item: ')
        items+=[item]
    color=input('Enter Star Color: ')
    species=input('Enter Dominant Species: ')
    economy_color=input('Enter Economy Color: ')
    other_info=input('Other Information: ')
    data[add]=[items,color,species,economy_color,other_info]
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
    adding.write('\n'+add+'/'+items_string+'/'+color+'/'+species+'/'+economy_color+'/'+other_info)
    adding.close()
            
#Show all Systems
def systems(data):
    for i in data:
        print(i)
    print()
    print('Total of',len(data),'Systems Discoverd')

#Show systems per Economy Color
def economy(data):
    color=input('Enter Economy Color: ')
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
            if data[i][-2]=='Purple':
                purple1+=[i]
                purple2+=[len(data[i][0])]
            elif data[i][-2]=='Blue':
                blue1+=[i]
                blue2+=[len(data[i][0])]
            elif data[i][-2]=='Green':
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
            if data[i][-2]=='Light Blue':
                lblue1+=[i]
                lblue2+=[len(data[i][0])]
            elif data[i][-2]=='Red':
                red1+=[i]
                red2+=[len(data[i][0])]
            elif data[i][-2]=='Orange':
                orange1+=[i]
                orange2+=[len(data[i][0])]
            elif data[i][-2]=='Yellow':
                yellow1+=[i]
                yellow2+=[len(data[i][0])]
        best_lblue=max(lblue2)
        best_red=max(red2)
        best_orange=max(orange2)
        best_yellow=max(yellow2)
        print(lblue1[lblue2.index(best_lblue)],'-->',red1[red2.index(best_red)],'-->',orange1[orange2.index(best_orange)],'-->',yellow1[yellow2.index(best_yellow)])
            
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
    green_sell=['Decrypted User Data', 'Star Silk', 'Comet Droplets', 'Ion Sphere']
    what=input('Enter item to sell: ')
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
            
#Show me all the lists of items
def items(data):
    for i in data:
        print(i)
        print(data[i][0])
        print()
            
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
    while True:
        try:
            x=int(input('How many items?: '))
        except:
            print('Invalid Number')
        else:
            break
    items=[]
    for i in range(x):
        item=input('Enter item: ')
        items+=[item]
    color=input('Enter Star Color: ')
    species=input('Enter Dominant Species: ')
    economy_color=input('Enter Economy Color: ')
    other_info=input('Other Information: ')
    data[change]=[items,color,species,economy_color,other_info]
#Changing outside file
    redo=open('Systems.txt','w')
    string=''
    for i in data:
        string+=i+'/'
        counter=1
        for x in data[i][0]:
            string+=x
            if counter!=len(data[i][0]):
                string+=','
            counter+=1
        string+='/'+data[i][1]+'/'+data[i][2]+'/'+data[i][3]+'/'+data[i][4]+'\n'
    redo.write(string)
    redo.close()
    

