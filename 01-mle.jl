n=50;
S=range(1.,n,step=0.1);
L(S,o)=S*log(o)+(n-S)*log(1. -o); #funtion defination for plot
o=range(0.1,0.9,length=100);
#import Pkg; 
#Pkg.add("Plots")
using Plots  #using the plot to plot the surface plot
gr()
p2=Plots.heatmap(S,o,(S,o)->L(S,o),color=:jet, xlabel="S", ylabel="o",title="Bird eye view");
SS=25;  #adding a line in the plot at 25
vline!([SS],label=false,color=:black); #Line adding
P3=Plots.plot(o,o->L(SS,o),label=false, xlabel='o',title="L(o|S=$SS)"); #plotting the L(o/ss at ss=25);
p1=Plots.plot(p2,P3) #plotting the both subplots in a p[lot
savefig(p1,"01-mle_using_julia.png") ##Saving the figure 