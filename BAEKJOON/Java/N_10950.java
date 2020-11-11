import java.util.*;
public class N_10950{
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int A, B, T;
        T = scan.nextInt();
        scan.nextLine();
        for(int i=0; i < T; i++){
            A = scan.nextInt();
            B = scan.nextInt();
            scan.nextLine();
            System.out.println(A + B);
        }
        scan.close();
    }
}