import java.util.*;
public class N_10430{
    public static void main(String[] args){
    	int A, B, C;
        Scanner sc = new Scanner(System.in);
        A = sc.nextInt();
        B = sc.nextInt();
        C = sc.nextInt();
        System.out.println(((A+B)%C)+"\n"+((A%C+B%C)%C)+"\n"+((A*B)%C)+"\n"+((A%C*B%C)%C));
        sc.close();
    }
}