package Math;

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


// 논리곱(Conjunction): p ∧ q
// 두 명제가 모두 참(True)일 때만 결과가 참이 되는 논리 연산입니다.
class Conjunction implements TruthTable {

    @Override
    public int getVaribleCount() {
        return 2;
    }

    @Override
    public boolean evaluate(boolean [] values) {
        return values[0] && values[1];
    }
    
    @Override
    public String getSymbol() {
        return "p ∧ q";
    }
}

// Main
public class Main {

    public static void main(String[] args){
        TruthTable conjunction = new Conjunction();
        conjunction.printTable();
    }
}