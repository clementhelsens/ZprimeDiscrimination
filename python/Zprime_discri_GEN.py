import ROOT as r
import math
import multiprocessing as mp
lumi=1000.
basedir='/eos/experiment/fcc/helhc/analyses/Zprime_ll_GEN/heppy_outputs/helhc_v01/'
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

]


samples=['p8_pp_ZprimeI_6TeV_ll',
         'p8_pp_ZprimeLRM_6TeV_ll',
         'p8_pp_ZprimeCHI_6TeV_ll',
         'p8_pp_ZprimeSSM_6TeV_ll',
         'p8_pp_ZprimePSI_6TeV_ll',
         'p8_pp_ZprimeETA_6TeV_ll'
]
samples=['p8_pp_ZprimeI_6TeV_ll']
XSEC={'p8_pp_ZprimeSSM_6TeV_ll':0.00127705,
      'p8_pp_ZprimeETA_6TeV_ll':0.000373203,
      'p8_pp_ZprimeCHI_6TeV_ll':0.000658995,
      'p8_pp_ZprimeLRM_6TeV_ll':0.000787521,
      'p8_pp_ZprimePSI_6TeV_ll':0.000319221,
      'p8_pp_ZprimeI_6TeV_ll'  :0.000515749,

      'p8_pp_ZprimeSSM_Interf_6TeV_ll':0.00146237,
      'p8_pp_ZprimeETA_Interf_6TeV_ll':0.000973733,
      'p8_pp_ZprimeCHI_Interf_6TeV_ll':0.00124877,
      'p8_pp_ZprimeLRM_Interf_6TeV_ll':0.00123982,
      'p8_pp_ZprimePSI_Interf_6TeV_ll':0.000913289,
      'p8_pp_ZprimeI_Interf_6TeV_ll':0.00112091,

}


NEVT={'p8_pp_ZprimeSSM_6TeV_ll':1000000,
      'p8_pp_ZprimeETA_6TeV_ll':1690000,
      'p8_pp_ZprimeCHI_6TeV_ll':1700000,
      'p8_pp_ZprimeLRM_6TeV_ll':1000000,
      'p8_pp_ZprimePSI_6TeV_ll':1700000,
      'p8_pp_ZprimeI_6TeV_ll'  :1700000,

      'p8_pp_ZprimeSSM_Interf_6TeV_ll':1000000,
      'p8_pp_ZprimeETA_Interf_6TeV_ll':980000,
      'p8_pp_ZprimeCHI_Interf_6TeV_ll':1000000,
      'p8_pp_ZprimeLRM_Interf_6TeV_ll':970000,
      'p8_pp_ZprimePSI_Interf_6TeV_ll':990000,
      'p8_pp_ZprimeI_Interf_6TeV_ll':1000000,
}

 
#a/b
def get_error_ratio(a,a_err,b,b_err):
    error=math.sqrt((b_err*b_err*a*a + a_err*a_err*b*b)/(b*b*b*b))
    return error


def get_error(a_err,b_err):
    error=math.sqrt(a_err*a_err + b_err*b_err)
    return error


def runMT_pool(args=('','')):
    indir,s=args
 
    tf=r.TFile.Open(indir)
    tt=tf.Get('events')
    n=tt.GetEntries()
    n=100

    weight=lumi*XSEC[s]/NEVT[s]
    print ' ---   ',weight

    ry_num_s1=0
    ry_den_s1=0
    yf_s1=0
    yfbar_s1=0
    cospos_s1=0
    cosneg_s1=0

    ry_num_s23=0
    ry_den_s23=0
    yf_s23=0
    yfbar_s23=0
    cospos_s23=0
    cosneg_s23=0

    ry_num_s1nos23=0
    ry_den_s1nos23=0
    yf_s1nos23=0
    yfbar_s1nos23=0
    cospos_s1nos23=0
    cosneg_s1nos23=0
    print 'nentries = ',n
  
    h_m_dy_s1  = r.TH2F("h_m_dy_s1","mass versus #delta|y|",80,2000.,10000.,50,-5.,5.)
    h_m_cos_s1 = r.TH2F("h_m_cos_s1","mass versus cos#theta^{*}",80,2000.,10000.,50,-1,1)
    h_m_zpy_s1 = r.TH2F("h_m_zpy_s1","mass versus |Zprime_{y}|",80,2000.,10000.,100,0.,5.)
    tlv_epos_s1 = r.TLorentzVector()
    tlv_eneg_s1 = r.TLorentzVector()

    h_m_dy_s23  = r.TH2F("h_m_dy_s23","mass versus #delta|y|",80,2000.,10000.,50,-5.,5.)
    h_m_cos_s23 = r.TH2F("h_m_cos_s23","mass versus cos#theta^{*}",80,2000.,10000.,50,-1,1)
    h_m_zpy_s23 = r.TH2F("h_m_zpy_s23","mass versus |Zprime_{y}|",80,2000.,10000.,100,0.,5.)
    tlv_epos_s23 = r.TLorentzVector()
    tlv_eneg_s23 = r.TLorentzVector()
    
    h_m_dy_s1nos23  = r.TH2F("h_m_dy_s1nos23","mass versus #delta|y|",80,2000.,10000.,50,-5.,5.)
    h_m_cos_s1nos23 = r.TH2F("h_m_cos_s1nos23","mass versus cos#theta^{*}",80,2000.,10000.,50,-1,1)
    h_m_zpy_s1nos23 = r.TH2F("h_m_zpy_s1nos23","mass versus |Zprime_{y}|",80,2000.,10000.,100,0.,5.)
    tlv_epos_s1nos23 = r.TLorentzVector()
    tlv_eneg_s1nos23 = r.TLorentzVector()

    h_m_dy_s1.Sumw2();h_m_dy_s23.Sumw2();h_m_dy_s1nos23.Sumw2()
    h_m_cos_s1.Sumw2();h_m_cos_s23.Sumw2();h_m_cos_s1nos23.Sumw2()
    h_m_zpy_s1.Sumw2();h_m_zpy_s23.Sumw2();h_m_zpy_s1nos23.Sumw2()

    for i in xrange(n):
        if i%50000==0:print 'entry %i/%i'%(i,n)
        tt.GetEntry(i)
        
        if tt.lep1_gen_1_pdgid == tt.lep2_gen_1_pdgid: 
            continue
        if abs(tt.lep1_gen_1_eta)>2.5 or abs(tt.lep2_gen_1_eta)>2.5: 
            continue

        if tt.jet1_pt>100: 
            print tt.jet1_pt
            tlv_j = r.TLorentzVector()
            tlv_l1 = r.TLorentzVector()
            tlv_l2 = r.TLorentzVector()
            tlv_j.SetPtEtaPhiM(tt.jet1_pt,tt.jet1_eta,tt.jet1_phi,tt.jet1_m)
            tlv_l1.SetPtEtaPhiM(tt.lep1_gen_1_pt,tt.lep1_gen_1_eta,tt.lep1_gen_1_phi,tt.lep1_gen_1_m)
            tlv_l2.SetPtEtaPhiM(tt.lep2_gen_1_pt,tt.lep2_gen_1_eta,tt.lep2_gen_1_phi,tt.lep2_gen_1_m)

            print 'dr j l1  :  ',tlv_j.DeltaR(tlv_l1),'    dr j l2  :  ',tlv_j.DeltaR(tlv_l2)

            continue
        
        if tt.lep1_gen_1_pdgid<0:
            m=0.105
            if abs(tt.lep1_gen_1_pdgid)==11: m=0.000511
            if tt.lep1_gen_1_pt>0 and tt.lep2_gen_1_pt>0:
                tlv_epos_s1.SetPtEtaPhiM(tt.lep1_gen_1_pt, tt.lep1_gen_1_eta, tt.lep1_gen_1_phi, m)
                tlv_eneg_s1.SetPtEtaPhiM(tt.lep2_gen_1_pt, tt.lep2_gen_1_eta, tt.lep2_gen_1_phi, m)
                
            if tt.lep1_gen_23_pt>0 and tt.lep2_gen_23_pt>0:
                tlv_epos_s23.SetPtEtaPhiM(tt.lep1_gen_23_pt, tt.lep1_gen_23_eta, tt.lep1_gen_23_phi, m)
                tlv_eneg_s23.SetPtEtaPhiM(tt.lep2_gen_23_pt, tt.lep2_gen_23_eta, tt.lep2_gen_23_phi, m)

            if tt.lep1_gen_1_pt>0 and tt.lep2_gen_1_pt>0 and tt.lep1_gen_23_pt<0 and tt.lep2_gen_23_pt<0:
                tlv_epos_s1nos23.SetPtEtaPhiM(tt.lep1_gen_1_pt, tt.lep1_gen_1_eta, tt.lep1_gen_1_phi, m)
                tlv_eneg_s1nos23.SetPtEtaPhiM(tt.lep2_gen_1_pt, tt.lep2_gen_1_eta, tt.lep2_gen_1_phi, m)

        else:
            m=0.105
            if abs(tt.lep1_pdgid)==11: m=0.000511
            if tt.lep1_gen_1_pt>0 and tt.lep2_gen_1_pt>0:
                tlv_eneg_s1.SetPtEtaPhiM(tt.lep1_gen_1_pt, tt.lep1_gen_1_eta, tt.lep1_gen_1_phi, m)
                tlv_epos_s1.SetPtEtaPhiM(tt.lep2_gen_1_pt, tt.lep2_gen_1_eta, tt.lep2_gen_1_phi, m)
                
            if tt.lep1_gen_23_pt>0 and tt.lep2_gen_23_pt>0:
                tlv_eneg_s23.SetPtEtaPhiM(tt.lep1_gen_23_pt, tt.lep1_gen_23_eta, tt.lep1_gen_23_phi, m)
                tlv_epos_s23.SetPtEtaPhiM(tt.lep2_gen_23_pt, tt.lep2_gen_23_eta, tt.lep2_gen_23_phi, m)

            if tt.lep1_gen_1_pt>0 and tt.lep2_gen_1_pt>0 and tt.lep1_gen_23_pt<0 and tt.lep2_gen_23_pt<0:
                tlv_eneg_s1nos23.SetPtEtaPhiM(tt.lep1_gen_1_pt, tt.lep1_gen_1_eta, tt.lep1_gen_1_phi, m)
                tlv_epos_s1nos23.SetPtEtaPhiM(tt.lep2_gen_1_pt, tt.lep2_gen_1_eta, tt.lep2_gen_1_phi, m)


        tlv_ee_s1 = tlv_epos_s1 + tlv_eneg_s1

        tlv_ee_s23 = tlv_epos_s23 + tlv_eneg_s23
        tlv_ee_s1nos23 = tlv_epos_s1nos23 + tlv_eneg_s1nos23

        #prepare components of the cosCS calculation
        Lplus_s1  = tlv_eneg_s1.E()+tlv_eneg_s1.Pz()
        Lminus_s1 = tlv_eneg_s1.E()-tlv_eneg_s1.Pz()
        Pplus_s1  = tlv_epos_s1.E()+tlv_epos_s1.Pz()
        Pminus_s1 = tlv_epos_s1.E()-tlv_epos_s1.Pz()

        #prepare components of the cosCS calculation
        Lplus_s23  = tlv_eneg_s23.E()+tlv_eneg_s23.Pz()
        Lminus_s23 = tlv_eneg_s23.E()-tlv_eneg_s23.Pz()
        Pplus_s23  = tlv_epos_s23.E()+tlv_epos_s23.Pz()
        Pminus_s23 = tlv_epos_s23.E()-tlv_epos_s23.Pz()

        #prepare components of the cosCS calculation
        Lplus_s1nos23  = tlv_eneg_s1nos23.E()+tlv_eneg_s1nos23.Pz()
        Lminus_s1nos23 = tlv_eneg_s1nos23.E()-tlv_eneg_s1nos23.Pz()
        Pplus_s1nos23  = tlv_epos_s1nos23.E()+tlv_epos_s1nos23.Pz()
        Pminus_s1nos23 = tlv_epos_s1nos23.E()-tlv_epos_s1nos23.Pz()

        #does the cosCS calculation
        cosThetaCS_s1  = (Lplus_s1*Pminus_s1 - Lminus_s1*Pplus_s1)
        cosThetaCS_s1 *= abs(tlv_ee_s1.Pz())
        cosThetaCS_s1 /= (tlv_ee_s1.Mag()*tlv_ee_s1.Pz())
        cosThetaCS_s1 /= math.sqrt(tlv_ee_s1.Mag2() + tlv_ee_s1.Pt()*tlv_ee_s1.Pt() )

        if tt.lep1_gen_23_pt>0 and tt.lep2_gen_23_pt>0:
            #does the cosCS calculation
            cosThetaCS_s23  = (Lplus_s23*Pminus_s23 - Lminus_s23*Pplus_s23)
            cosThetaCS_s23 *= abs(tlv_ee_s23.Pz())
            cosThetaCS_s23 /= (tlv_ee_s23.Mag()*tlv_ee_s23.Pz())
            cosThetaCS_s23 /= math.sqrt(tlv_ee_s23.Mag2() + tlv_ee_s23.Pt()*tlv_ee_s23.Pt() )

        if tt.lep1_gen_1_pt>0 and tt.lep2_gen_1_pt>0 and tt.lep1_gen_23_pt<0 and tt.lep2_gen_23_pt<0:
            #does the cosCS calculation
            cosThetaCS_s1nos23  = (Lplus_s1nos23*Pminus_s1nos23 - Lminus_s1nos23*Pplus_s1nos23)
            cosThetaCS_s1nos23 *= abs(tlv_ee_s1nos23.Pz())
            cosThetaCS_s1nos23 /= (tlv_ee_s1nos23.Mag()*tlv_ee_s1nos23.Pz())
            cosThetaCS_s1nos23 /= math.sqrt(tlv_ee_s1nos23.Mag2() + tlv_ee_s1nos23.Pt()*tlv_ee_s1nos23.Pt() )

        delta_y_s1 = -9999.
        #l1=l-, l2=l+
        if tt.lep1_gen_1_pdgid >0: delta_y_s1 = abs(tt.lep1_gen_1_eta)-abs(tt.lep2_gen_1_eta)
        #l1=l+, l2=l-
        if tt.lep2_gen_1_pdgid >0: delta_y_s1 = abs(tt.lep2_gen_1_eta)-abs(tt.lep1_gen_1_eta)

        delta_y_s23 = -9999.
        #l1=l-, l2=l+
        if tt.lep1_gen_23_pdgid >0: delta_y_s23 = abs(tt.lep1_gen_23_eta)-abs(tt.lep2_gen_23_eta)
        #l1=l+, l2=l-
        if tt.lep2_gen_23_pdgid >0: delta_y_s23 = abs(tt.lep2_gen_23_eta)-abs(tt.lep1_gen_23_eta)


        if tt.lep1_gen_1_pt>0 and tt.lep2_gen_1_pt>0:
            h_m_cos_s1.Fill( tlv_ee_s1.M(),cosThetaCS_s1,weight)
            h_m_dy_s1.Fill( tlv_ee_s1.M(),delta_y_s1,weight)
            h_m_zpy_s1.Fill( tlv_ee_s1.M(),abs(tlv_ee_s1.Rapidity()),weight)
            
            if tlv_ee_s1.M()<6200 and  tlv_ee_s1.M()>5800:
                if cosThetaCS_s1>0:cospos_s1+=1
                else:cosneg_s1+=1
                if tt.lep1_gen_1_pdgid >0 and abs(tt.lep1_gen_1_eta)>abs(tt.lep2_gen_1_eta):yf_s1+=1
                if tt.lep2_gen_1_pdgid >0 and abs(tt.lep2_gen_1_eta)>abs(tt.lep1_gen_1_eta):yf_s1+=1
                if tt.lep1_gen_1_pdgid <0 and abs(tt.lep1_gen_1_eta)>abs(tt.lep2_gen_1_eta):yfbar_s1+=1
                if tt.lep2_gen_1_pdgid <0 and abs(tt.lep2_gen_1_eta)>abs(tt.lep1_gen_1_eta):yfbar_s1+=1
                if abs(tlv_ee_s1.Rapidity())<0.5:ry_num_s1+=1
                elif 0.5<abs(tlv_ee_s1.Rapidity()) and abs(tlv_ee_s1.Rapidity())<2.5:ry_den_s1+=1

        if tt.lep1_gen_23_pt>0 and tt.lep2_gen_23_pt>0:
            h_m_cos_s23.Fill( tlv_ee_s23.M(),cosThetaCS_s23,weight)
            h_m_dy_s23.Fill( tlv_ee_s23.M(),delta_y_s23,weight)
            h_m_zpy_s23.Fill( tlv_ee_s23.M(),abs(tlv_ee_s23.Rapidity()),weight)

            if tlv_ee_s23.M()<6200 and  tlv_ee_s23.M()>5800:
                if cosThetaCS_s23>0:cospos_s23+=1
                else:cosneg_s23+=1
                if tt.lep1_gen_23_pdgid >0 and abs(tt.lep1_gen_23_eta)>abs(tt.lep2_gen_23_eta):yf_s23+=1
                if tt.lep2_gen_23_pdgid >0 and abs(tt.lep2_gen_23_eta)>abs(tt.lep1_gen_23_eta):yf_s23+=1
                if tt.lep1_gen_23_pdgid <0 and abs(tt.lep1_gen_23_eta)>abs(tt.lep2_gen_23_eta):yfbar_s23+=1
                if tt.lep2_gen_23_pdgid <0 and abs(tt.lep2_gen_23_eta)>abs(tt.lep1_gen_23_eta):yfbar_s23+=1
                if abs(tlv_ee_s23.Rapidity())<0.5:ry_num_s23+=1
                elif 0.5<abs(tlv_ee_s23.Rapidity()) and abs(tlv_ee_s23.Rapidity())<2.5:ry_den_s23+=1

        if tt.lep1_gen_1_pt>0 and tt.lep2_gen_1_pt>0 and tt.lep1_gen_23_pt<0 and tt.lep2_gen_23_pt<0:
            h_m_cos_s1nos23.Fill( tlv_ee_s1nos23.M(),cosThetaCS_s1nos23,weight)
            h_m_dy_s1nos23.Fill( tlv_ee_s1nos23.M(),delta_y_s1,weight)
            h_m_zpy_s1nos23.Fill( tlv_ee_s1nos23.M(),abs(tlv_ee_s1nos23.Rapidity()),weight)


            if tlv_ee_s1nos23.M()<6200 and  tlv_ee_s1nos23.M()>5800:
                if cosThetaCS_s1nos23>0:cospos_s1nos23+=1
                else:cosneg_s1nos23+=1
                if tt.lep1_gen_1_pdgid >0 and abs(tt.lep1_gen_1_eta)>abs(tt.lep2_gen_1_eta):yf_s1nos23+=1
                if tt.lep2_gen_1_pdgid >0 and abs(tt.lep2_gen_1_eta)>abs(tt.lep1_gen_1_eta):yf_s1nos23+=1
                if tt.lep1_gen_1_pdgid <0 and abs(tt.lep1_gen_1_eta)>abs(tt.lep2_gen_1_eta):yfbar_s1nos23+=1
                if tt.lep2_gen_1_pdgid <0 and abs(tt.lep2_gen_1_eta)>abs(tt.lep1_gen_1_eta):yfbar_s1nos23+=1
                if abs(tlv_ee_s1nos23.Rapidity())<0.5:ry_num_s1nos23+=1
                elif 0.5<abs(tlv_ee_s1nos23.Rapidity()) and abs(tlv_ee_s1nos23.Rapidity())<2.5:ry_den_s1nos23+=1


    err_1=get_error(yf_s1,yfbar_s1)
    err_2=get_error(cospos_s1,cosneg_s1)
    err_ry=get_error_ratio(float(ry_num_s1),math.sqrt(float(ry_num_s1)),float(ry_den_s1),math.sqrt(float(ry_den_s1)))
    err_afb=get_error_ratio(float(yf_s1-yfbar_s1),math.sqrt(err_1),float(float(yf_s1+yfbar_s1)),math.sqrt(err_1))
    err_afb_cs=get_error_ratio(float(cospos_s1-cosneg_s1),math.sqrt(err_2),float(float(cospos_s1+cosneg_s1)),math.sqrt(err_2))

    print '==============================================================='
    print 'sample status 1     ',s
    print 'ry              ',float(float(ry_num_s1)/float(ry_den_s1)),' +/-  ',err_ry,'  =====  ',ry_num_s1,ry_den_s1,ry_num_s1+ry_den_s1
    print 'AFB             ',float(yf_s1-yfbar_s1)/float(yf_s1+yfbar_s1),' +/-  ',err_afb,'  =====  ',yf_s1,yfbar_s1,yf_s1+yfbar_s1
    print 'AFB  costheta   ',float(cospos_s1-cosneg_s1)/float(cospos_s1+cosneg_s1),' +/-  ',err_afb_cs,'  =====  ',cospos_s1,cosneg_s1,cospos_s1+cosneg_s1
    print '==============================================================='

    err_1=get_error(yf_s23,yfbar_s23)
    err_2=get_error(cospos_s23,cosneg_s23)    
    err_ry=get_error_ratio(float(ry_num_s23),math.sqrt(float(ry_num_s23)),float(ry_den_s23),math.sqrt(float(ry_den_s23)))
    err_afb=get_error_ratio(float(yf_s23-yfbar_s23),math.sqrt(err_1),float(float(yf_s23+yfbar_s23)),math.sqrt(err_1))
    err_afb_cs=get_error_ratio(float(cospos_s23-cosneg_s23),math.sqrt(err_2),float(float(cospos_s23+cosneg_s23)),math.sqrt(err_2))

    print '  '
    print 'sample status 23     ',s
    print 'ry              ',float(float(ry_num_s23)/float(ry_den_s23)),' +/-  ',err_ry,'  =====  ',ry_num_s23,ry_den_s23,ry_num_s23+ry_den_s23
    print 'AFB             ',float(yf_s23-yfbar_s23)/float(yf_s23+yfbar_s23),' +/-  ',err_afb,'  =====  ',yf_s23,yfbar_s23,yf_s23+yfbar_s23
    print 'AFB  costheta   ',float(cospos_s23-cosneg_s23)/float(cospos_s23+cosneg_s23),' +/-  ',err_afb_cs,'  =====  ',cospos_s23,cosneg_s23,cospos_s23+cosneg_s23
    print '==============================================================='

    err_1=get_error(yf_s1nos23,yfbar_s1nos23)
    err_2=get_error(cospos_s1nos23,cosneg_s1nos23)    
    err_ry=get_error_ratio(float(ry_num_s1nos23),math.sqrt(float(ry_num_s1nos23)),float(ry_den_s1nos23),math.sqrt(float(ry_den_s1nos23)))
    err_afb=get_error_ratio(float(yf_s1nos23-yfbar_s1nos23),math.sqrt(err_1),float(float(yf_s1nos23+yfbar_s1nos23)),math.sqrt(err_1))
    err_afb_cs=get_error_ratio(float(cospos_s1nos23-cosneg_s1nos23),math.sqrt(err_2),float(float(cospos_s1nos23+cosneg_s1nos23)),math.sqrt(err_2))

    print '  '
    print 'sample status 1 no 23     ',s
    print 'ry              ',float(float(ry_num_s1nos23)/float(ry_den_s1nos23)),' +/-  ',err_ry,'  =====  ',ry_num_s1nos23,ry_den_s1nos23,ry_num_s1nos23+ry_den_s1nos23
    print 'AFB             ',float(yf_s1nos23-yfbar_s1nos23)/float(yf_s1nos23+yfbar_s1nos23),' +/-  ',err_afb,'  =====  ',yf_s1nos23,yfbar_s1nos23,yf_s1nos23+yfbar_s1nos23
    print 'AFB  costheta   ',float(cospos_s1nos23-cosneg_s1nos23)/float(cospos_s1nos23+cosneg_s1nos23),' +/-  ',err_afb_cs,'  =====  ',cospos_s1nos23,cosneg_s1nos23,cospos_s1nos23+cosneg_s1nos23
    print '==============================================================='


    outf = r.TFile.Open("%s_GEN.root"%s,"RECREATE")
    outf.cd()
    h_m_cos_s1.Write()
    h_m_dy_s1.Write()
    h_m_zpy_s1.Write()
    h_m_cos_s23.Write()
    h_m_dy_s23.Write()
    h_m_zpy_s23.Write()
    h_m_cos_s1nos23.Write()
    h_m_dy_s1nos23.Write()
    h_m_zpy_s1nos23.Write()

    outf.Close()


threads = []
for s in samples:
    indir='%s%s/heppy.FCChhAnalyses.HELHC.Zprime_ll.TreeProducer.TreeProducer_1/tree.root'%(basedir,s)
    threads.append((indir,s))

ncpu=mp.cpu_count()
print "ncpu  ",ncpu
pool = mp.Pool(ncpu)
histos_list = pool.map(runMT_pool,threads) 
