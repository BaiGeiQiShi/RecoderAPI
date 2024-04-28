import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class RcdAPI {
    String fileDir = "APItest.py";  //directory of .py
    String pyDir = "python3";  //call the interpreter
    String result = null;

    public void setDir(String dir) {
        fileDir = dir;
    }

    public void setPyDir(String dir) {
        pyDir = dir;
    }

    public String runRecoder(String code , int line, String srcDir, String projectDir) {
        Process proc;
        //code=code.replace(System.lineSeparator(),"$");
        //code = code.replace("\n", "$");
        String linenum = String.valueOf(line);
        String[] command = new String[]{pyDir, fileDir, code, linenum, srcDir, projectDir};
        StringBuilder tempR = new StringBuilder();
        try {
            proc = Runtime.getRuntime().exec(command);  //process command
            BufferedReader input = new BufferedReader(new InputStreamReader(proc.getInputStream()));
            String getLine = null;
            while ((getLine = input.readLine()) != null) {
                tempR.append(getLine).append("\n");
            }
            input.close();
            proc.waitFor();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
        result = tempR.toString();
        return result;
    }
}
