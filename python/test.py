import ROOT as r
import math
h1=r.TH1F('h1','h1',1,0,1)
h2=r.TH1F('h2','h2',1,0,1)

h1.Sumw2()
h2.Sumw2()

bin1_cont = 100343
bin2_cont = 1004329

bin1_err = 10.343
bin2_err = 104.232

h1.SetBinContent(1,bin1_cont)
h2.SetBinContent(1,bin2_cont)

h1.SetBinError(1,bin1_err)
h2.SetBinError(1,bin2_err)


h1.Divide(h2)

print h1.GetBinContent(1),'  ', h1.GetBinError(1)
error=math.sqrt((bin2_err*bin2_err*bin1_cont*bin1_cont + bin1_err*bin1_err*bin2_cont*bin2_cont)/(bin2_cont*bin2_cont*bin2_cont*bin2_cont))
print error

