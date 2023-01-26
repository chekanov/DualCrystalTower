import sys
from globalmod import *

myinput="interactive"
if (len(sys.argv) ==2):
   myinput = sys.argv[1]


print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print ('Use as: script.py -b 0 (or 1,2)')

############# Configs ##############
nameX="E [GeV]"
nameY="E(hits) / E"


Xmin=0.3
Xmax=20.0
Ymin=0.95
Ymax=1.01


import sys
epsfig="figs/"+sys.argv[0].replace(".py",".eps")


gROOT.SetStyle("Plain");
xwin=600
ywin=600
c1=TCanvas("c","Mass",10,10,xwin,ywin);
c1.SetFrameBorderMode(0);
ps1 = TPostScript( epsfig,113)
c1.SetTickx()
c1.SetTicky()
c1.SetTitle("")
c1.SetLineWidth(3)
c1.SetBottomMargin(0.12)
c1.SetTopMargin(0.01)
c1.SetRightMargin(0.1)
c1.SetFillColor(0)
c1.SetLeftMargin(0.15)

# c1.SetLogy(1)
c1.SetLogx(1)

h=gPad.DrawFrame(Xmin,Ymin,Xmax,Ymax);
h.Draw()

ax=h.GetXaxis();
ax.SetTitle( nameX );
ay=h.GetYaxis();
ay.SetTitle( nameY );

ax.SetLabelSize(0.04)
ax.SetTitleSize(0.05)
ax.SetTitleOffset(1.0)
ay.SetTitleOffset(1.3)

ay.SetLabelSize(0.04)
ay.SetTitleSize(0.05)
gPad.SetTickx()
gPad.SetTicky()

ay.Draw("same")
ax.Draw("same")


energies=[0.5,1,5,10] 

ptmin=Xmin
ptmax=Xmax
#s1="sqrt(([0]/sqrt(x))*([0]/sqrt(x))+([1]/x)*([1]/x)+[2]*[2])"
s1="([0]/sqrt(x))+[1]"

f1=TF1("f1",s1,ptmin,ptmax);
f1.SetLineStyle(1)
f1.SetLineWidth(2)
f1.SetLineColor(4)
f1.SetParameter(0,0.5)
f1.SetParameter(1,4.58662e-01)
#f1.FixParameter(1,0)
#f1.SetParameter(2,2.02282e-02)


i=0
elec=TGraphErrors()
for e in energies:
      fname="histos/hist_e-_"+str(e)+"gev.root"
      xfile=TFile( fname )
      hh=xfile.Get("heest")
      RMS=rms90(hh); 
      #RMS=hh.GetRMS()
      ERR=hh.GetRMSError()
      MEAN=hh.GetMean()
      MEAN_ERR=hh.GetMeanError()
      print(e," MEAN/E=",MEAN," RMS=",RMS," ERR=",ERR)
      elec.SetPoint(i,e,MEAN)
      elec.SetPointError(i,MEAN_ERR, MEAN_ERR)
      i=i+1
elec.SetLineColor( 1 )
elec.SetMarkerColor( 2 )
elec.SetMarkerSize(1)
elec.SetMarkerStyle(21)
elec.SetLineWidth(3)
elec.SetLineStyle(1)
elec.Draw("][pe same")

leg2=TLegend(0.3, 0.68, 0.89, 0.94);
leg2.SetBorderSize(0);
leg2.SetTextFont(62);
leg2.SetFillColor(10);
leg2.SetTextSize(0.04);
leg2.AddEntry(elec,"Electrons","pl")
leg2.Draw("same");


gPad.RedrawAxis()
c1.Update()


if (myinput != "-b"):
              if (input("Press any key to exit") != "-9999"):
                         c1.Close(); sys.exit(1);

