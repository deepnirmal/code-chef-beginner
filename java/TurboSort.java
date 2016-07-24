package checl;



import java.util.Arrays;

import java.util.Scanner;



public class TurboSort {

	public static void main(String[] args) {
		int x,i;
		Scanner in=new Scanner(System.in);
		x=in.nextInt();
		int array[]=new int[x];
		for(i=0;i<x;i++){
			array[i]=in.nextInt();
			
		}
		Arrays.sort(array);
		for(i=0;i<x;i++){
			System.out.print(array[i]+"\n");
		}

}
}