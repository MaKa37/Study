package JavaStudy;

import java.util.*;

public class JavaCollection {
    public static void main (String[] args) {

        /* 다형성을 활용한 객체 선언
            변수 선언은 인터페이스(List, Set, Map)으로 하고, 객체 생성은 구현 클래스(ArrayList, HashSet)으로 하면,
            나중에 내부 구현 방식을 바꾸고 싶을 때 코드 수정 범위를 최소화할 수 있다.
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
         */
    }
}
