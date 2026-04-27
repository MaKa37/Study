package Java;

/* 타입 파라미터 네이밍
T: Type(일반적인 타입) {Integer, Double, Boolean, Long, Float, Character, String... Class name}
E: Element(컬렉션의 요소, 예: List<E>)
K: Key(키)
V: Value(값)
N: Number(숫자)
 */

// 1. 제네릭 클래스 정의(타입 파라미터 T 사용)
class Data<T> {
    private T t;
    public void set(T t) { this.t = t; }
    public T get() { return t; }
}

/* 제네릭(Generic)
1. 개념: 클래스, 인터페이스, 메소드를 정의할 때 타입 매개변수(Type Parameter)를 선언하여 사용하는 기능
2. 기능: 런타임 시점에서 엄격한 자료형 검사를 통해 런타임 오류를 방지하고 데이터를 꺼낼 때 마다 수행하는 불필요한 캐스트(형변환) 연산을 생략할 수 있다.
*/ 
public class Generic {
    public static void main(String[] args){
        // 2. 제네릭 클래스 사용(명확한 타입 지정)
        Data<String> dataGen = new Data<>();

        // dataGen.set(Integer.valueOf(20)); -> 컴파일 오류 발생
        dataGen.set("Hello");
        System.out.println(dataGen.getClass().getName()); // Java.Data -> 객체
        
        String sGen = dataGen.get();
        System.out.println(sGen.getClass().getName()); // java.lang.String -> 객체에서 꺼내온 데이터 타입
    }
}
