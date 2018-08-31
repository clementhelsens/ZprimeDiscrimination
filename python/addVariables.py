import ROOT as r
from array import array
import glob
treename='events'
indir='TESTTREE.root'

lfiles=glob.glob('/eos/experiment/fcc/hh/analyses/Dijet_reso/heppy_outputs/fcc_v02_newHT/p8_pp_ZprimeSSM_*TeV_jj/heppy.FCChhAnalyses.FCChh.Dijet_reso.TreeProducer.TreeProducer_1/tree.root')
lfiles=[f for f in lfiles if 'Chunk' not in f]
lfiles=[indir]
for f in lfiles:
    print f
    tf= r.TFile.Open(f,"update")
    tt = tf.Get(treename)

#    costhetastar_cs   = array( 'f', [ 0 ] )
#    costhetastar_cs_b = tt.Branch("costhetastar_cs",costhetastar_cs,"costhetastar_cs/F")



    nentries = tt.GetEntries()
    trndm = r.TRandom3()
    trndm.SetSeed(0)
#nentries=100
    for i in xrange(nentries):
        if i%10000==0: print i,'/',nentries,' entry'
        fluc=trndm.Gaus()
        tt.GetEntry(i)
        nommass=tt.Mj1j2_pf04
        Mj1j2_pf04_5p[0] = nommass*(1+fluc*0.05)
        Mj1j2_pf04_10p[0] = nommass*(1+fluc*0.10)
        Mj1j2_pf04_15p[0] = nommass*(1+fluc*0.15)
        Mj1j2_pf04_20p[0] = nommass*(1+fluc*0.2)

        Mj1j2_pf04_5p_b.Fill()
        Mj1j2_pf04_10p_b.Fill()
        Mj1j2_pf04_15p_b.Fill()
        Mj1j2_pf04_20p_b.Fill()


    tt.Write()
    tf.Close()
