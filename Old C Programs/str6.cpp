//programs to count words and digit 

#include <stdio.h>

int main()
{
	int a, i, alpha=0, space=0, digit=0, spchar=0;
	char x[50];
	
	printf("Enter the string :\n");
	gets(x);
	
	for( i=0; x[i]!='\0'; i++ )
	{
		
		if( x[i]>='a'&&x[i]<='z' || x[i]>='A'&&x[i]<='Z' )
		alpha++;
		else if (x[i]==' ')
		space++;
		else if(x[i]>= '0' &&x[i]<= '9')
		digit++;
		else
		spchar++;
	}

	printf("\nTotal alphabets in string are : %d\n",alpha);
	printf("Total Spaces in strings are : %d\n",space);
	printf("Total words in strings are : %d\n",space+1);
	printf("Total digits in string are : %d\n",digit);
	printf("Total special charcters in string are : %d\n",spchar);
	printf("Total characters in strings are : %d\n\n",alpha+space+spchar+digit);
	
	return 0;
}
