//strings operation without using string.h

#include<stdio.h>
int main()
{
	int x, i, j, p=0, q, r=0, s=0; 
	char a[30], b[30], c[40] ; 
	
	printf("\n\tSring operations\n") ; 
	printf("***********************************\n\n") ; 
	
	printf("1.\tLength of string\n2.\tString Concatination"); 
	printf("\n3.\tReverse the string\n4.\tCopy the string\n"); 
	printf("5.\tTo convert the string in upper case\n");
	printf("6.\tTo convert the string in lower case\n\n");
	scanf("%d", &x) ; 
	
	if(x==1)
	{
		printf("Enter the string :\n") ; 
		fflush(stdin) ; 
		gets(a) ; 
		for(i=0; a[i]!='\0'; i++) 
		p++ ; 
		printf("The length of your string is : %d", p) ; 
	}
	
	else if(x==2) 
	{
		printf("Enter the first string :\n") ; 
		fflush(stdin) ; 
		gets(a) ; 
		printf("Enter the second string :\n") ; 
		fflush(stdin) ; 
		gets(b) ; 
		for(i=0; a[i]!='\0';i++) 
		{
			
			c[i]=a[i] ;
		}
		c[i]='\0' ; 
		for(j=0; b[j]!='\0'; j++) 
		{
			
			c[i+j]=b[j] ; 
		}
		c[i+j]='\0' ; 
		printf("the concatinated string is :\n") ; 
		puts(c) ; 
	}
	
	else if(x==3) 
	{
		
		printf("\n\nEnter anything to reverse :\n") ; 
		
		fflush(stdin) ; 
		gets(a) ; 
		
		while(a[r]!='\0') 
		
		{
			r++ ; 
		}
		
		for(i=r-1; i>=0; i--) 
		{
			
			b[s]=a[i] ; 
			s++ ; 
		}
		
		b[s]='\0' ; 
		printf("\nThe reversed string is: \n") ; 
		printf("\n%s\n",b) ; 
	}
	
	else if(x==4)
	{
		printf("Enter the string :\n");
		fflush(stdin);
		gets(a);
		for(i=0; a[i]!='\0'; i++)
		{
			b[i]=a[i];
		}
		printf("\nThe length of the sting entered is : %d\n",i);
		printf("The copied string is :\n");
		puts(b);
	}
	
	else if(x==5)
	{
		printf("Enter the string : \n");
		fflush(stdin);
		fgets(a, sizeof(a),stdin);
		for(i=0; a[i]!='\0'; i++)
		{
			if(a[i]>='a'&& a[i]<='z')
			a[i] = a[i]-32 ;
		}
		printf("\nThe uppercase string is :\n");
		puts(a);
	}
	
	else if(x==6)
	{
		printf("Enter the string : \n");
		fflush(stdin);
		gets(a);
		for(i=0; a[i]!='\0'; i++)
		{
			if(a[i]>='A' && a[i]<='Z')
			{
				a[i]=a[i]+32;
			}
		}
		printf("The lowercase string is :\n");
		puts(a);
	}
	
	else
	{
		printf("\nplease enter the valid number to prform operation\n");
		printf("Thank you");
	}
	
	return 0 ; 
	
}

