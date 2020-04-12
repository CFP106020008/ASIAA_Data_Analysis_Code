/***************************************************************************
IRX-beta relation

last updated 14/05/16 by H. Hirashita
****************************************************************************/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double tau(double,double);

int main(int argc,char **argv)
{
   double beta_int,beta,f_IR,f_UV,tauUV;
   double lambda,lambdaUV,lambda1,lambda2,dlambda;

   /* parameter set-up */
   beta_int=-2.2;     /* intrinsic beta */
   lambdaUV=0.16;    /* typical UV wavelength [um] */
   lambda1=0.16;     /* shortest wavelength to determine beta [um] */
   lambda2=0.25;     /* shortest wavelength to determine beta [um] */
   dlambda=0.01;     /* dlambda for integration */

   for(tauUV=1.e-2;tauUV<1.e1;tauUV*=1.2){
     f_IR=0.;
     for(lambda=0.1;lambda<=0.4;lambda+=dlambda){  /* lambda in um */
       f_IR+=pow(lambda,beta_int)*(1.-exp(-tau(lambda,tauUV)));
     }
     f_IR*=dlambda;
     f_UV=pow(lambdaUV,beta_int+1.)*exp(-tau(lambdaUV,tauUV));
     beta=beta_int-log10(exp(1.))*(tau(lambda1,tauUV)-tau(lambda2,tauUV))
               /log10(lambda1/lambda2);
     printf("%le  %le\n",beta,f_IR/f_UV);
   }

   exit(0);
}

double tau(double lambda,double tauUV)
{
  // return(pow(0.16/lambda,2.5)*tauUV);
  return(pow(0.16/lambda,1.3)*tauUV);
}

