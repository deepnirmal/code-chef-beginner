package checl;


import java.util.Scanner;

public class EnormousInputTest {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		
		long  n= in.nextInt();
		long  k=in.nextInt();
		int ctr=0;
	
		
		
		if(n<=Math.pow(10, 7) && k<=Math.pow(10, 7))
		{
			for(int i=0;i<n;i++)
			{
				
				int x=in.nextInt();
				if(x<Math.pow(10, 9))
				if(x%k==0)
				{
					ctr++;
				}
			}
			System.out.println(ctr);
			
			
			
			
			
		}

	}

}
