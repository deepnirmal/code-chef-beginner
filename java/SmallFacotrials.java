package checl;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

public class SmallFacotrials {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		ArrayList<Integer> nums= new ArrayList<Integer>();
		long x=in.nextInt();
		if(x>0 && x<=100)
		{
			for(int i=0;i<x;i++)
			nums.add(in.nextInt());
				
			for(int i=0;i<x;i++)
			{
				
			int num = nums.get(i);
			if(num>0 && num<=100)
			System.out.println(facto(num));
			}
			
		}

		
		
		

	}
	public static BigInteger facto(int x)
	{
		
		BigInteger fact= new BigInteger("1");
		for(int i=1;i<=x;i++)
			fact= fact.multiply(new BigInteger(i+""));

		return fact;

	}

}
