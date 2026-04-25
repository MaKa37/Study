package Math;

public class Test{

    public static void main(String[] args) {
        // 반복 횟수: 만 번은 너무 빨라 차이가 안 보일 수 있어 1억 번으로 설정했습니다.
        // 원하시면 10,000으로 수정해서 테스트해보세요!
        long iterations = 100_000_000L; 
        
        System.out.println("테스트 시작 (반복 횟수: " + iterations + ")\n");

        // 1. 나눗셈 & 나머지 연산 (%) 측정
        long startTime = System.nanoTime();
        long sum1 = 0;
        for (long i = 0; i < iterations; i++) {
            // 기존 방식: (i / 2) % 2
            sum1 += (i / 2) % 2;
        }
        long endTime = System.nanoTime();
        long durationDiv = endTime - startTime;
        System.out.println("1. 나눗셈 & 나머지 방식: " + (durationDiv / 1_000_000.0) + " ms");

        // 2. 비트 연산 (>>, &) 측정
        startTime = System.nanoTime();
        long sum2 = 0;
        for (long i = 0; i < iterations; i++) {
            // 최적화 방식: (i >> 1) & 1
            sum2 += (i >> 1) & 1;
        }
        endTime = System.nanoTime();
        long durationBit = endTime - startTime;
        System.out.println("2. 비트 연산 방식:       " + (durationBit / 1_000_000.0) + " ms");

        // 결과 비교
        System.out.println("\n--------------------------------");
        System.out.printf("비트 연산이 %.2f배 더 빠릅니다.\n", (double) durationDiv / durationBit);
        
        // JIT 최적화 방지용 출력 (합계가 같아야 로직이 동일한 것)
        if (sum1 != sum2) System.out.println("결과가 다릅니다! 로직 확인 필요.");
    }
}



