import java.util.Scanner;

public class N_2753{
    public static void main(String[] args){
        Scanner io = new Scanner(System.in);
        int year = io.nextInt();
        if(year%4 == 0){
            if(year%100 == 0) {
            	if(year%400 == 0)
            		System.out.println(1);
            	else
            		System.out.println(0);
            }
            else
                System.out.println(1);
        }
        else
            System.out.println(0);
        io.close();
    }
}