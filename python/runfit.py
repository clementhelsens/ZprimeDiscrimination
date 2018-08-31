import glob
import fileinput
import itertools
import os
l=glob.glob('config/*.config_temp')

lumi=[ 1000000., 10000000., 25000000., 50000000.]
models=['','ETA','CHI','PSI','LRM','I']

comb = list(itertools.product(models, lumi))
for c in comb:
    print c[0], c[1]
    for i in l:
        print i
        with open(i, 'r') as file :
            filedata = file.read()
            filedata = filedata.replace("=MODEL=",c[0])
            filedata = filedata.replace("=LUMIVALUE=",str(int(c[1])))
            if c[0]=='':filedata = filedata.replace("m_{Z } = 6 TeV_sel0_mzp","m_{Z} = 6 TeV_sel0_mzp")
        outfile=i.replace('_temp','')
        with open(outfile, 'w') as file:
            file.write(filedata)
        
        if 'ee' in outfile or 'mumu' in outfile:
            #os.system('../FCCFitter/myFit.exe h %s'%outfile)
            #os.system('../FCCFitter/myFit.exe w %s'%outfile)
            #os.system('../FCCFitter/myFit.exe f %s'%outfile)
            print 'dont run fit',

        elif 'll' in outfile:
            os.system('../FCCFitter/myFit.exe mwfl %s'%outfile)
