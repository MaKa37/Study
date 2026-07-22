package Math;

interface TruthT{
    void generate(String... variables);
    void printTable();
}

class TruthTableProcessor implements TruthT {
    String[] headers;  // 인자 값 저장 배열 변수
    boolean[][] table; // 진리 표 가변 배열 변수
    private int rows;          // 진리 표 행의 크기 저장 변수
    private int cols;          // 진리 표 열의 크기 저장 변수

    @Override
    public void generate(String... variables) {
        this.headers = variables;              // 진리 표의 헤더 값
        this.cols = variables.length;          // 진리 표의 열의 크기 계산
        this.rows = (int) Math.pow(2, cols); // 진리 표의 행의 크기
        this.table = new boolean[rows][cols];   // 진리 표 객체 생성

        for (int i = 0; i < rows; i++){ // 행의 개수만큼 반복
            int shift = cols - 1;
            for (int j = 0; j < cols; j++){ // 열의 개수만큼 반복
                // 비트 연산 후 논리 연산: 끝 비트가 0이면 T, 1이면 F
                table[i][j] = (i >> (shift--) & 1 ) == 0;

                // int interval = (int) Math.pow(2, cols - 1 - j); // 진리 값 변동 주기
                // table[i][j] = (i / interval) % 2 == 0; // 논리 연산 시(비트 연산이 약 2.3배 더 빠름)
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
                System.out.print((table[i][j] ? "T" : "F") + "\t");
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