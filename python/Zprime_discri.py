import ROOT as r
import math
import multiprocessing as mp
lumi=1000.
basedir='/eos/experiment/fcc/helhc/analyses/Zprime_ll/heppy_outputs/helhc_v01/'
basedir='/eos/experiment/fcc/helhc/analyses/Zprime_ll_PDF19/heppy_outputs/helhc_v01/'
samples=['p8_pp_ZprimeSSM_6TeV_ll',
         'p8_pp_ZprimeETA_6TeV_ll',
         'p8_pp_ZprimeCHI_6TeV_ll',
         'p8_pp_ZprimeLRM_6TeV_ll',
         'p8_pp_ZprimePSI_6TeV_ll',
         'p8_pp_ZprimeI_6TeV_ll',

         'p8_pp_ZprimeSSM_Interf_6TeV_ll',
         'p8_pp_ZprimeETA_Interf_6TeV_ll',
         'p8_pp_ZprimeCHI_Interf_6TeV_ll',
         'p8_pp_ZprimeLRM_Interf_6TeV_ll',
         'p8_pp_ZprimePSI_Interf_6TeV_ll',
         'p8_pp_ZprimeI_Interf_6TeV_ll',

         'mgp8_pp_mumu_5f_HT_5000_10000',
         'mgp8_pp_ee_5f_HT_5000_10000',
         'mgp8_pp_mumu_5f_HT_2000_5000',
         'mgp8_pp_ee_5f_HT_2000_5000'

         'p8_pp_ZprimeSSM_4TeV_ll',
         'p8_pp_ZprimeETA_4TeV_ll',
         'p8_pp_ZprimeCHI_4TeV_ll',
         'p8_pp_ZprimeLRM_4TeV_ll',
         'p8_pp_ZprimePSI_4TeV_ll',
         'p8_pp_ZprimeI_4TeV_ll',

         'p8_pp_ZprimeSSM_8TeV_ll',
         'p8_pp_ZprimeETA_8TeV_ll',
         'p8_pp_ZprimeCHI_8TeV_ll',
         'p8_pp_ZprimeLRM_8TeV_ll',
         'p8_pp_ZprimePSI_8TeV_ll',
         'p8_pp_ZprimeI_8TeV_ll'

]


samples=[
         'p8_pp_ZprimeSSM_4TeV_ll_PDF19',
         'p8_pp_ZprimeETA_4TeV_ll_PDF19',
         'p8_pp_ZprimeCHI_4TeV_ll_PDF19',
         'p8_pp_ZprimeLRM_4TeV_ll_PDF19',
         'p8_pp_ZprimePSI_4TeV_ll_PDF19',
         'p8_pp_ZprimeI_4TeV_ll_PDF19',

         'p8_pp_ZprimeSSM_6TeV_ll_PDF19',
         'p8_pp_ZprimeETA_6TeV_ll_PDF19',
         'p8_pp_ZprimeCHI_6TeV_ll_PDF19',
         'p8_pp_ZprimeLRM_6TeV_ll_PDF19',
         'p8_pp_ZprimePSI_6TeV_ll_PDF19',
         'p8_pp_ZprimeI_6TeV_ll_PDF19',

         'p8_pp_ZprimeSSM_8TeV_ll_PDF19',
         'p8_pp_ZprimeETA_8TeV_ll_PDF19',
         'p8_pp_ZprimeCHI_8TeV_ll_PDF19',
         'p8_pp_ZprimeLRM_8TeV_ll_PDF19',
         'p8_pp_ZprimePSI_8TeV_ll_PDF19',
         'p8_pp_ZprimeI_8TeV_ll_PDF19'
]

XSEC={'p8_pp_ZprimeSSM_6TeV_ll':0.00127705,
      'p8_pp_ZprimeETA_6TeV_ll':0.000373203,
      'p8_pp_ZprimeCHI_6TeV_ll':0.000658995,
      'p8_pp_ZprimeLRM_6TeV_ll':0.000787521,
      'p8_pp_ZprimePSI_6TeV_ll':0.000319221,
      'p8_pp_ZprimeI_6TeV_ll'  :0.000515749,

      'p8_pp_ZprimeSSM_4TeV_ll':0.0125426,
      'p8_pp_ZprimeETA_4TeV_ll':0.0038843,
      'p8_pp_ZprimeCHI_4TeV_ll':0.00703298,
      'p8_pp_ZprimeLRM_4TeV_ll':0.00797759,
      'p8_pp_ZprimePSI_4TeV_ll':0.00336506,
      'p8_pp_ZprimeI_4TeV_ll'  :0.00582704,

      'p8_pp_ZprimeSSM_8TeV_ll':0.000204715,
      'p8_pp_ZprimeETA_8TeV_ll':4.90595E-05,
      'p8_pp_ZprimeCHI_8TeV_ll':8.70986E-05,
      'p8_pp_ZprimeLRM_8TeV_ll':0.000115722,
      'p8_pp_ZprimePSI_8TeV_ll':4.16344E-05,
      'p8_pp_ZprimeI_8TeV_ll'  :6.57607E-05,



      'p8_pp_ZprimeSSM_6TeV_ll_PDF19':0.00136389,
      'p8_pp_ZprimeETA_6TeV_ll_PDF19':0.000397324,
      'p8_pp_ZprimeCHI_6TeV_ll_PDF19':0.000676058,
      'p8_pp_ZprimeLRM_6TeV_ll_PDF19':0.000828187,
      'p8_pp_ZprimePSI_6TeV_ll_PDF19':0.000336398,
      'p8_pp_ZprimeI_6TeV_ll_PDF19'  :0.000519332,

      'p8_pp_ZprimeSSM_4TeV_ll_PDF19':0.0145604,
      'p8_pp_ZprimeETA_4TeV_ll_PDF19':0.00457997,
      'p8_pp_ZprimeCHI_4TeV_ll_PDF19':0.00791412,
      'p8_pp_ZprimeLRM_4TeV_ll_PDF19':0.00912529,
      'p8_pp_ZprimePSI_4TeV_ll_PDF19':0.0039201,
      'p8_pp_ZprimeI_4TeV_ll_PDF19'  :0.00640409,

      'p8_pp_ZprimeSSM_8TeV_ll_PDF19':0.000207047,
      'p8_pp_ZprimeETA_8TeV_ll_PDF19':4.70821e-05,
      'p8_pp_ZprimeCHI_8TeV_ll_PDF19':8.69071e-05,
      'p8_pp_ZprimeLRM_8TeV_ll_PDF19':0.000117093,
      'p8_pp_ZprimePSI_8TeV_ll_PDF19':3.94839e-05,
      'p8_pp_ZprimeI_8TeV_ll_PDF19'  :6.66165e-05,

      'p8_pp_ZprimeSSM_Interf_6TeV_ll':0.00146237,
      'p8_pp_ZprimeETA_Interf_6TeV_ll':0.000973733,
      'p8_pp_ZprimeCHI_Interf_6TeV_ll':0.00124877,
      'p8_pp_ZprimeLRM_Interf_6TeV_ll':0.00123982,
      'p8_pp_ZprimePSI_Interf_6TeV_ll':0.000913289,
      'p8_pp_ZprimeI_Interf_6TeV_ll':0.00112091,

      'mgp8_pp_mumu_5f_HT_5000_10000':2.603E-06,
      'mgp8_pp_ee_5f_HT_5000_10000':2.603E-06,
      'mgp8_pp_mumu_5f_HT_2000_5000':0.0006172,
      'mgp8_pp_ee_5f_HT_2000_5000':0.0006172
}


NEVT={'p8_pp_ZprimeSSM_6TeV_ll_PDF19':990000,
      'p8_pp_ZprimeETA_6TeV_ll_PDF19':980000,
      'p8_pp_ZprimeCHI_6TeV_ll_PDF19':980000,
      'p8_pp_ZprimeLRM_6TeV_ll_PDF19':1000000,
      'p8_pp_ZprimePSI_6TeV_ll_PDF19':980000,
      'p8_pp_ZprimeI_6TeV_ll_PDF19'  :990000,

      'p8_pp_ZprimeSSM_4TeV_ll_PDF19':980000,
      'p8_pp_ZprimeETA_4TeV_ll_PDF19':990000,
      'p8_pp_ZprimeCHI_4TeV_ll_PDF19':990000,
      'p8_pp_ZprimeLRM_4TeV_ll_PDF19':1000000,
      'p8_pp_ZprimePSI_4TeV_ll_PDF19':990000,
      'p8_pp_ZprimeI_4TeV_ll_PDF19'  :980000,

      'p8_pp_ZprimeSSM_8TeV_ll_PDF19':1000000,
      'p8_pp_ZprimeETA_8TeV_ll_PDF19':1000000,
      'p8_pp_ZprimeCHI_8TeV_ll_PDF19':1000000,
      'p8_pp_ZprimeLRM_8TeV_ll_PDF19':1000000,
      'p8_pp_ZprimePSI_8TeV_ll_PDF19':1000000,
      'p8_pp_ZprimeI_8TeV_ll_PDF19'  :990000,

    'p8_pp_ZprimeSSM_6TeV_ll':1000000,
      'p8_pp_ZprimeETA_6TeV_ll':1690000,
      'p8_pp_ZprimeCHI_6TeV_ll':1700000,
      'p8_pp_ZprimeLRM_6TeV_ll':1000000,
      'p8_pp_ZprimePSI_6TeV_ll':1700000,
      'p8_pp_ZprimeI_6TeV_ll'  :1700000,

      'p8_pp_ZprimeSSM_4TeV_ll':1000000,
      'p8_pp_ZprimeETA_4TeV_ll':1690000,
      'p8_pp_ZprimeCHI_4TeV_ll':1700000,
      'p8_pp_ZprimeLRM_4TeV_ll':1000000,
      'p8_pp_ZprimePSI_4TeV_ll':1700000,
      'p8_pp_ZprimeI_4TeV_ll'  :1700000,

      'p8_pp_ZprimeSSM_8TeV_ll':990000,
      'p8_pp_ZprimeETA_8TeV_ll':1700000,
      'p8_pp_ZprimeCHI_8TeV_ll':1700000,
      'p8_pp_ZprimeLRM_8TeV_ll':1000000,
      'p8_pp_ZprimePSI_8TeV_ll':1690000,
      'p8_pp_ZprimeI_8TeV_ll'  :1700000,


      'p8_pp_ZprimeSSM_Interf_6TeV_ll':1000000,
      'p8_pp_ZprimeETA_Interf_6TeV_ll':980000,
      'p8_pp_ZprimeCHI_Interf_6TeV_ll':1000000,
      'p8_pp_ZprimeLRM_Interf_6TeV_ll':970000,
      'p8_pp_ZprimePSI_Interf_6TeV_ll':990000,
      'p8_pp_ZprimeI_Interf_6TeV_ll':1000000,

      'mgp8_pp_mumu_5f_HT_5000_10000':6200000,
      'mgp8_pp_ee_5f_HT_5000_10000':6180000,
      'mgp8_pp_mumu_5f_HT_2000_5000':6200000,
      'mgp8_pp_ee_5f_HT_2000_5000':5910000
}

 

#samples=['p8_pp_ZprimeSSM_6TeV_ll']
def runMT_pool(args=('','')):
    indir,s=args
    tf=r.TFile.Open(indir)
    tt=tf.Get('events')
    n=tt.GetEntries()
    n=50000

    weight=lumi*XSEC[s]/NEVT[s]
    print ' ---   ',weight

    ry_num=0
    ry_den=0
    yf=0
    yfbar=0

    cospos=0
    cosneg=0

    print 'nentries = ',n
    tlv_epos = r.TLorentzVector()
    tlv_eneg = r.TLorentzVector()

    h_m_dy  = r.TH2F("h_m_dy","mass versus #delta|y|",80,2000.,10000.,50,-5.,5.)
    h_m_cos = r.TH2F("h_m_cos","mass versus cos#theta^{*}",80,2000.,10000.,50,-1,1)
    h_m_zpy = r.TH2F("h_m_zpy","mass versus |Zprime_{y}|",80,2000.,10000.,100,0.,5.)

    h_m_dy.Sumw2()
    h_m_cos.Sumw2()
    h_m_zpy.Sumw2()

    for i in xrange(n):
        if i%50000==0:print 'entry %i/%i'%(i,n)
        tt.GetEntry(i)

        if tt.lep1_pdgid == tt.lep2_pdgid: 
            continue
        #if abs(tt.lep1_pdgid) == 11 and abs(tt.lep2_pdgid)==11 and abs(tt.zprime_ele_m-6000.)>500:
        #    continue
        #if abs(tt.lep1_pdgid) == 13 and abs(tt.lep2_pdgid)==13 and abs(tt.zprime_muon_m-6000.)>500:
        #    continue
        if abs(tt.lep1_eta)>2.5 or abs(tt.lep2_eta)>2.5: 
            continue

        if tt.lep1_pdgid<0:
            m=0.105
            if abs(tt.lep1_pdgid)==11: m=0.000511
            tlv_epos.SetPtEtaPhiM(tt.lep1_pt, tt.lep1_eta, tt.lep1_phi, m)
            tlv_eneg.SetPtEtaPhiM(tt.lep2_pt, tt.lep2_eta, tt.lep2_phi, m)
        else:
            m=0.105
            if abs(tt.lep1_pdgid)==11: m=0.000511
            tlv_eneg.SetPtEtaPhiM(tt.lep1_pt, tt.lep1_eta, tt.lep1_phi, m)
            tlv_epos.SetPtEtaPhiM(tt.lep2_pt, tt.lep2_eta, tt.lep2_phi, m)

        tlv_ee = tlv_epos + tlv_eneg
        #prepare components of the cosCS calculation
        Lplus  = tlv_eneg.E()+tlv_eneg.Pz()
        Lminus = tlv_eneg.E()-tlv_eneg.Pz()
        Pplus  = tlv_epos.E()+tlv_epos.Pz()
        Pminus = tlv_epos.E()-tlv_epos.Pz()

        #does the cosCS calculation
        cosThetaCS  = (Lplus*Pminus - Lminus*Pplus)
        cosThetaCS *= abs(tlv_ee.Pz())
        cosThetaCS /= (tlv_ee.Mag()*tlv_ee.Pz())
        cosThetaCS /= math.sqrt(tlv_ee.Mag2() + tlv_ee.Pt()*tlv_ee.Pt() )

        delta_y = -9999.
        #l1=l-, l2=l+
        if tt.lep1_pdgid >0: delta_y = abs(tt.lep1_eta)-abs(tt.lep2_eta)

        #l1=l+, l2=l-
        if tt.lep2_pdgid >0: delta_y = abs(tt.lep2_eta)-abs(tt.lep1_eta)

        if abs(tt.lep1_pdgid) == 11 and abs(tt.lep2_pdgid)==11: 
            h_m_cos.Fill( tt.zprime_ele_m,cosThetaCS,weight)
            h_m_dy.Fill( tt.zprime_ele_m,delta_y,weight)
            h_m_zpy.Fill( tt.zprime_ele_m,abs(tt.zprime_y),weight)

        elif abs(tt.lep1_pdgid) == 13 and abs(tt.lep2_pdgid)==13: 
            h_m_cos.Fill( tt.zprime_muon_m,cosThetaCS,weight)
            h_m_dy.Fill( tt.zprime_muon_m,delta_y,weight)
            h_m_zpy.Fill( tt.zprime_muon_m,abs(tt.zprime_y),weight)

        if cosThetaCS>0:cospos+=1
        else:cosneg+=1


        #l1=l-, l2=l+, eta(l1)>eta(l2) FWD
        if tt.lep1_pdgid >0 and abs(tt.lep1_eta)>abs(tt.lep2_eta):yf+=1

        #l1=l+, l2=l-, eta(l2)>eta(l1) FWD
        if tt.lep2_pdgid >0 and abs(tt.lep2_eta)>abs(tt.lep1_eta):yf+=1

        #l1=l+, l2=l-, eta(l1)>eta(l2) BKW
        if tt.lep1_pdgid <0 and abs(tt.lep1_eta)>abs(tt.lep2_eta):yfbar+=1

        #l1=l-, l2=l+, eta(l2)>eta(l1) BKW
        if tt.lep2_pdgid <0 and abs(tt.lep2_eta)>abs(tt.lep1_eta):yfbar+=1

        if abs(tt.zprime_y)<0.5:ry_num+=1
        elif 0.5<abs(tt.zprime_y) and abs(tt.zprime_y)<2.5:ry_den+=1
        #if abs(tt.zprime_y)>2.5:print abs(tt.zprime_y)
    print '==============================================================='
    print 'sample          ',s
    print 'ry              ',float(float(ry_num)/float(ry_den))       ,'   ',ry_num,ry_den,ry_num+ry_den
    print 'AFB             ',float(yf-yfbar)/float(yf+yfbar)          ,'   ',yf,yfbar,yf+yfbar
    print 'AFB  costheta   ',float(cospos-cosneg)/float(cospos+cosneg),'   ',cospos,cosneg,cospos+cosneg
    print '==============================================================='

    outf = r.TFile.Open("/afs/cern.ch/user/h/helsens/FCCsoft/ZprimeDiscri/Outputs/%s.root"%s,"RECREATE")
    outf.cd()
    h_m_cos.Write()
    h_m_dy.Write()
    h_m_zpy.Write()
    outf.Close()


threads = []
for s in samples:
    indir='%s%s/heppy.FCChhAnalyses.HELHC.Zprime_ll.TreeProducer.TreeProducer_1/tree.root'%(basedir,s)
    threads.append((indir,s))

ncpu=mp.cpu_count()
print "ncpu  ",ncpu
pool = mp.Pool(ncpu)
histos_list = pool.map(runMT_pool,threads) 
