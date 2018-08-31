import ROOT as r
import glob
from array import array

models=['SSM','ETA','CHI','LRM','PSI','I']

XSEC={'SSM':0.00127705,
      'ETA':0.000373203,
      'CHI':0.000658995,
      'LRM':0.000787521,
      'PSI':0.000319221,
      'I':0.000515749,
}

fits_mumu=glob.glob('Outputs/helhc_v01/Zprime/mumu/Zprime_mumu_6TeV*/Fits/*.txt')
fits_ee=glob.glob('Outputs/helhc_v01/Zprime/ee/Zprime_ee_6TeV*/Fits/*.txt')
fits_ll=glob.glob('Outputs/helhc_v01/Zprime/ll/Zprime_ll_6TeV*/Fits/*.txt')



def dograph(fits, iscomb, name):

    Errors={}


    for fname in fits:
        mod='SSM'
        print fname
        model=fname.split('/')[-1]
        model=model.replace('.txt','')
        model=model.split('_')
        if model[3]!='':mod=model[3]
        lumi=model[4]
        print 'model ',mod,'  lumi ',lumi
        f = open(fname, 'r')
        for line in f:
            if 'SigXsecOverSM' in line:
                line=line.replace('\n','')
                line=line.split(' ')
                up=line[3]
                down=line[4]
                try:
                    Errors[mod].update({lumi:[up,down]})
                except KeyError:
                    Errors[mod]={lumi:[up,down]}

    print Errors



    graph_dic = {}

    for key, value in sorted(Errors.iteritems()):
        lumiArray = array( 'd' )
        dummy = array( 'd' )
        xsecArray = array( 'd' )
        xsec_err_up = array( 'd' )
        xsec_err_do = array( 'd' )
        print key
        for key2, value2 in sorted(value.iteritems()):
            print key2,value2
        
            xsec=XSEC[key]
            if iscomb:xsec=xsec*2./3.
            else:xsec=xsec/3.
            lumiArray.append(float(key2)/1000000.)
            xsecArray.append(xsec*1000000.)
            xsec_err_up.append(xsec*1000000.*float(value2[0]))
            xsec_err_do.append(abs(xsec*1000000.*float(value2[1])))
            dummy.append(0)

            print 'lumiArray  ',lumiArray
            print 'xsecArray  ',xsecArray
            print 'xsec up    ',xsec_err_up
            print 'xsec do    ',xsec_err_do

            graph_dic[str(key)]= r.TGraphAsymmErrors(len(dummy), lumiArray, xsecArray,dummy,dummy,xsec_err_do,xsec_err_up)



    lg = r.TLegend(0.6,0.7,0.9,0.9)
    lg.SetFillStyle(0)
    lg.SetLineColor(0)
    lg.SetBorderSize(0)
    lg.SetShadowColor(10)
    lg.SetTextSize(0.040)
    lg.SetTextFont(42)
    lg.SetNColumns(3)

    colors={'SSM':1, 'LRM':2, 'PSI':4, 'CHI':8, 'ETA':6, 'I':7}

    graph_dic['SSM'].SetMaximum(600)
    graph_dic['SSM'].SetMinimum(0.)
    graph_dic['SSM'].SetMarkerColor(colors['SSM'])
    graph_dic['SSM'].SetLineColor(colors['SSM'])
    graph_dic['SSM'].SetLineWidth(colors['SSM'])
    graph_dic['SSM'].SetFillColor(colors['SSM'])
    graph_dic['SSM'].SetFillStyle(3001)

    graph_dic['SSM'].SetTitle("Fitted #sigma versus Int. Lumi ")
    graph_dic['SSM'].GetXaxis().SetTitle( "Int. Lumi (ab^{-1})" )
    graph_dic['SSM'].GetYaxis().SetTitle( "Fitted #sigma (ab)" )
    graph_dic['SSM'].GetYaxis().SetTitleOffset(1.3)

   
    graph_dic['PSI'].SetMarkerColor(colors['PSI'])
    graph_dic['PSI'].SetLineColor(colors['PSI'])
    graph_dic['PSI'].SetLineWidth(2)
    graph_dic['PSI'].SetFillColor(colors['PSI'])
    graph_dic['PSI'].SetFillStyle(3001)

    graph_dic['CHI'].SetMarkerColor(colors['CHI'])
    graph_dic['CHI'].SetLineColor(colors['CHI'])
    graph_dic['CHI'].SetLineWidth(2)
    graph_dic['CHI'].SetFillColor(colors['CHI'])
    graph_dic['CHI'].SetFillStyle(3001)

    graph_dic['I'].SetMarkerColor(9)
    graph_dic['I'].SetLineColor(9)
    graph_dic['I'].SetLineWidth(2)
    graph_dic['I'].SetFillColor(9)
    graph_dic['I'].SetFillStyle(3001)

    graph_dic['LRM'].SetMarkerColor(colors['I'])
    graph_dic['LRM'].SetLineColor(colors['I'])
    graph_dic['LRM'].SetLineWidth(2)
    graph_dic['LRM'].SetFillColor(colors['I'])
    graph_dic['LRM'].SetFillStyle(3001)

    graph_dic['ETA'].SetMarkerColor(colors['ETA'])
    graph_dic['ETA'].SetLineColor(colors['ETA'])
    graph_dic['ETA'].SetLineWidth(2)
    graph_dic['ETA'].SetFillColor(colors['ETA'])
    graph_dic['ETA'].SetFillStyle(3001)


    lg.AddEntry(graph_dic['SSM'],"SSM","f")
    lg.AddEntry(graph_dic['PSI'],"#psi","f")
    lg.AddEntry(graph_dic['CHI'],"#chi","f")
    lg.AddEntry(graph_dic['LRM'],"LRM","f")
    lg.AddEntry(graph_dic['ETA'],"#eta","f")
    lg.AddEntry(graph_dic['I'],"I","f")

    c=r.TCanvas('c','c',600,600)
    graph_dic['SSM'].Draw("ACP")
    graph_dic['SSM'].Draw("3")

    graph_dic['PSI'].Draw("C")
    graph_dic['PSI'].Draw("3")

    graph_dic['CHI'].Draw("C")
    graph_dic['CHI'].Draw("3")

    graph_dic['LRM'].Draw("C")
    graph_dic['LRM'].Draw("3")

    graph_dic['ETA'].Draw("C")
    graph_dic['ETA'].Draw("3")

    graph_dic['I'].Draw("C")
    graph_dic['I'].Draw("3")

    lg.Draw()
    c.SaveAs('sigma.png')



dograph(fits_ee, False,'ee')
