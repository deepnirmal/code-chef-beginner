import java.util.Scanner;


public class balloons {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in) ;
		
	int n=in.nextInt() ;
	int i;
	for(i=0;i<n;i++) 
	{
		String str=new String();
		str=in.next();
		int ctrA=0,ctrB=0,j ;
		for(j=0;j<str.length();j++)
		{
			if(str.charAt(j)=='a')
			{
				ctrA++ ;
			}
			else
				ctrB++;
				
		}
		if(ctrA<ctrB)
		System.out.println(ctrA);
		else
			System.out.println(ctrB);
	}
		
		
	}

}
