package JavaStudy;

// java.util 핵심 클래스
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

public class JavaUtil {
    public static void main (String[] args) {
        // 1. Scanner: 사용자에게 데이터 입력받기
        Scanner scanner = new Scanner(System.in);
        System.out.print("생성할 데이터(난수)의 개수를 입력하세요: ");
        int count = scanner.nextInt();

        // 2. Random: 임의의 데이터(난수) 발생
        Random random = new Random();

        // 3. List & ArrayList: 순서가 있는 데이터의 동적 저장(컬렉션 프레임워크)
        List<Integer> dataList = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            // 1부터 100 사이의 난수를 리스트에 추가
            dataList.add(random.nextInt(100) + 1);
        }
        System.out.println("\n[1단계] 생성된 원본 데이터 리스트: " + dataList);

        // 4. Collections: 컬렉션 객체 조작(오름차순 정렬)
        Collections.sort(dataList);
        System.out.println("[2단계] 오름차순 정렬된 데이터 리스트: " + dataList);

        // 5. Map & HashMap: 키(Key)와 값(Value) 형태로 데이터 집계
        // 데이터의 특징(홀수/짝수)을 기준으로 빈도수를 카운팅하여 저장합니다.
        Map<String, Integer> dataAggregation = new HashMap<>();
        dataAggregation.put("짝수", 0);
        dataAggregation.put("홀수", 0);

        for (int num : dataList) {
            if (num % 2 == 0) {
                dataAggregation.put("짝수", dataAggregation.get("짝수") + 1);
            }
            else {
                dataAggregation.put("홀수", dataAggregation.get("홀수") + 1);
            }
        }
        System.out.println("[3단계] 데이터 그룹화 및 집계 결과(Map): " + dataAggregation);

        // 6. Arrays: 배열 조작
        // 동적 자료구조인 List를 정적 크기의 Array(배열)로 변환 후 문자열로 출력
        Integer[] dataArray = dataList.toArray(new Integer[0]);
        System.out.println("[4단계] List를 Array로 변환하여 출력: " + Arrays.toString(dataArray));

        // 리소스 해제
        scanner.close();
    }
}