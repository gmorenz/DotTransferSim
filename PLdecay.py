import numpy
import matplotlib.pyplot as plt
from io import BytesIO
import os
import subprocess

def PLDecay(filepath, filedir, fullfilename, savenam, mode, numbins, channels, printev = 1000000, reprate = 1, fontsize = 12, numlines = float('inf')):
    if mode == "t2":
        print("Error: Cannot calculate PL Decay from T2 data")
    suffix = ".txt"

    data = []
    if channels > 1:
        data2 = []
        data3 = []
    count = 0

    cmd1 = ("photon_synced_t2,--sync-channel," + str(channels) +",--file-in," + filepath+"RawData/"+filedir+fullfilename+"/"+fullfilename + suffix)
    cmd1 = cmd1.split(",")
    photons = subprocess.Popen(cmd1, stdout = subprocess.PIPE)
    out = photons.stdout.read()
    print(out)
    print(type(out))
    crash = please
         #MEMORY EFFICIENT LOADING!!!
    with open(filepath+"RawData/"+filedir+fullfilename+"/"+fullfilename + suffix, 'r') as fileobj:
        for line in fileobj:
            count = count + 1
            thisline = numpy.genfromtxt(BytesIO(line.encode('utf-8')),delimiter = ",")
            if channels == 1:
                data.append(thisline[2])
            else:
                if thisline[0] == 0:
                    data.append(thisline[2])
                elif thisline[0] == 1:
                    data2.append(thisline[2])
                elif thisline[0] == 2:
                    data3.append(thisline[2])
            if count%printev == 0:
                print(count)
            if count == numlines:
                break

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.hist(data, bins=numbins, color = 'r')
    if channels > 1:
        ax.hist(data2,bins = numbins, color = 'b')
        if not data3 == []:
            ax.hist(data3,bins=numbins, color = 'g')
    
    if fontsize > 12:
        ax.xaxis.set_tick_params(size = 7, width=2)
        ax.yaxis.set_tick_params(size = 7, width=2)
    
    fig.tight_layout()
    fig.savefig(savename + ".png")
    plt.close(fig)

filepath = "C:/Users/Karen/Dropbox (WilsonLab)/WilsonLab Team Folder/Data/Karen/DotTransferSim/"
filedir = "April17-longfinalfigs/"
filenames = ["Apr17"]
i = 0
count = 0
for concentration in [2*10**(-8),2*10**(-6),2*10**(-10)]:
    i = i + 1
    for sensitivity in [0.1,0.5,0.01]:
        for k_demission in [1400000,15]:
            for nligands in [100,1,10000]:
                for diffuse in range(2):
                    
                    f = filenames[0]
                    count = count + 1
                
                    if i == 2:
                        f = f + "conc"
                    elif i == 3:
                        f = f + "dilute"
                    
                    if k_demission == 15:
                        f = f + "CdSe"
                    else:
                        f = f + "PbS"
                    
                    f = f + str(nligands) + "ligs"

                    if diffuse == 1:
                        f = f + "DIFF"

                    PLDecay(filepath, filedir, f, f+"PLDec", "t3", 2048, 2)

filedir = "April23-longfinalfigs-lowflux/"
filenames = ["Apr23"]

i = 0
for concentration in [2*10**(-8),2*10**(-6),2*10**(-10)]:
    i = i + 1
    for sensitivity in [0.1,0.5,0.01]:
        for k_demission in [1400000,15]:
            for nligands in [100,1,10000]:
                for diffuse in range(2):
                    for laserpwr in [0.0005,0.05]:
                        f = filenames[0]
                        count = count + 1
                    
                        if i == 2:
                            f = f + "conc"
                        elif i == 3:
                            f = f + "dilute"
                        
                        if k_demission == 15:
                            f = f + "CdSe"
                        else:
                            f = f + "PbS"
                        
                        f = f + str(nligands) + "ligs"

                        if diffuse == 1:
                            f = f + "DIFF"

                        f = f + "lp" + str(laserpwr)

                        PLDecay(filepath, filedir, f, f+"PLDec", "t3", 2048, 2)