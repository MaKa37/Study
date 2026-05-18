package JavaStudy;

import java.util.*;

public class JavaCollection {
    public static void main (String[] args) {

        /* 다형성을 활용한 객체 선언
            변수 선언은 인터페이스(List, Set, Map)으로 하고, 객체 생성은 구현 클래스(ArrayList, HashSet)으로 하면,
            나중에 내부 구현 방식을 바꾸고 싶을 때 코드 수정 범위를 최소화할 수 있다.
        */

        /* List(구현체: ArrayList)
            - 데이터가 입력된 순서를 기억하며, 동일한 데이터의 중복 저장을 허용합니다.
            - 순서(Index)가 있어서 특정 위치의 데이터를 꺼낼 수 있습니다.
         */
        // 0. 인터페이스를 List로 선언하고 ArrayList로 객체 생성
        List<String> list = new ArrayList<>();

        // 1. 데이터 삽입 (순서대로 저장됨, 중복 허용)
        list.add("Java");
        list.add("Python");
        list.add("Java"); // "Java" 중복 저장

        System.out.println("리스트 크기: " + list.size()); // 출력: 3
        System.out.println("1번 인덱스 값: " + list.get(1)); // 출력: Python

        // 2. 데이터 순회
        System.out.println("--- 향상된 for문 ---");
        for (String lang : list) {
            System.err.println(lang);
        }

        System.out.println("--- 람다식 순회 (Java 8 이상) ---");
        list.forEach(lang -> System.out.print(lang + "\t"));


        /* Set(구현체: HashSet)
            - 데이터의 순서를 보장하지 않으며, 중복을 허용하지 않는다.
         */
        System.out.println("\n-------------------------------------------");
        Set<String> set = new HashSet<>();

        // 1. 데이터 삽입
        set.add("Apple");
        set.add("Banana");
        boolean isAdded = set.add("Apple"); // 중복 데이터 삽입 시도

        // "Apple"은 이미 존재하므로 추가되지 않고 false를 반환함
        System.out.println("중복 삽입 성공 여부: " + isAdded); // false
        System.out.println("Set 크기: " + set.size()); // 2(Apple, Banana)

        // 2. 데이터 존재 여부 확인
        if (set.contains("Banana")) {
            System.out.println("바나나가 존재합니다.");
        }

        /* Queue(구현체: LinkedList)
            - 먼저 들어간 데이터가 먼저 낭는 FIFO(First-In-First-Out, 선입선출) 구조입니다.
            - Java에서 Queue는 인터페이스이므로, 이를 구현한 LinkedList 클래스를 사용하여 생성합니다.
            - LinkedList는 List와 Queue 역할을 모두 수행할 수 있습니다.
         */

        System.out.println("\n-------------------------------------------");
        Queue<String> queue = new LinkedList<>();

        // 1. 큐에 데이터 추가(offer)
        queue.offer("첫 번째 손님");
        queue.offer("두 번째 손님");
        queue.offer("세 번째 손님");

        // 2. 큐에서 데이터 꺼내기(poll - 꺼낸 후 큐에서 삭제됨)
        System.out.println("처리 중: " + queue.poll()); // 첫 번째 손님
        System.out.println("처리 중: " + queue.poll()); // 두 번째 손님

        // 3. 남은 대기열 확인
        System.out.println("남은 대기 인원: " + queue.size()); // 1

        /* Map(구현체: HashMap)
            - Key와 Value의 쌍으로 데이터를 저장합니다.
            - Key는 중복될 수 없지만, Value는 중복될 수 있습니다.
            - ex: Key(학번): Value(학생 이름)
         */

        System.out.println("\n-------------------------------------------");
        Map<String, Integer> map = new HashMap<>();

        // 1. 데이터 삽입 (put)
        map.put("김철수", 90);
        map.put("이영희", 100);
        map.put("김철수", 95); // Key가 같으면 기존 값을 새로운 값으로 덮어씌움

        // 김철수의 점수는 90점에서 95점으로 변경됨.
        System.out.println("김철수 점수: " + map.get("김철수"));

        // 2. 데이터 순회
        map.forEach((key, value) -> System.out.println("이름: " + key + ", 점수: " + value));
    }
}
