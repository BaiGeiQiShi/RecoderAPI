class test {
    public static void main(String[]args) {
        RcdAPI getTest = new RcdAPI();
	String fDir = "buggy/" + "src/main/java/org/apache/commons/math/complex/Complex.java";
	String pDir = "buggy/" +"src/main/java";
	int linenum = 297;
        String Result = getTest.runRecoder("code", linenum, fDir, pDir);
        System.out.print(Result);
    }
}
