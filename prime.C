#include<stdio.h>
int main()
{
  int num;
  int count=0;
  printf("Enter your number");
  scanf("%d",&num);
  for(int i=2;i<num;i++)
  {
    if(num%i==0)
    count=count+1;
    else
    continue;
  }
  if(count>0)
  printf("Number is not prime");
  else
  printf("number is prime\n");
}
