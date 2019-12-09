import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class N_10871{
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        String s, temp[], array[];
        s = in.readLine();
        temp = s.split(" ");
        int N = Integer.parseInt(temp[0]), X = Integer.parseInt(temp[1]);
        s = in.readLine();
        array = s.split(" ");
        for(int i = 0; i < N; ++i){
            if(Integer.parseInt(array[i]) < X)
                out.write(array[i] + " ");
        }
        out.flush();
        in.close();
        out.close();
	}
}
