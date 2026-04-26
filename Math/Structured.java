package Math;

import java.util.LinkedHashMap;
import java.util.Map;

// Map 구조로 진리 표 구조 설계하기

interface TruthTable {
    void generate(String... variables);
    void addExpression(String var1, String operator, String var2);
    void printTable();
}

class TruthTableLogic implements TruthTable {
    // 순서 보장을 위해 LinkedHashMap 사용: Key(헤더명), Value(해당 열의 진리값 배열)
    private Map<String, boolean[]> tableMap = new LinkedHashMap<>();
    private int rows; // 행의 크기

    @Override
    public void generate(String... variables) {
        int cols = variables.length;
        this.rows = 1 << cols;

        for (int j = 0; j < cols; j++) {
            boolean[] columnData = new boolean[rows];
            int shift = cols - 1 - j;

            for (int i = 0; i < rows; i++) {
                // 끝 비트가 0이면 T, 1이면 F
                columnData[i] = ((i >> shift) & 1) == 0;
            }
            // 계산된 단일 열 데이터를 Map에 추가
            tableMap.put(variables[j], columnData);
        }
    }

    @Override
    public void addExpression(String var1, String operator, String var2) {
        
        // 1. 입력받은 인자가 기존 진리표에 존재하는지 검증
        if (!tableMap.containsKey(var1) || !tableMap.containsKey(var2)) {
            System.out.println("오류: 존재하지 않는 변수입니다.");
            return;
        }

        // 2. Map에서 두 변수의 배열의 열 데이터를 추출
        boolean[] col1 = tableMap.get(var1);
        boolean[] col2 = tableMap.get(var2);
        boolean[] newCol = new boolean[rows];

        String newHeader = var1 + " " + operator + " " + var2;

        // 3. 행 단위로 논리 연산
        for (int i = 0; i < rows; i++) {
            switch (operator.toUpperCase()) {
                case "AND":
                case "&&":
                    newCol[i] = col1[i] && col2[i];
                    break;
                case "OR":
                case "||":
                    newCol[i] = col1[i] || col2[i];
                    break;
                default:
                    System.out.println("지원하지 않는 연산자입니다: " + operator);
                    return;
            }
        }

        // 4. 연산 결과를 새로운 테이블(열)로 Map에 추가
        tableMap.put(newHeader, newCol);
    }

    @Override
    public void printTable() {

        // 1. 객체 생성 여부 체크
        if (tableMap.isEmpty()) {
            System.out.println("표가 생성되지 않았습니다. generate()를 먼저 호출하세요.");
            return;
        }

        // 2. 헤더 출력 (Map의 Key값)
        for (String header : tableMap.keySet()) {
            System.out.print(header + "\t\t");
        }
        System.out.println("\n---------------------------------------------");

        // 3. 데이터 출력
        for (int i = 0; i < rows; i++){
            for (String header : tableMap.keySet()) {
                boolean value = tableMap.get(header)[i];
                System.out.print((value ? "T" : "F") + "\t\t");
            }
            System.out.println();
        }
    }
}

public class Structured {
    public static void main(String[] args){
        TruthTable processor = new TruthTableLogic();

        // 1. 진리 표 생성
        processor.generate("p", "q", "r");

        // 2. 논리 연산 추가 (기존 테이블에 열이 추가됨)
        processor.addExpression("p", "&&", "q");
        // processor.addExpression("q", "||", "r");
        // processor.addExpression("p", "AND", "r");

        // 3. 출력
        processor.printTable();
    }
}
