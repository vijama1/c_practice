#include<stdio.h>
int main()
{
  int num;
  int f=1;
  printf("Enter your number");
  scanf("%d",&num);
  for(int i=1;i<=num;i++)
  {
    f=f*i;
  }
  printf("The factorial is %d\n",f );
}
