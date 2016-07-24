package checl;



import java.util.ArrayList;
import java.util.Scanner;

public class LifeUniverseEverything {

	public static void main(String[] args) {
			
			ArrayList<Integer> mylist = new ArrayList<Integer>();
			
			Scanner in = new Scanner(System.in);
			while(in.hasNext())
			{
				mylist.add(in.nextInt());
			}

			for(int i=0;i<mylist.size();i++)
			{
				
				if(mylist.get(i)!=42)
				{
					System.out.println(mylist.get(i));
				}
				else 
					break;
			}
		
			
		
			
	}

}
