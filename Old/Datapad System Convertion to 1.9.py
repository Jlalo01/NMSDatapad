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
        
    for i in data:
        x=len(data[i][0])
        data[i][0]=str(x)

    y=''

    for i in data:
        y+=i+'/'+data[i][0]+'/'+data[i][1]+'/'+data[i][2]+'/'+data[i][3]+'/'+data[i][4]+'\n'

    print(y)



    writing=open('Systems.txt','w')
    ok=writing.write(y)
    writing.close()

main()
