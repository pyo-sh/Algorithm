import java.util.*;
public class N_8393{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n, sum=0;
        n = sc.nextInt();
        for(int i=1;i<=n;i++)
            sum += i;
        System.out.println(sum);
        sc.close();
    }
}