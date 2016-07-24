package checl;

import java.util.Scanner;

public class ATM {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int withdraw=in.nextInt();
		float balance=in.nextFloat();
		if(withdraw >0 && withdraw<=2000 && balance>0 && balance<=2000)	
		{
		if(withdraw<balance && withdraw%5==0)
		{
			float x=(float) (balance-withdraw-0.50);
			if(x>0.00)
			System.out.println(String.format("%.2f", x));
			else
				System.out.println(String.format("%.2f", balance));
		}
		else 
			System.out.println(String.format("%.2f", balance));

	}}

}
