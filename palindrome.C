#include<stdio.h>
int main()
{
  int n,same;
  int rem=0,rev=0;
  printf("Enter the number");
  scanf("%d",&n);
  same=n;
  while(n>0)
  {
    rem=n%10;
    rev=rev*10+rem;
    n=int(n/10);
  }
  if(same==rev)
  {
    printf("\nNumber is palindrome");
  }
  else
  {
    printf("\nNumber is not palindrome");
  }
  return 0;
}
