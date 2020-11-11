import java.util.Scanner;
public class N_2588{
    public static void main(String[] args){
        Scanner io = new Scanner(System.in);
        int a,b;
        a = io.nextInt();
        b = io.nextInt();
        System.out.println(a*((b-((b/10)*10))));
        System.out.println(a*((b-((b/100)*100))/10));
        System.out.println(a*(b/100));
        System.out.println(a*b);
        io.close();
    }
}