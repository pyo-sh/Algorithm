import java.util.Scanner;

public class N_2884{
    public static void main(String[] args){
        Scanner io = new Scanner(System.in);
        int hour = io.nextInt();
        int minute = io.nextInt();
        if(minute < 45) {
        	if(hour == 0)
        		System.out.println((hour + 24 - 1) + " " + (minute + 60 - 45));
        	else
        		System.out.println((hour - 1) + " " + (minute + 60 - 45));
        }
        else
        	System.out.println(hour + " " + (minute - 45));
    }
}