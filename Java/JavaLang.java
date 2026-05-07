package Java;

class DataRecord {
    String id;

    public DataRecord(String id) {
        this.id = id;
    }

    // 객체 출력 시 메모리 주소(클래스이름@해시코드) 대신 실제 값 반환
    @Override
    public String toString() {
        return "DataRecord{id='" + id + "'}";
    }

    // 두 객체의 논리적 동등성(실제 데이터 값)을 비교하도록 재정의
    public boolean equals(Object obj) {
        if (this == obj) return true; // 주소가 같을 시 동일
        if (obj == null || getClass() != obj.getClass()) return false; // 타입 확인
        DataRecord record = (DataRecord) obj;
        return id. equals(record.id); // 내부 문자열 값 비교
    }
}

public class JavaLang {
    public static void main(String[] args) {

        // 1. Object 클래스: toString() 및 equals() 재정의
        // 객체의 메모리 주소가 아닌, '실제 데이터 값'을 기준으로 객체를 식별하고 출력하도록 오버라이딩하는 필수 패턴
        System.out.println("### Object Example ###");

        DataRecord rec1 = new DataRecord("user_123");
        DataRecord rec2 = new DataRecord("user_123");

        System.out.println(rec1.toString());   // DataRecord{id='user_123'}
        System.out.println(rec1 == rec2);      // false(메모리 주소가 다름)
        System.out.println(rec1.equals(rec2)); // true(오버라이딩된 equals 메서드로 값 비교)
        System.out.println();

        // 2. 문자열 처리: String vs StringBuilder & StringBuilder
        // String(불변: Immutability)

        String str = "Data"; // 메모리 주소: 2122698 <- System.out.println(str.hashCode());
        str += " Pideline"; // 메모리 주소: -1370290460 (기존 객체가 삭제되고 새로 생성됨.)

        // StringBuilder & StringBuffer(가변: Mutable)
        StringBuilder sb = new StringBuilder("Data"); // StringBuffer sc = new StringBuffer("Data");
        sb.append(" Pipeline");
        sb.insert(5, "Stream ");
        System.out.println(sb.toString());
        System.out.println();

        // 3. 포장 클래스(Wrapper Class): 박싱/언박싱 및 형 변환
        // 기본 자료형과 객체 타입 간의 자동 변환(Auto-boxing/unboxing) 메커니즘과 데이터 타입 파싱 방법
        
        // 3-1. 오토 박싱(Auto-boxing) & 언박싱(Auto-unboxing)
        Integer wrappedCount = 1000; // int -> Integer 객체로 자동 변환 (컬렉션에 담을 때 유용) 
        int primitiveCount = wrappedCount; // Integer 객체 -> int로 자동 변환
        
        // 3-2. 데이터 형 변환(파싱)
        String rawData = "45020";
        int parsedData = Integer.parseInt(rawData); // 문자열 -> 정수 변환
        double piVal = Double.parseDouble("3.14159"); // 문자열 -> 실수 변환
        String stringfiedData = String.valueOf(parsedData); // 정수 -> 문자열 변환
    
        // 4. System 클래스: 성능 측정 및 배열 제어
        int[] sourceData = {10, 20, 30, 40, 50};
        int[] targetBuffer = new int[5];

        // 4-1. 실행 시간 측정 시작(밀리초 단위)
        long startTime = System.currentTimeMillis();

        // 4-2. 고속 배열 복사(for문 보다 빠르고 효율적임)
        // System.arraycopy(원본배열, 원본시작인덱스, 대상배열, 대상시작인덱스, 복사할길이)
        System.arraycopy(sourceData, 0, targetBuffer, 0, sourceData.length);

        // 4-3. 실행 시간 측정 종료
        long endTime = System.currentTimeMillis();
        System.out.println("로직 소요 시간: " + (endTime - startTime) + "ms");
        System.exit(0);
    }
}
