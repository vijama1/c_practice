#include<stdio.h>
int main()
{
  int n,same,num1,num2;
  int rem=0,rev=0;
  int large=0,remainder1=0,small=2147483647;
  printf("Enter the number:");
  scanf("%d",&n);
  num1=n;
  num2=n;
  same=n;
  while(n>0)
  {
    rem=n%10;
    rev=rev*10+rem;
    n=int(n/10);
  }
  if(same==rev)
  {
    printf("Number is palindrome\n");

    while(num1>0)
    {
      remainder1=num1%10;
      if(remainder1>large)
      {
      large=remainder1;
    }
      num1=int(num1/10);
    }
    printf("Largest number is %d ",large);
  }
  else
  {
    printf("Number is not palindrome\n");
    while(num2>0)
    {
      remainder1=num2%10;
      if(remainder1<small)
      {
      small=remainder1;
    }
      num2=int(num2/10);
    }
    printf("Smallest number is %d ",small);
  }
  return 0;
}
