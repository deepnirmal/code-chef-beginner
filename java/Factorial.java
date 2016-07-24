package checl;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

public class Factorial {

	public static void main(String[] args) {
		
		ArrayList<Integer> nums= new ArrayList<Integer>();
		Scanner in = new Scanner(System.in);
		
		int x = in.nextInt();
		if(x<=100000)
		{
			for(int i=0;i<x;i++)
			{
				nums.add(in.nextInt());
			}
			
			
			for(int i=0;i<x;i++)
			{
				
			
				
				int num= nums.get(i);
				
				int ctr=0;
				while(num>0)
				{
					num=num/5;
					ctr=ctr+num;
				}

				
				System.out.println(ctr);
				
			}
		}

	}
	
}


