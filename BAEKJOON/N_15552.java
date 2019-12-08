import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class N_15552{
    public static void main(String[] agrs) throws Exception{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		int num = Integer.parseInt(in.readLine());
		for(; num!=0; --num) {
			String s = in.readLine();
			String[] array = s.split(" ");
			int a = Integer.parseInt(array[0]);
			int b = Integer.parseInt(array[1]);
			out.write((a+b) + "\n");
		}
		out.flush();
		out.close();
    }
}