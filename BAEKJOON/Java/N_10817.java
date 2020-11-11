import java.util.*;
public class N_10817 {
 public static void main(String[] args) {
  Scanner sc = new Scanner(System.in);
  int A, B, C, temp;
  A = sc.nextInt();
  B = sc.nextInt();
  C = sc.nextInt();
  temp = A;
  if((B>=A&&B<=C)||(B>=C&&B<=A))
   temp = B;
  if((C>=A&&C<=B)||(C>=B&&C<=A))
   temp = C;
  System.out.println(temp);
  sc.close();
 }
}