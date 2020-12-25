#include<stdio.h>
#include<conio.h>

char name[50];
int age;
int i;
int weight;
char ill[5];
int illdays;
int eat;
int water;
char exercise[5];
int height;
int junk;
char ask[5];

int cold;

int fever;
int stomach;
int headache;
int stress;
int pain;   


int main()
{


intro();


printf("\nPlease Enter Your First Name\n");

scanf("%s", name);

printf("\nEnter Your Age\n");

scanf("%d",&age);


printf("\nEnter Your Weight\n");

scanf("%d",&weight);

printf("\nEnter Your Height(in cm)\n");

scanf("%d",&height);

printf("\nSo Let's Start Inspection\n ");

printf("\nDid you have any major diseases from the following?\nIf yes then type no. of disease or type 0\n");

printf("\nHeart Disease   Diabities  Cancer            TB             \n");

printf("\nSugar           pneumonia  Kidney Stone      Skin Infection \n");

printf("\nAsthma          AIDS       Arthriis          Covid-19       \n");

printf("\nSevere Cold     Sinus      Dengue            Malaria        \n");

printf("\nTyphoid         Polio      Dog Infection     Fungual        \n");

printf("\nSwine Flu       Jaundice   Any Infection     Impairment     \n");

scanf("%d",&i);

printf("\nDid you become ill frequently? (In Yes or No)\n");

scanf("%s",ill);

if(!strcmp(ill, "yes") || !strcmp(ill, "yes"))
{
  printf("In how many days you become ill?\n");   
  
  scanf("%d",&illdays);          
}
       
printf("In A day How many time you eat?\n");

scanf("%d",&eat);

printf("In A day How many time you eat Junk Food?\n");

scanf("%d",&junk);

printf("In A day How many glass of water you drink?\n");

scanf("%d",&water);

printf("Do you exercise daily? (In Yes or No)\n");

scanf("%s",exercise);



printf("\nYou given all information.Do You want to answer of frequent illness (so we can give remedies)? Press Yes or No (If not we will give remedies about illness)\n");

scanf("%s",ask);
if(!strcmp(ask, "yes") || !strcmp(ask, "yes"))
{
  frequentill();
              
                 } 
            else{ printf("\nOk Thank You for you precious  Time.\n");
                 } 

report();




 getch();
 return 0;
    
    
}

int intro()
{
    

    
printf("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to Online Health Checkup\t\t\t\n");
    
printf("\nCreated By Indie_Coder (Pankaj Keshav Borade)\n");

printf("\nFor Better Experience Open In Full Screen Mode &  Press Enter After Entering Data\n");
}




int frequentill()
{


printf("\nOne By One 5 minor diseases questions will come?\nPress 0 for No or Press 1 for Yes\n");

printf("Do you become ill from Common Cold frequently?\n");

scanf("%d",&cold);



printf("Do you become ill from Fever frequently?\n");

scanf("%d",&fever);

printf("Do you become ill from Stomach Pain frequently?\n");

scanf("%d",&stomach);

printf("Do you become ill from HeadAche frequently?\n");

scanf("%d",&headache);

printf("Do you become ill from Stress frequently?\n");

scanf("%d",&stress);

printf("Do you feel Pain in Joints frequently?\n");

scanf("%d",&pain);
}






int report()
{
 printf("\nDone\n");   
 
 printf("\n                                                                                               Your Given Information  \n");

printf("\nYour Name: %s\n",name);

printf("\nAge: %d\n",age);

printf("\nWeight: %d\n",weight);

printf("\nHeight: %d\n",height);


printf("\n                                                                                                %s's Health Report  \n",name);
 
if(age >=15 && age<= 17){
     printf("\n--> You are a teenager\n");
     
      if(weight<=45 && height<=150){
      printf("\n-->You are underweight & height is bit small acc. to your age. Must eat daily 2 to 3 banana and try skipping to icrease height. \n");
      }
      else if(weight<=45 && height >150 ) {
      printf("\n-->You are underweight & height is perfect acc. to your age. Must eat daily 2 to 3 banana.\n");
      }
      else if(weight > 45 && height<=150 && weight <=70 ) {
      printf("\n-->You are weight is perfect but height is bit small acc. to your age. Maitain weight like this & try skipping to icrease height.\n");
      }
      else if(weight<=70 && height >150 && weight > 45) {
      printf("\n-->You are weight is perfect & height is perfect acc. to your age. Maintain weight like this..\n");
      }
      if(weight >70 && height<=150){
      printf("\n-->You are overweight & height is bit small acc. to your age. Must you only eat 2 Times a day also take one fast in week and try skipping to icrease height. \n");
      }
      else if(weight > 70 && height>=151 ) {
      printf("\n-->You are overweight & height is perfect acc. to your age. Must you only eat 2 Times a day also take one fast in week.\n");
      }
     }
else if(age >=1 && age<= 14) {
      printf("\n--> You are kid\n");
      
      printf("\n Your Weight & Height is Normal.\n");
      }
else if(age >=18) {
      printf("\n--> You are adult");
      
         if(weight<=45 && height<=150){
      printf("\n-->You are underweight & height is bit small acc. to your age. Must eat daily 2 to 3 banana and try skipping to icrease height. \n");
      }
      else if(weight<=45 && height >150 ) {
      printf("\n-->You are underweight & height is perfect acc. to your age. Must eat daily 2 to 3 banana.\n");
      }
      else if(weight > 45 && height<=150 && weight <=70 ) {
      printf("\n-->You are weight is perfect but height is bit small acc. to your age. Maitain weight like this & try skipping to icrease height.\n");
      }
      else if(weight<=70 && height >150 && weight > 45) {
      printf("\n-->You are weight is perfect & height is perfect acc. to your age. Maintain weight like this..\n");
      }
      if(weight >70 && height<=150){
      printf("\n-->You are overweight & height is bit small acc. to your age. Must you only eat 2 Times a day also take one fast in week and try skipping to icrease height. \n");
      }
      else if(weight > 70 && height>=151 ) {
      printf("\n-->You are overweight & height is perfect acc. to your age. Must you only eat 2 Times a day also take one fast in week.\n");
      }
      }
      
if(i ==0)
{
     printf("\n-->Very Good you don't have any Major Disease. Try to avoid Junk Food & go through Yoga each day.\n");
}  
   else if(i == 1)
   {
         printf("\n-->You have one disease. Try to avoid Junk Food & go through Yoga each day.No worry it will cure soon.\n");
        }    
        
   else if(i >= 2)
   {
         printf("\n-->You have Disease. Try to avoid Junk Food & go through Yoga each day.No worry it will cure soon.\n");
        }  
        
if(!strcmp(ill, "yes") || !strcmp(ill, "yes"))
{
  if(illdays<30)
  {
      printf("\n-->You should eat healthy food not junk food at all.Try to wake up at early morning & do Yoga.");
                } 
                
  if(illdays>=30)
  {
     printf("\n-->Majority people come in this slot of frequent disease but it is not good.\n");
                 } 
                      
}
else{
     printf("\n--.Excellent You don't become ill frequently.Maintain this by avoiding Junk Food.\n");
     }
      
if(eat ==0)
{
     printf("\n-->You should eat two times a day.It can give weakness.\n");
}  
   else if(eat == 1)
   {
         printf("\n-->One time eating in a day is not enough for your body.You should eat atleast 2 Times.\n");
        }    
        
        else if(eat >= 2 && eat <= 3)
   {
         printf("\n-->Your eating habit is perfect.\n");
        }    
        
   else if(eat >= 4)
   {
         printf("\n-->Your Eating is very bad.You should eat only 2-3 Times.\n");
        } 
      
        
if(junk ==0)
{
     printf("\n-->Very Good you don't eat in any junk food.Maintain this good habbit.\n");
}  
   else if(junk == 1)
   {
         printf("\n-->It's Ok you eat only one time in day. This means 7 times a week.You should eat atmost 3 Times a week.\n");
        }    
        
   else if(junk >= 2)
   {
         printf("\n-->Eating Junk Food is very bad health.It can increase fat & your body becomes weaks  from internally.You should eat only 1 times in day.\n");
        } 
      
if(water ==0)
{
     printf("\n-->You don't drink water in a day.You are Joking.Water is needed for basic function to run in body. You should drink atleast 8 glass of water in day.\n");
}  
   else if(water >= 1 && water <=7)
   {
         printf("\n-->You should drink minimum 8 glass of Water.\n");
        }    
        
   else if(water >= 8)
   {
         printf("\n-->As considering glasses of water.It is fine.\n");
        } 
        
if(!strcmp(exercise, "yes") || !strcmp(exercise, "yes"))
{
  printf("\n-->You exercise & yoga do daily it is very good.Keep it up\n");
              
                 } 
            else{ printf("\n-->You should do exercise & yoga daily 1 hour.It will strength mentally & physically.\n");
                 } 


if(!strcmp(ask, "yes") || !strcmp(ask, "yes"))
{
  printf("\nYou become ill frequently by this\n");
  if(cold == 1)
  {
          printf("\n-->Common Cold");
          }  
          
   if(fever == 1)
  {
          printf("\n-->Fever");
          }    
          
      if(headache == 1)
  {
          printf("\n-->HeadAche");
          }  
          
      if(stomach == 1)
  {
          printf("\n-->Stomach Pain");
          }   
          
     if(stress == 1)
  {
          printf("\n-->Stress");
          }  
          
      if(pain == 1)
  {
          printf("\n-->Pain In Joints");
          }    
                 } 

printf("\n\nHere is the Remedies\n\n");                 
printf("\nFor Cold: 1.Drink Warm Water 2.Gargle with Hot Water 3.Take Steam 4.Stay Warm  5.Contact Doctor immeaditely if cold is more than 4 Days\n");              
printf("\nFor Fever: 1.Drink More Water 2.Take More Rest 3.Use Blankets for sweat to come 4.Contact Doctor immeaditely after 2 days if fever is there.\n");
printf("\nFor Headache: 1.Take Rest 2.Don't drink cold water 3.Use Hot Steam 4.Contact Doctor immeaditely after 1 days if headache is there.\n");
printf("\nFor Stress: 1.Avoid Bad Thoughts 2.Drink More Water 3.Take Rest 4.Do Meditation & Yoga 5.Contact Doctor immeaditely after 1 days if headache is there.\n");

printf("\n\n\nThank You For You Precious Time\n");
}

