package Java;

interface Addable {
    int add(int a, int b);
}

public class Lambda {

    public static void main(String[] args) {
        // 1. 기존 익명 구현 클래스 문법
        Addable ad1 = new Addable() {
            public int add(int a, int b) {
                return (a + b);
            }
        };

        // 2. 기본 람다식 적용
        Addable ad2 = (int a, int b) -> {
            return (a + b);
        };

        // 3. 가장 축약된 형태의 람다식
        Addable ad3 = (a, b) -> (a + b);

        System.out.println(ad1.add(1, 1) + ad2.add(1, 1) + ad3.add(1, 1));
    }
}