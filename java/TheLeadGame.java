package checl;


import java.util.Scanner;

public class TheLeadGame {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
	int x=in.nextInt();
	int s1=0,s2=0,max=0;
	int flag=0;
	if(x<=10000)
	for(int i=0;i<x;i++)
	{
		int n1=in.nextInt();
		int n2=in.nextInt();
		
		s1=s1+n1;
		s2=s2+n2;
		if(s1>s2 && (s1-s2)>max)
		{
			flag=1;
			max=s1-s2;
			
		}
		else if(s1<s2 && (s2-s1)>max)
		{
			flag=2;
			max=s2-s1;
		}
	}
	
	System.out.println(flag+" "+max);
	}

}
