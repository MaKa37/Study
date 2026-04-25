package Math;

/* 진리표 생성 규칙
N = 인자의 개수(EX: p, q → 2 = N)
I = 행의 개수(N ^ 2)
J = 열의 개수(N)
interval = 진리값 주기(2 ^ (N - 1 - J))
 */
interface TruthTable{
    
    // 1. 사용하는 변수의 개수를 반환
    int getVaribleCount();

    // 2. 배열을 인자로 받아 연산 수행
    boolean evaluate(boolean[] values);

    // 3. 출력 기호
    String getSymbol();

    // 4. 동적 진리표 생성 디폴트 메서드
    default void printTable() {
        int n = getVaribleCount();
        int rows = (int) Math.pow(2, n);

        // [헤더 출력] p, q, r ... 알파벳 순서대로 출력
        for (int i = 0; i < n; i++){
            System.out.println((char) ('p' + i) + "\t");
        }
        System.out.println("Result(" + getSymbol() + ")");
        System.out.println("---------------------------------");

        // 진리표 데이터 생성 및 출력
        for (int i = 0; i < rows; i++){
            boolean[] condition = new boolean[n]; // 각 행의 T/F 값을 담을 배열

            for (int j = 0; j < n; j++) {
                int interval = (int) Math.pow(2, n - 1 - j);

                // 몫이 짝수면 T, 홀수면 F
                condition[j] = (i / interval) % 2 == 0;

                System.out.println((condition[j] ? "T" : "F") + " ");
            }

            // 하위 클래스에서 구현한 로직으로 결과 계산
            boolean result = evaluate(condition);
            System.out.println(" " + (result ? "T" : "F"));
        }
        System.out.println();
    }
}

interface TruthT{
    void generate(String... variables);
    void printTable();
}

class TruthTableProcessor implements TruthT {
    private String[] headers;
    private int[][] table;
    private int rows;
    private int cols;

    @Override
    public void generate(String... variables) {
        this.headers = variables; // 진리표의 헤더 값
        this.cols = variables.length; // 진리표의 열의 크기
        this.rows = (int) Math.pow(2, cols); // 진리표의 행의 크기
        this.table = new int[rows][cols];       

        for (int i = 0; i < rows; i++){ // 행의 개수만큼 반복
            for (int j = 0; j < cols; j++){ // 열의 개수만큼 반복
                int interval = (int) Math.pow(2, cols - 1 - j); // 진리 값 변동 주기
                table[i][j] = ((i / interval) % 2) ^ 1; // 진리 값 결정 로직(0 XOR 1 = 1 / 1 XOR 1 = 0)
            }
        }
    }

    @Override
    public void printTable(){
        if (headers == null || table == null){
            System.out.println("표가 생성되지 않았습니다. generate()를 먼저 호출하세요.");
            return;
        }

        // 1. 헤더 출력
        for (String header : headers) {
            System.out.print(header + "\t");
        }
        System.out.println("\n---------------------------");

        // 2. 데이터 출력
        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                System.out.print(table[i][j] + "\t");
            }
            System.out.println();
        }
    }
}

// Main
public class Main {

    public static void main(String[] args){
        TruthT processor = new TruthTableProcessor();
        processor.generate("p", "q", "r");
        processor.printTable();
    }
}