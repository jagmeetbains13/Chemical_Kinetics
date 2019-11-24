//using root cern

void chem11(){


//set range accordingly

//Giving the data 
//***************************************************************************************************************************
//***************************************************************************************************************************

double x[] = {};    //time

double y[] = {};    //CCC values

double y2[] = {};  //CCT values

double y3[] = {};  //CTT values

int no_data = 0;           //no. of data points

//****************************************************************************************************************************
//****************************************************************************************************************************



TCanvas *c1 = new TCanvas("c1","Chemistry fit",200,10,1000,1000);
TGraph *g = new TGraph(no_data, x, y);
TF1 *f = new TF1("f", "[1]*exp(-1*[0]*x)");

//Fixing paramter
f->FixParameter(1,y[0]);   //fixing y[0] value
g->Fit(f);

//Getting K1 value 
double K1 = f->GetParameter(0);

g->GetYaxis()->SetRangeUser(0,80);
g->GetXaxis()->SetTitle("Time (min)");
g->GetYaxis()->SetTitle("%CCC");
g->Draw("A*");
c1->Update();
c1->Print("K1.pdf)","pdf");




//K2 Fitting


TGraph *g2 = new TGraph(no_data, x, y2);
TCanvas *c2 = new TCanvas("c2","Chemistry fit K2",200,10,1000,1000);
TF1 *f2 = new TF1("f2", "([1]-([2]*([3])/([0]-[3])))*exp(-1*[0]*x) + (([2]*[3])/([0]-[3]))*exp(-1*[3]*x) ");

//Fixing paramter
f2->FixParameter(1,y2[0]);   //fixing y[0] value  29.21
f2->FixParameter(2,y[0]);    // 68.23 
f2->FixParameter(3,K1);


g2->Fit(f2);

//Getting K2 value 
double K2 = f2->GetParameter(0);

g2->GetYaxis()->SetRangeUser(0,50);
g2->GetXaxis()->SetTitle("Time (min)");
g2->GetYaxis()->SetTitle("%CCT");
g2->Draw("A*");
c2->Update();
c2->Print("K2.pdf)","pdf");





//K3 Fitting


TGraph *g3 = new TGraph(no_data, x, y3);
TCanvas *c3 = new TCanvas("c3","Chemistry fit K3",200,10,1000,1000);
TF1 *f3 = new TF1("f", "(([1]-([2]*([3])/([4]-[3])))*([4])/([0]-[4]))*exp(-1*[4]*x) + ((([2]*[3])/([4]-[3]))*([4])/([0]-[3]))*exp(-1*[3]*x) + ([5] - (([1]-([2]*([3])/([4]-[3])))*([4])/([0]-[4])) - ((([2]*[3])/([4]-[3]))*([4])/([0]-[3])))*exp(-1*[0]*x)");

//Fixing paramter
f3->FixParameter(1,y2[0]);   //fixing y[0] value  29.21
f3->FixParameter(2,y[0]); 
f3->FixParameter(3,K1);
f3->FixParameter(4,K2);
f3->FixParameter(5,y3[0]);

g3->Fit(f3);

//Getting K3 value 
double K3 = f3->GetParameter(0);

g3->GetYaxis()->SetRangeUser(0,50);
g3->GetXaxis()->SetTitle("Time (min)");
g3->GetYaxis()->SetTitle("%CTT");
g3->Draw("A*");
c3->Update();
c3->Print("K3.pdf)","pdf");


cout<<"Value of K1 is "<<K1<<endl;
cout<<"Value of K2 is "<<K2<<endl;
cout<<"Value of K3 is "<<K3<<endl;
}
