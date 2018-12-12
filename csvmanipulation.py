import numpy as np 
energylist =[]


def main():
    try:
        SV,SC,BV,BC,LV,LC = np.loadtxt('data.csv',skiprows=2,delimiter=',',unpack=True,dtype='str')
        
        for voltage,current in zip(SV,SC):
            energy = int(voltage)*int(current)*3
            energylist.append(energy)
        
        
        total_energy = sum(energylist)
        print(total_energy)
            

          
    except Exception:
        print (str(Exception))

main()