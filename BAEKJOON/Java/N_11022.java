import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class N_11022{
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int a, b, num = Integer.parseInt(in.readLine());
        String s, array[];
        for(int i = 1; i <= num; ++i){
            s = in.readLine();
            array = s.split(" ");
            a = Integer.parseInt(array[0]);
            b = Integer.parseInt(array[1]);
            out.write("Case #" + i + ": " + a + " + " + b + " = " + (a+b) + "\n");
        }
        out.flush();
        in.close();
        out.close();
	}
}
