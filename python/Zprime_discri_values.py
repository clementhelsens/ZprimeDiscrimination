import ROOT as r
r.gROOT.SetBatch()
import math
from array import array
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



colors={'p8_pp_ZprimeSSM_6TeV_ll':1, 
        'p8_pp_ZprimeLRM_6TeV_ll':2, 
        'p8_pp_ZprimePSI_6TeV_ll':4, 
        'p8_pp_ZprimeCHI_6TeV_ll':8, 
        'p8_pp_ZprimeETA_6TeV_ll':6, 
        'p8_pp_ZprimeI_6TeV_ll':7,

        'p8_pp_ZprimeSSM_4TeV_ll':1, 
        'p8_pp_ZprimeLRM_4TeV_ll':2, 
        'p8_pp_ZprimePSI_4TeV_ll':4, 
        'p8_pp_ZprimeCHI_4TeV_ll':8, 
        'p8_pp_ZprimeETA_4TeV_ll':6, 
        'p8_pp_ZprimeI_4TeV_ll':7,

        'p8_pp_ZprimeSSM_8TeV_ll':1, 
        'p8_pp_ZprimeLRM_8TeV_ll':2, 
        'p8_pp_ZprimePSI_8TeV_ll':4, 
        'p8_pp_ZprimeCHI_8TeV_ll':8, 
        'p8_pp_ZprimeETA_8TeV_ll':6, 
        'p8_pp_ZprimeI_8TeV_ll':7,

        'p8_pp_ZprimeSSM_Interf_6TeV_ll':1, 
        'p8_pp_ZprimeLRM_Interf_6TeV_ll':2, 
        'p8_pp_ZprimePSI_Interf_6TeV_ll':4, 
        'p8_pp_ZprimeCHI_Interf_6TeV_ll':8, 
        'p8_pp_ZprimeETA_Interf_6TeV_ll':6, 
        'p8_pp_ZprimeI_Interf_6TeV_ll':7,}

names={'p8_pp_ZprimeSSM_6TeV_ll':"SSM", 
       'p8_pp_ZprimeLRM_6TeV_ll':"LRM", 
       'p8_pp_ZprimePSI_6TeV_ll':"#psi", 
       'p8_pp_ZprimeCHI_6TeV_ll':"#chi", 
       'p8_pp_ZprimeETA_6TeV_ll':"#eta", 
       'p8_pp_ZprimeI_6TeV_ll':"I",

       'p8_pp_ZprimeSSM_4TeV_ll':"SSM", 
       'p8_pp_ZprimeLRM_4TeV_ll':"LRM", 
       'p8_pp_ZprimePSI_4TeV_ll':"#psi", 
       'p8_pp_ZprimeCHI_4TeV_ll':"#chi", 
       'p8_pp_ZprimeETA_4TeV_ll':"#eta", 
       'p8_pp_ZprimeI_4TeV_ll':"I",

       'p8_pp_ZprimeSSM_8TeV_ll':"SSM", 
       'p8_pp_ZprimeLRM_8TeV_ll':"LRM", 
       'p8_pp_ZprimePSI_8TeV_ll':"#psi", 
       'p8_pp_ZprimeCHI_8TeV_ll':"#chi", 
       'p8_pp_ZprimeETA_8TeV_ll':"#eta", 
       'p8_pp_ZprimeI_8TeV_ll':"I",

       'p8_pp_ZprimeSSM_Interf_6TeV_ll':"SSM Interf", 
       'p8_pp_ZprimeLRM_Interf_6TeV_ll':"LRM Interf", 
       'p8_pp_ZprimePSI_Interf_6TeV_ll':"#psi Interf", 
       'p8_pp_ZprimeCHI_Interf_6TeV_ll':"#chi Interf", 
       'p8_pp_ZprimeETA_Interf_6TeV_ll':"#eta Interf", 
       'p8_pp_ZprimeI_Interf_6TeV_ll':"I Interf"
}


ry_val = 0.5

#a/b
def get_error_ratio(a,a_err,b,b_err):
    error=math.sqrt((b_err*b_err*a*a + a_err*a_err*b*b)/(b*b*b*b))
    return error

def get_error(a_err,b_err):
    error=math.sqrt(a_err*a_err + b_err*b_err)
    return error

def get_ry(h, m_min, m_max, ry_min, ry_max, h_b, err):
    first_bin = h.GetXaxis().FindBin(m_min)
    last_bin =  h.GetXaxis().FindBin(m_max)-1

    h_proj=h.ProjectionY("_py",first_bin,last_bin)
    num = h_proj.Integral(0, h_proj.FindBin(ry_min)-1)
    den = h_proj.Integral( h_proj.FindBin(ry_min), h_proj.FindBin(ry_max))
    err_num=math.sqrt(num)
    err_den=math.sqrt(den)

    err_num_b=0
    err_den_b=0
    if h_b!=None and err>0.:
        h_proj_b=h_b.ProjectionY("_py_b",first_bin,last_bin)
        num_b = h_proj_b.Integral(0, h_proj_b.FindBin(ry_min)-1)
        den_b = h_proj_b.Integral( h_proj_b.FindBin(ry_min), h_proj_b.FindBin(ry_max))
        err_num_b=num_b*err
        err_den_b=den_b*err

        num+=num_b
        den+=den_b
        err_num = get_error(err_num,err_num_b)
        err_den = get_error(err_den,err_den_b)

    print err_num,'    ',err_den,'  ',err_num_b,'  ',err_den_b
    ry = num/den
    ry_err = get_error_ratio(num, err_num, den, err_den)
    return ry, ry_err, num, den


def get_afb(h, m_min, m_max, h_b, err):
    first_bin = h.GetXaxis().FindBin(m_min)
    last_bin =  h.GetXaxis().FindBin(m_max)-1
    h_proj=h.ProjectionY("_py",first_bin,last_bin)
    neg=h_proj.Integral(0,int(h_proj.GetNbinsX()/2))
    pos=h_proj.Integral(int(h_proj.GetNbinsX()/2)+1,h_proj.GetNbinsX())
    err_neg=math.sqrt(neg)
    err_pos=math.sqrt(pos)

    err_pos_b=0
    err_neg_b=0
    if h_b!=None and err>0.:
        h_proj_b=h_b.ProjectionY("_py_b",first_bin,last_bin)
        pos_b = h_proj_b.Integral(0,int(h_proj.GetNbinsX()/2))
        neg_b = h_proj_b.Integral(int(h_proj.GetNbinsX()/2)+1,h_proj.GetNbinsX())
        err_pos_b=pos_b*err
        err_neg_b=neg_b*err

        pos+=pos_b
        neg+=neg_b
        err_pos = get_error(err_pos,err_pos_b)
        err_neg = get_error(err_neg,err_neg_b)

    num=pos-neg
    den=pos+neg
    err_num = get_error(err_neg,err_pos)
    err_den = get_error(err_neg,err_pos)
    afb=num/den
    afb_err = get_error_ratio(num, err_num, den, err_den)
    return afb, afb_err, num, den


def get_values(lumi, s, b, m_min, m_max, add=False, err=0.):

    tf_s = r.TFile.Open(s+'.root','r')
    #units of /fb so her 1/ab

    tf_b = None
    h_m_dy_b  = None
    h_m_cos_b = None
    h_m_zpy_b = None

    h_m_dy  = tf_s.Get("h_m_dy")
    h_m_cos = tf_s.Get("h_m_cos")
    h_m_zpy = tf_s.Get("h_m_zpy")
    h_m_dy.Scale(lumi)
    h_m_cos.Scale(lumi)
    h_m_zpy.Scale(lumi)
    if b!='':
        tf_b = r.TFile.Open(b+'.root','r')
        h_m_dy_b  = tf_b.Get("h_m_dy")
        h_m_cos_b = tf_b.Get("h_m_cos")
        h_m_zpy_b = tf_b.Get("h_m_zpy")
        h_m_dy_b.Scale(lumi)
        h_m_cos_b.Scale(lumi)
        h_m_zpy_b.Scale(lumi)
        if add==True:
            h_m_dy.Add(h_m_dy_b)
            h_m_cos.Add(h_m_cos_b)
            h_m_zpy.Add(h_m_zpy_b)


    ry,    ry_err, num_ry,  den_ry  = get_ry(h_m_zpy, m_min, m_max, ry_val, 4.5, h_m_zpy_b, err)
    afb_dy, afb_dy_err, num_afb, den_afb = get_afb(h_m_dy,m_min, m_max, h_m_dy_b, err)
    afb_cos,afb_cos_err,num_cos, den_cos = get_afb(h_m_cos,m_min, m_max, h_m_cos_b, err)

    print '==============================================================='
    print 'sample          ',s
    print 'ry              ',ry     ,' +/-  ',ry_err,'   ',num_ry, den_ry ,num_ry+den_ry
    print 'AFB  d|y|       ',afb_dy ,' +/-  ',afb_dy_err,'   ',num_afb,den_afb,num_afb+den_afb
    print 'AFB  costheta   ',afb_cos,' +/-  ',afb_cos_err,'   ',num_cos,den_cos,num_cos+den_cos
    print '==============================================================='
    tf_s.Close()
    if tf_b != None:tf_b.Close()

    return [ry,  ry_err,afb_cos,afb_cos_err]

lumi=1000.*15



#get_values(lumi, 'p8_pp_ZprimeI_6TeV_ll', '',m_min, m_max)
#get_values(1000., 'backgrounds', '',m_min, m_max)
#get_values(lumi, 'p8_pp_ZprimeI_6TeV_ll', 'backgrounds',m_min, m_max, False, 1.5)
#get_values(lumi, 'p8_pp_ZprimeI_6TeV_ll', 'backgrounds',m_min, m_max, True)


samples=['p8_pp_ZprimeSSM_6TeV_ll',
         'p8_pp_ZprimeETA_6TeV_ll',
         'p8_pp_ZprimeCHI_6TeV_ll',
         'p8_pp_ZprimeLRM_6TeV_ll',
         'p8_pp_ZprimePSI_6TeV_ll',
         'p8_pp_ZprimeI_6TeV_ll']

#samples=['p8_pp_ZprimeSSM_4TeV_ll',
#         'p8_pp_ZprimeETA_4TeV_ll',
#         'p8_pp_ZprimeCHI_4TeV_ll',
#         'p8_pp_ZprimeLRM_4TeV_ll',
#         'p8_pp_ZprimePSI_4TeV_ll',
#         'p8_pp_ZprimeI_4TeV_ll']

#samples=['p8_pp_ZprimeSSM_8TeV_ll',
#         'p8_pp_ZprimeETA_8TeV_ll',
#         'p8_pp_ZprimeCHI_8TeV_ll',
#         'p8_pp_ZprimeLRM_8TeV_ll',
#         'p8_pp_ZprimePSI_8TeV_ll',
#         'p8_pp_ZprimeI_8TeV_ll']

#samples=['p8_pp_ZprimeSSM_Interf_6TeV_ll',
#         'p8_pp_ZprimeETA_Interf_6TeV_ll',
#         'p8_pp_ZprimeCHI_Interf_6TeV_ll',
#         'p8_pp_ZprimeLRM_Interf_6TeV_ll',
#         'p8_pp_ZprimePSI_Interf_6TeV_ll',
#         'p8_pp_ZprimeI_Interf_6TeV_ll']

#####################################################################################
#####################################################################################
g_dic={}
for s in samples:
    gmax=2.
    gmin=1.
    m_min=5800
    m_max=6200
    m_min=3000
    m_max=9000

    if "4TeV" in s:
        gmax=0.48
        gmin=0.34
        m_min=3800
        m_max=4200

    if "8TeV" in s:
        gmax=1.2
        gmin=0.6
        m_min=7800
        m_max=8200

    lumi=1000.*15
    val=get_values(lumi, s, 'backgrounds',m_min, m_max, False, 0.05)
    #val=get_values(lumi, s, '',m_min, m_max)
    ry = array( 'd' )
    afb = array( 'd' )
    ry_err = array( 'd' )
    afb_err = array( 'd' )
    print val
    ry.append(val[0])
    ry_err.append(val[1])
    afb.append(val[2])
    afb_err.append(val[3])
    print ry

    g_dic[s]=r.TGraphErrors(1,afb,ry,afb_err,ry_err)

first=True
c=r.TCanvas('c','c',600,600)
print g_dic
lg = r.TLegend(0.6,0.7,0.9,0.9)
lg.SetFillStyle(0)
lg.SetLineColor(0)
lg.SetBorderSize(0)
lg.SetShadowColor(10)
lg.SetTextSize(0.040)
lg.SetTextFont(42)
lg.SetNColumns(3)
for g in g_dic:

    g_dic[g].SetMarkerColor(colors[g])
    g_dic[g].SetLineColor(colors[g])
    g_dic[g].SetFillColor(colors[g])

    g_dic[g].SetLineWidth(2)
    lg.AddEntry(g_dic[g],names[g],"f")
    if first:
        g_dic[g].SetMaximum(gmax)
        g_dic[g].SetMinimum(gmin)
        g_dic[g].GetXaxis().SetLimits(-0.4, 0.15)
#        g_dic[g].GetXaxis().SetLimits(-0.8, 0.15)

        g_dic[g].GetXaxis().SetTitle( "A_{FB}" )
        g_dic[g].GetYaxis().SetTitle( "r_{y} (x=%s)"%(str(ry_val) ))
        g_dic[g].GetYaxis().SetTitleOffset(1.3)
        g_dic[g].SetTitle("")
        g_dic[g].Draw("ACP")
        first=False
    else:
        g_dic[g].Draw("C")
        g_dic[g].SetMaximum(gmax)
        g_dic[g].SetMinimum(gmin)
        g_dic[g].GetXaxis().SetRangeUser(-0.4, 0.15)


lum_t = r.TLatex()
lum_t.SetTextAlign(22)
lum_t.SetTextFont(43)
lum_t.SetTextSize(32)
lum_t.DrawLatex(-0.30,0.77,"%i ab^{-1}"%(int(lumi/1000.)))

lg.Draw()
c.SaveAs('ry_afb.eps')
#####################################################################################

#####################################################################################
g_dic_afb={}
g_dic_afb_err_up={}
g_dic_afb_err_do={}
g_dic_ry={}
g_dic_ry_err_up={}
g_dic_ry_err_do={}

samples=['p8_pp_ZprimePSI_Interf_6TeV_ll',
         'p8_pp_ZprimeETA_Interf_6TeV_ll']

name="_SSM_%s"%(samples[1].replace('p8_pp_Zprime','').replace('_6TeV_ll',''))

lumi=[1000.,2000.,3000.,4000.,5000.,7000.,8000.,10000.,15000.,20000.,25000.,30000.,35000.,40000.,50000.,100000.]
for s in samples:

    m_min=5800
    m_max=6200
    gmax=0.8
    gmin=0.5
  
    if "4TeV" in s:
        gmax=0.48
        gmin=0.34
        m_min=3800
        m_max=4200

    if "8TeV" in s:
        gmax=1.2
        gmin=0.6
        m_min=7800
        m_max=8200


    ry = array( 'd' )
    afb = array( 'd' )
    afb_err_up = array( 'd' )
    afb_err_do = array( 'd' )

    ry_err = array( 'd' )
    ry_err_up = array( 'd' )
    ry_err_do = array( 'd' )

    afb_err = array( 'd' )
    dummy = array( 'd' )
    lumi_arr = array( 'd' )

    for l in lumi:
        #val=get_values(l, s, 'backgrounds',m_min, m_max, False, 0.05)
        val=get_values(l, s,'',m_min, m_max)

        ry.append(val[0])
        ry_err.append(val[1])
        afb.append(val[2])
        afb_err.append(val[3])
        dummy.append(0)
        lumi_arr.append(l/1000.)
        ry_err_up.append(val[0]+val[1])
        ry_err_do.append(val[0]-val[1])
        afb_err_up.append(val[2]+val[3])
        afb_err_do.append(val[2]-val[3])

    g_dic_ry[s]  = r.TGraphErrors(len(lumi),lumi_arr,ry,dummy,ry_err)
    g_dic_ry_err_up[s]  = r.TGraph(len(lumi),lumi_arr,ry_err_up)
    g_dic_ry_err_do[s]  = r.TGraph(len(lumi),lumi_arr,ry_err_do)

    g_dic_afb[s] = r.TGraphErrors(len(lumi),lumi_arr,afb,dummy,afb_err)
    g_dic_afb_err_up[s]  = r.TGraph(len(lumi),lumi_arr,afb_err_up)
    g_dic_afb_err_do[s]  = r.TGraph(len(lumi),lumi_arr,afb_err_do)

  
first=True
c_ry=r.TCanvas('c','c',600,600)
lg = r.TLegend(0.6,0.7,0.9,0.9)
lg.SetFillStyle(0)
lg.SetLineColor(0)
lg.SetBorderSize(0)
lg.SetShadowColor(10)
lg.SetTextSize(0.040)
lg.SetTextFont(42)
lg.SetNColumns(3)
print g_dic_ry
for g in reversed(sorted(g_dic_ry.keys())):
    g_dic_ry[g].SetMarkerColor(colors[g])
    g_dic_ry[g].SetLineColor(colors[g])
    g_dic_ry[g].SetFillColor(colors[g])
    g_dic_ry[g].SetLineWidth(2)

    lg.AddEntry(g_dic_ry[g],names[g],"f")
    if first:
        first=False
        g_dic_ry[g].SetMaximum(gmax)
        g_dic_ry[g].SetMinimum(gmin)
        g_dic_ry[g].SetLineColor(colors[g])
        g_dic_ry[g].SetLineWidth(-2002)
        g_dic_ry[g].SetFillColor(colors[g])
        g_dic_ry[g].SetFillStyle(3002)

        g_dic_ry[g].SetTitle("r_{y} versus Int. Lumi ")
        g_dic_ry[g].GetXaxis().SetTitle( "Lumi (ab^{-1})" )
        g_dic_ry[g].GetYaxis().SetTitle( "r_{y} (x=%s)"%(str(ry_val)) )
        g_dic_ry[g].GetYaxis().SetTitleOffset(1.3)
        g_dic_ry[g].Draw("A3")
#        g_dic_ry[g].Draw("3")


    else:
        g_dic_ry[g].SetLineColor(colors[g])
        g_dic_ry[g].SetLineWidth(0)
        g_dic_ry[g].SetFillColor(colors[g])
        g_dic_ry[g].SetFillStyle(3002)
        #g_dic_ry[g].Draw("AB1")
        g_dic_ry[g].Draw("3")

    g_dic_ry_err_up[g].SetLineWidth(2)
    g_dic_ry_err_up[g].SetLineColor(colors[g])
    g_dic_ry_err_up[g].Draw("C")
    g_dic_ry_err_do[g].SetLineWidth(2)
    g_dic_ry_err_do[g].SetLineColor(colors[g])
    g_dic_ry_err_do[g].Draw("C")

lg.Draw()


c_ry.SaveAs('ry_vslumi%s.eps'%name)
c_ry.SaveAs('ry_vslumi%s.png'%name)
#####################################################################################

first=True
c_afb=r.TCanvas('c','c',600,600)
lg = r.TLegend(0.6,0.7,0.9,0.9)
lg.SetFillStyle(0)
lg.SetLineColor(0)
lg.SetBorderSize(0)
lg.SetShadowColor(10)
lg.SetTextSize(0.040)
lg.SetTextFont(42)
lg.SetNColumns(3)
for g in reversed(sorted(g_dic_afb.keys())):

    g_dic_afb[g].SetMarkerColor(colors[g])
    g_dic_afb[g].SetLineColor(colors[g])
    g_dic_afb[g].SetFillColor(colors[g])
    g_dic_afb[g].SetLineWidth(2)

    lg.AddEntry(g_dic_afb[g],names[g],"f")
    if first:
        first=False
        g_dic_afb[g].SetMaximum(0.15)
        g_dic_afb[g].SetMinimum(-0.35)
        g_dic_afb[g].SetLineColor(colors[g])
        g_dic_afb[g].SetLineWidth(-2002)
        g_dic_afb[g].SetFillColor(colors[g])
        g_dic_afb[g].SetFillStyle(3002)

        g_dic_afb[g].SetTitle("A_{FB} versus Int. Lumi ")
        g_dic_afb[g].GetXaxis().SetTitle( "Int. Lumi (ab^{-1})" )
        g_dic_afb[g].GetYaxis().SetTitle( "A_{FB}" )
        g_dic_afb[g].GetYaxis().SetTitleOffset(1.3)
        g_dic_afb[g].Draw("A3")
#        g_dic_afb[g].Draw("3")


    else:
        g_dic_afb[g].SetLineColor(colors[g])
        g_dic_afb[g].SetLineWidth(0)
        g_dic_afb[g].SetFillColor(colors[g])
        g_dic_afb[g].SetFillStyle(3002)
        #g_dic_afb[g].Draw("AB1")
        g_dic_afb[g].Draw("3")

    g_dic_afb_err_up[g].SetLineWidth(2)
    g_dic_afb_err_up[g].SetLineColor(colors[g])
    g_dic_afb_err_up[g].Draw("C")
    g_dic_afb_err_do[g].SetLineWidth(2)
    g_dic_afb_err_do[g].SetLineColor(colors[g])
    g_dic_afb_err_do[g].Draw("C")

lg.Draw()


c_afb.SaveAs('afb_vslumi%s.eps'%name)
c_afb.SaveAs('afb_vslumi%s.png'%name)
#####################################################################################



#####################################################################################
#####################################################################################
samples=['p8_pp_ZprimeSSM_6TeV_ll',
         'p8_pp_ZprimeCHI_6TeV_ll',
         'p8_pp_ZprimeETA_6TeV_ll',
         'p8_pp_ZprimeLRM_6TeV_ll',
         'p8_pp_ZprimePSI_6TeV_ll',
         'p8_pp_ZprimeI_6TeV_ll'
]

#samples=['p8_pp_ZprimeSSM_4TeV_ll',
#         'p8_pp_ZprimeCHI_4TeV_ll',
#         'p8_pp_ZprimeETA_4TeV_ll',
#         'p8_pp_ZprimeLRM_4TeV_ll',
#         'p8_pp_ZprimePSI_4TeV_ll',
#         'p8_pp_ZprimeI_4TeV_ll'
#         ]

#samples=['p8_pp_ZprimeSSM_Interf_6TeV_ll',
#         'p8_pp_ZprimeETA_Interf_6TeV_ll',
#         'p8_pp_ZprimeCHI_Interf_6TeV_ll',
#         'p8_pp_ZprimeLRM_Interf_6TeV_ll',
#         'p8_pp_ZprimePSI_Interf_6TeV_ll',
#         'p8_pp_ZprimeI_Interf_6TeV_ll']
g_dic_m_ry={}
g_dic_m_afb={}
ssplit=3
if "Interf" in samples[0]: ssplit=4
startmass=samples[0].split('_')[ssplit]
startmass=startmass.replace('TeV','')
startmass=int(startmass)
masses=[x*200.+startmass for x in xrange(10)]

for s in samples:
    lumi=1000.*15
    val=[]

    ry = array( 'd' )
    afb = array( 'd' )
    afb_err = array( 'd' )
    ry_err = array( 'd' )
    mass_arr = array( 'd' )
    dummyr = array( 'd' )


    for m in masses:
        m_min=m-100.
        m_max=m+100.
        if "Interf" not in s: val=get_values(lumi, s, 'backgrounds',m_min, m_max, False, 0.05)
        else: val=get_values(lumi, s, '',m_min, m_max)
        
        ry.append(val[0])
        ry_err.append(val[1])
        afb.append(val[2])
        afb_err.append(val[3])
        mass_arr.append(m/1000.)
        dummy.append(200)

    g_dic_m_ry[s]=r.TGraphErrors(len(mass_arr),mass_arr,ry,dummy,ry_err)
    g_dic_m_afb[s]=r.TGraphErrors(len(mass_arr),mass_arr,afb,dummy,afb_err)



c_ry_m=r.TCanvas('c','c',600,600)
lg = r.TLegend(0.6,0.7,0.9,0.9)
lg.SetFillStyle(0)
lg.SetLineColor(0)
lg.SetBorderSize(0)
lg.SetShadowColor(10)
lg.SetTextSize(0.040)
lg.SetTextFont(42)
lg.SetNColumns(3)
first=True
for g in reversed(sorted(g_dic_m_ry.keys())):
    g_dic_m_ry[g].SetMarkerColor(colors[g])
    g_dic_m_ry[g].SetLineColor(colors[g])
    g_dic_m_ry[g].SetFillColor(colors[g])
    g_dic_m_ry[g].SetLineWidth(2)

    lg.AddEntry(g_dic_m_ry[g],names[g],"f")
    if first:
        first=False   
        g_dic_m_ry[g].SetMaximum(0.8)
        g_dic_m_ry[g].SetMinimum(0.4)     
        g_dic_m_ry[g].SetTitle("r_{y} versus Int. Lumi ")
        g_dic_m_ry[g].GetXaxis().SetTitle( "Mass GeV" )
        g_dic_m_ry[g].GetYaxis().SetTitle( "r_{y} (x=%s)"%(str(ry_val)) )
        g_dic_m_ry[g].GetYaxis().SetTitleOffset(1.3)
        g_dic_m_ry[g].Draw("ACP")
    else:
        g_dic_m_ry[g].Draw("C")

lg.Draw()
lum_t.DrawLatex(5.2,0.75,"%i ab^{-1}"%(int(lumi/1000.)))
c_ry_m.SaveAs('ry_vs_m.eps')
c_ry_m.SaveAs('ry_vs_m.png')
#        g_dic_ry[g].Draw("3")



c_afb_m=r.TCanvas('c','c',600,600)
lg = r.TLegend(0.6,0.7,0.9,0.9)
lg.SetFillStyle(0)
lg.SetLineColor(0)
lg.SetBorderSize(0)
lg.SetShadowColor(10)
lg.SetTextSize(0.040)
lg.SetTextFont(42)
lg.SetNColumns(3)
first=True
for g in reversed(sorted(g_dic_m_afb.keys())):
    g_dic_m_afb[g].SetMarkerColor(colors[g])
    g_dic_m_afb[g].SetLineColor(colors[g])
    g_dic_m_afb[g].SetFillColor(colors[g])
    g_dic_m_afb[g].SetLineWidth(2)

    lg.AddEntry(g_dic_m_afb[g],names[g],"f")
    if first:
        first=False   
        g_dic_m_afb[g].SetMaximum(0.2)
        g_dic_m_afb[g].SetMinimum(-0.45)   
        g_dic_m_afb[g].SetTitle("r_{y} versus Int. Lumi ")
        g_dic_m_afb[g].GetXaxis().SetTitle( "Mass TeV" )
        g_dic_m_afb[g].GetYaxis().SetTitle( "A_{FB}" )
        g_dic_m_afb[g].GetYaxis().SetTitleOffset(1.3)
        g_dic_m_afb[g].Draw("ACP")
    else:
        g_dic_m_afb[g].Draw("C")

lg.Draw()
lum_t.DrawLatex(5.2,0.15,"%i ab^{-1}"%(int(lumi/1000.)))
c_afb_m.SaveAs('afb_vs_m.eps')
c_afb_m.SaveAs('afb_vs_m.png')
#        g_dic_ry[g].Draw("3")
