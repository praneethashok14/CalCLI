# include <stdio.h>
int
main()
{
int ans,meth,num1,num2=0;
printf("Enter number 1: ");
scanf("%d",&num1);
printf("Enter number 2: ");
scanf("%d",&num2);
while(1)
{
   
 printf("Choose method:\n1: Add\n2: Subtract\n3: Multiply\n4: Divide\n5: Terminate\nEnter choice:");
scanf("%d", &meth);
if (meth==1)
   printf("Answer (you selected: addition): = %d\n",(num1+num2));
if (meth==2)
   printf("Answer (you selected: subtraction): = %d\n",(num1-num2));
if (meth==3)
   printf("Answer (you selected: multiplication): = %d\n",(num1*num2));
if (meth==4)
   printf("Answer (you selected: division): = %d\n",(num1/num2));
if (meth==5)
break;
}


    return 0;
}