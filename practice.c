//arranging words in alphabetical order
#include<stdio.h>
#include<string.h>

int arrange(char str1[50][100])
{
	int i,j;
	char temp[50];
	for(i=0;i<50;i++)
	{
		for(j=i+1;j<50;j++)
		{
			if(strcmp(str1[i],str1[j])>0)
			{
				strcpy(temp,str1[i]);
				strcpy(str1[i],str1[j]);
				strcpy(str1[j],temp);
			}
		}
	}

	printf("The given strings in alphabetical order are:\n");
	for(i=0;i<50;i++)
	{
		printf("%s",str1[i]);
		printf("\n");
	}
		
		
	return 0;
}

int main()
{
	int n;
	char str2[50][100];
	printf("How many strings do you want to enter:\n");
	scanf("%d",&n);
	printf("Enter each string one by one:\n");
	for(int i=0;i<n;i++)
	{
		scanf("%s",str2[i]);
	}
	arrange(str2);
	return 0;
}

	
		
	
