package checl;

import java.util.Scanner;

public class SumsOfTraingle {

	public static void main(String[] args) {
		Scanner in= new Scanner(System.in);
		
		int x = in.nextInt(); 
		
		
		for(int n=0;n<x;n++)
		{
			
			int lines= in.nextInt();
			int[][] array = new int[100][100];
			for(int i=0;i<lines;i++)
				for(int j=0;j<=i;j++)
					array[i][j]=in.nextInt();
			

				
			
		}
		

		
		
	}

	}


