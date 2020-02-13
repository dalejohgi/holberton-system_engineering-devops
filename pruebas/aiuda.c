#include <stdio.h>
int main(void)
{
 char n;
 char m;

	for(n = 48; n <= 57; n++)
	{				
		for(m = 48; m <= 57; m++)
			{
			putchar(n);
			putchar(m);
			if (n == 57 && m == 57)
				{
				break;
				}	
		putchar(',');
		putchar(' ');

			}			

	}	
	putchar('\n');


return(0);
}
