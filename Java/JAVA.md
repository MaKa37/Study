
## 01. 자바 계층 구조

📁 MyShoppingProject (프로젝트: 최상위 단위)
└── 📦 shop.member.module (모듈: 연관된 패키지들의 그룹)
    ├── 📄 module-info.java (모듈 설정: 접근 제어 및 의존성 정의)
    └── 📁 com.shop.member (패키지: 클래스의 논리적/물리적 폴더)
        └── 📄 Customer.java (소스 파일: 실제 코드가 작성되는 파일)
            └── 🏛️ class Customer (클래스: 객체 생성을 위한 설계도)
                ├── 📦 int age; (필드: 상태/속성)
                ├── 📦 String name; (필드: 상태/속성)
                ├── ⚙️ Customer() { ... } (생성자: 초기화)
                └── ⚙️ void buyItem() { ... } (메서드: 행동/기능)

### 각 계층 상세 설명
1. 프로젝트(Project)
	- 애플리케이션의 최상위 컨테이너입니다.
	- 하나 이상의 모듈이나 패키지를 포함하며, 전체 애플리케이션의 빌드 및 배포 단위가 됩니다.
	
2.  모듈(Module) `(Java 9 이상)
	- 서로 밀접하게 연관된 패키지들을 하나로 묶은 단위입니다.
	- `module-info.java`파일을 통해 외부로 노출할 패키지와 내부에서만 사용할 패키지를 엄격하게 제어합니다.
	
3.  패키지(Pakage)
	- 유사한 기능을 하는 클래스와 인터페이스들을 그룹화하는 폴더 역할을 합니다.
	- 이름 충돌(Name Collision)을 방지하고 접근 제어자(Access Modifier)와 결합하여 보안성을 높입니다.
	
4.  소스 파일(Source File)
	- 확장자가 `.java`인 텍스트 파일입니다.
	- 하나의 소스 파일 안에는 여러 클래스가 존재할 수 있지만, `public` 클래스는 파일당 단 하나만 존재해야 하며 파일명과 일치해야 합니다.
	
5.  클래스(Class)
	- 객체(Object)를 생성하기 위한 템플릿 또는 설계도입니다.
	- 프로그램의 기본적인 구조적 단위입니다.
		- 5-1. 필드(Field): 클래스 내부에 선언된 변수로, 객체의 데이터(상태)를 저장합니다.
		- 5-2. 생성자(Constructor): 객체가 메모리에 생성될 때 초기화를 담당하는 특수한 형태의 메서드입니다.
		- 5-3. 메서드(Method): 객체가 수행할 수 있는 동작(기능)을 정의한 코드 블록입니다.
	

---

### 01-01. 자바 문법
#### 접근 제어자

접근 제어자는 클래스, 변수 메서드의 접근 범위를 설정하는 키워드입니다.

| **제어자**       | **동일 클래스** | **동일 패키지** | **자식 클래스** | **전체(Project)** |
| ------------- | ---------- | ---------- | ---------- | --------------- |
| **public**    | O          | O          | O          | O               |
| **protected** | O          | O          | O          | X               |
| **default**   | O          | O          | X          | X               |
| **private**   | O          | X          | X          | X               |

---

#### 특수 제어자

특수 제어자(Modifiers)는 클래스, 필드, 메서드의 기본적인 성격에 추가적인 '특수한 기능'을 부여하는 키워드입니다.
자바 클래스 구조에서 필드나 메서드를 선언할 때 접근 제어자 뒤에 붙혀서 사용합니다.

| **제어자**      | **적용 대상**    | **주요 의미**             |
| ------------ | ------------ | --------------------- |
| **static**   | 필드, 메서드      | 클래스 공유 (객체 생성 불필요)    |
| **final**    | 클래스, 필드, 메서드 | 변경 불가 (상수, 상속/재정의 금지) |
| **abstract** | 클래스, 메서드     | 미완성 (상속을 통한 강제 구현)    |

1. static(정적 제어자): 객체 생성없이 공통으로 사용
     - 의미: 인스턴스(객체)에 속하는 것이 아니라 클래스 자체에 고정하여 모든 객체가 해당 변수나 메서드를 공유합니다.
     - 문법: `[접근 제어자] static [데이터 타입];`
     - 특징: `new`로 객체를 만들지 않아도 `클래스명.변수명`으로 바로 접근 가능.

2. final(최종 제어자): 더 이상 수정하거나 변경할 수 없음.
     - 의미: 대상에 따라 의미가 조금씩 다릅니다.
          - 변수: 한 번 값을 저장하면 변경할 수 없는 상수가 됩니다.
          - 메서드: 자식 크랠스에서 오버라이딩(재정의)할 수 없습니다.
          - 클래스: 다른 클래스가 상속받을 수 없습니다.
     - 문법: `[접근 제어자] final [데이터 타입] [변수명] = 값;`

3. abstract(추상 제어자): 기능은 자식 클래스에서 구현하겠다는 의미입니다.
     - 의미: 미완성된 상태를 나타냅니다.
          - 추상 메서드: `몸통( { } )`이 없는 메서드로, 상속받은 자식 클래스에서 내용을 구현해야 합니다.
          - 추상 클래스: 추상 메서드를 하나라도 포함하고 있는 클래스입니다.
     - 문법: `[접근 제어자] abstract [반환 타입] [메서드명()];`

```java
public class Constants {
     // static과 final을 합쳐 '공용 상수'로 자주 사용합니다.
     public static double PI = 3.14159;

     // abstract는 몸통 없이 선언만 합니다.
     public abstract void performAction(); // performAction(번역: 실행)
}
```

---

#### 데이터 타입(자료형)

데이터 타입(Data Type)은 변수에 저장될 데이터의 종류와 크기를 결정하는 키워드입니다.
자바는 변수를 선언할 때 반드시 데이터 타입을 명시해야합니다.
- 기본 타입(Primitive Type): 실제 데이터 값을 저장하는 타입
- 참조 타입(Reference Type): 메모리 주소를 저장하는 타입

##### 데이터 타입의 종류

| **분류**           | **타입 (Type)**                                            | **크기**                                           | **저장되는 값 / 주요 의미**                                                                                                                                                                    |
| ---------------- | -------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **논리형<br>(기본)**  | **boolean**                                              | 1 byte                                           | 참(true) 또는 거짓(false)                                                                                                                                                                  |
| **문자형<br>(기본)**  | **char**                                                 | 2 byte                                           | 단일 문자 (Unicode, UTF-16)                                                                                                                                                               |
| **정수 형<br>(기본)** | **byte**<br><br>**short**<br><br>**int**<br><br>**long** | 1 byte<br><br>2 byte<br><br>4 byte<br><br>8 byte | ($-128 \sim 127$($-2^7 \sim 2^7-1$))<br><br>($-32,768 \sim 32,767$($-2^{15} \sim 2^{15}-1$))<br><br>약 $\pm 21$억 ($-2^{31} \sim 2^{31}-1$)<br><br>약 $\pm 9$경 ($-2^{63} \sim 2^{63}-1$) |
| **실수형<br>(기본)**  | **float**<br><br>**double**                              | 4 byte<br><br>8 byte                             | ($\pm 1.4 \times 10^{-45} \sim \pm 3.4 \times 10^{38}$)<br><br>($\pm 4.9 \times 10^{-324} \sim \pm 1.8 \times 10^{308}$)                                                              |
| **참조형**          | **Class**, **Array**, **Interface**, 등                   | JVM에 따라 다름                                       | 실제 데이터가 있는 힙(Heap) 메모리의 주소                                                                                                                                                            |

1. 정수형(Integer Types): 소수점이 없는 숫자를 저장합니다.
	- 기본: `int`를 사용하며, 데이터 크기에 따라 다른 크기의 정수형을 선언하기도 합니다.
	- 문법: `[데이터 타입] [변수명] = 정수값;` / long l1 = `2147483648L`; 끝자리 `L` 표현
	- 특징: `int`의 범위를 초과하는 큰 숫자를 다룰 때는 `long`을 사용합니다.
	  
2. 실수형(Floating-Point Types): 소수점이 포함된 숫자를 저장합니다.
	- 기본: `double`을 사용하며, float형 보다 더 정확한 소수점 자리를 표현할 수 있습니다.
	- 문법: `[데이터 타입] [변수명] = 실수값;`
	- 특징: `float`타입에 값을 할당할 때는 숫자 끝에 접미사 `F` 를 붙혀야합니다.
	  
3. 논리형과 문자형(Logical & Character Types): 상태의 값과 단일 문자를 다룹니다.
	- 의미: 프로그램의 조건 흐름을 제어하거나(boolean), 글자 하나를 저장(char)할 때 사용
	- 문법:
		- `boolean [변수명] = true / false;`
		- `char [변수명] = '단일 문자'`
	- 특징: 
		- 자바에서 `boolean`은 C언어와 달리 숫자(0, 1)와 호환되지 않습니다.
		- `char` 값을 할당할 때는 반드시 작은따옴표(` ' ' `)를 사용해야 합니다.
	
4.  참조형(Reference Types): 기본형 8가지를 제외한 모든 타입입니다.
	- 의미: 실제 데이터 값 대신, 객체가 생성된 메모리(Heap)의 주소(참조값)를 변수에 저장
	- 문법: `[클래스/배열/인터페이스] [변수명] = new [클래스/배열]();`
	- 특징: `new` 연산자를 사용해 객체를 생성하는 것이 일반적이며, 값이 없음을 뜻하는 `null`로 초기화할 수 있습니다.(EX: String)

```java
public class DataTypeExample {
	// 1. 정수형과 실수형(기본형)
	public int maxPlayers = 100;
	public long totalRevenue = 500000000L;
	public float pi = 3.141592f;
	public double temperature = 36.5;
	
	// 2. 논리형과 문자형(기본형)
	public boolean isActivate = true;
	public char grade = 'A';
	
	// 3. 참조형(Class, Array)
	public String userName = "홍길동";
	public int[] scores = new int[]{90, 85, 100};
}
```

---

#### 연산자와 특수 기호

자바에서 연산자(Operators)는 변수나 상수의 데이터를 가공하고 계산하기 위해 사용하는 기호이며, 특수 기호(구분자, Separators)는 코드의 문법적 구조를 정의하고 실행 흐름을 나누는 역할을 합니다.

##### 연산자와 특수 기호

| **분류**    | **종류**      | **기호**                            | **주요 의미**                                    |
| --------- | ----------- | --------------------------------- | -------------------------------------------- |
| **연산자**   | **산술 연산자**  | `+`, `-`, `*`, `/`, `%`           | 사칙연산 및 나머지(`%`) 계산                           |
|           | **대입 연산자**  | `=`, `+=`, `-=`, `*=`, `/=`, `%=` | 값을 변수에 할당 (복합 대입 포함)                         |
|           | **증감 연산자**  | `++`, `--`                        | 변수의 값을 1씩 증가 또는 감소                           |
|           | **비교 연산자**  | `==`, `!=`, `>`, `<`, `>=`, `<=`  | 두 값을 비교하여 참/거짓(boolean) 반환                   |
|           | **논리 연산자**  | `&&`,  \| \|, `!`                 | AND(그리고), OR(또는), NOT(부정) 조건 결합              |
|           | **배타적 연산자** | `^`                               | XOR(배타적 논리합)                                 |
|           | **삼항 연산자**  | `? :`                             | 조건식 ? 참일 때 값 : 거짓일 때 값                       |
| **특수 기호** | **중괄호**     | `{ }`                             | 클래스, 메서드, 제어문 등의 **코드 블록(영역)** 지정            |
|           | **소괄호**     | `( )`                             | 연산 우선순위 지정, 메서드 매개변수 선언/호출                   |
|           | **대괄호**     | `[ ]`                             | 배열 선언 및 인덱스(순서) 접근                           |
|           | **세미콜론**    | `;`                               | 하나의 **문장(명령어)이 끝났음**을 표시                     |
|           | **콜론**      | `:`                               | 향상된 for문 요소 분리, switch case 라벨, 삼항 연산자 조건 분기 |
|           | **마침표**     | `.`                               | 객체의 멤버(필드, 메서드)에 접근 (하위 항목 호출)               |
|           | **쉼표**      | `,`                               | 변수 연속 선언, 매개변수나 배열 요소 구분                     |

1. 산술 및 대입 연산자: 계산과 저장
	- 의미: 수학적 계산을 수행하고 그 결과를 변수에 저장합니다.
	- 특징: 
		- `=` 연산자는 '같다'는 뜻이 아니라 '오른쪽의 값을 왼쪽에 넣는다'는 대입의 의미다.
		- `+=`같은 복합 대입 연산자를 쓰면 코드를 더 짧게 줄일 수 있습니다.
	- 문법: `a = a + 5` ≡ `a += 5;`
	  
2. 비교 및 논리연산자: 조건 판단
	- 의미: 값의 크기를 비교하거나(비교), 여러 조건을 엮어서(논리) 최종적으로 `true` 또는 `false`값을 만들어냅니다.
	- 특징: 
		- `if`문이나 `for`, `while` 같은 제어문에서 흐름을 결정할 때 필수적으로 사용됩니다.
		- Java에서는 '같다'를 표현할 때 `==`를, '다르다'를 표현할 때 `!=`를 사용합니다.
	
3. 특수 기호(구분자): 코드의 뼈대 구성
	- `{ }`는 영역의 시작과 끝을 의미합니다.
	- `;`는 코드의 마침표를 의미합니다.
	- `.`은 주로 만들어진 객체의 계층 구조를 구분할 때 사용(예: `System.out.println()`)
	- `:`는
		- for문에서 모든 데이터를 처음부터 끝까지 순서대로 꺼내서 탐색할 때 사용합니다.
		- array에서는 `String[] str1 = "StringArray"에서 str[1:]의 값은 tringArray`
		- switch-case문에서는 여러 조건 중 변수의 값과 일치하는 코드를 찾습니다.
		- 삼항연산자에서는 간단한 `if-else문을 한 줄로 줄여서 작성할 때 사용합니다.`


```java
public class OperatorSymbolExample { // { } 클래스 블록
	public static void main(String[] args) { 
		// 1. 산술 및 대입 연산자, 세미콜론(;)
		int a = 10;
		int b = 3;
		int remainder = a % b; // % 나머지 연산 ( 10 나누기 3의 나머지는 1 )
		a += 5; // 복합 대입 연산 (a는 15가 됩니다.)
		 
		// 2. 비교 및 논리 연산자, 소괄호()
		boolean isTrue = (a > 10) && (b < 5);
		 
		// 3. 증감 및 삼항 연산자
		b++; // 증감 연산자로 인해 b는 4가 됨.
		String result = (remainder == 1) ? "홀수" : "짝수";
		 
		// 4. 마침표(.)를 통한 객체 접근
		System.out.println("결과: " + result);
		 
		// 5-1. for문에서의 콜론(:)
		String[] fruits = {"사과", "바나나", "포도"};
		for (String fruit : fruits) {
			System.out.println("과일: " + fruit);
		}
		System.out.println();
		
		// 5-2. switch-case 에서의 콜론(:) 
		int caseNumber = 1;
		switch (caseNumber) {
			case 1: 
				System.out.println("1번 케이스");
				break;
			case 2:
				System.out.println("1번 케이스");
				break;
			default:
				System.out.println("기본 케이스");
		}
		
		// 5-3. 반복문 라벨에서의 콜론(:)
		outerLoop:
		for(int i = 0; i = 3; i++) {
			for(int j = 0; j < 3; j++) {
				if (i == 1 && j == 1) {
					System.out.println("조건 만족으로 전체 반복문 강제 종료");
					break outerLoop; // 안쪽 반복문이지만 바깥 반복문까지 종료됨.
				}
			}
		}
	}
}
```


---

##### 비트 연산자

| **분류**              | **기호** | **주요 의미**                                          |
| ------------------- | ------ | -------------------------------------------------- |
| **비트 AND**          | `&`    | 두 비트가 **모두 1일 때만 1**, 그 외에는 0                      |
| **비트 OR**           | `\|`   | 두 비트 중 **하나라도 1이면 1**, 모두 0이면 0                    |
| **비트 XOR**          | `^`    | 두 비트가 **서로 다르면 1**, 같으면 0 (배타적 논리합)                |
| **비트 NOT**          | `~`    | 비트 반전 (0은 1로, 1은 0으로 변경)                           |
| **Left Shift**      | `<<`   | 지정한 수만큼 비트를 **왼쪽**으로 이동 (빈자리는 0으로 채움)              |
| **Right Shift**     | `>>`   | 지정한 수만큼 비트를 **오른쪽**으로 이동 (빈자리는 원래의 부호 비트로 채움)      |
| **논리적 Right Shift** | `>>>`  | 지정한 수만큼 비트를 **오른쪽**으로 이동 (부호 상관없이 빈자리는 무조건 0으로 채움) |

---

#### Class 기본 문법

Java에서 클래스(Class)는 객체를 생성하기 위한 설계도입니다.
데이터(필드)와 그 데이터를 처리하는 행위(메서드)를 하나로 묶는 캡슐화의 기본 단위입니다.

|**구성 요소**|**설명**|
|---|---|
|**필드 (Fields)**|객체의 상태를 저장하는 변수 (멤버 변수)|
|**생성자 (Constructors)**|객체가 생성될 때 호출되며, 필드를 초기화하는 특수 메서드|
|**메서드 (Methods)**|객체의 동작이나 기능을 정의하는 코드 블록|

1. 필드(Fields / 멤버 변수)
	- 클래스에서 가장 먼저 객체의 상태와 데이터를 정의하는 변수입니다.
	- 보통 정적(Static)인 변수를 먼저 선언하고, 그 다음 인스턴스 변수를 작성합니다.
	- 문법 구조: `[접근 제어자] [특수 제어자] [데이터 타입] [변수명] = [초기 값];`
	
2. 생성자(Constructor)
	- 클래스 이름과 동이하며 반환 타입이 없습니다.
	- 객체 생성 시 `new` 연산자와 함께 호출됩니다.
	- 생성자를 명시하지 않으면 컴파일러가 기본 생성자(Default Constructor)를 자동으로 추가합니다.
	  
3. 메서드(Method)
	- 객체 간의 데이터 상호작용을 담당합니다.
	- `this` 키워드를 사용하여 인스턴스 자신의 필드나 메서드에 접근할 수 있습니다.


```java
public class DatabaseConfig {
	
	// 1. 필드(상태 정의)
	private static final String DEFAULT_DRIVER = "com.mysql.cj.jdbc.Driver"; // 정적 상수
	private String url;       // DB 주소
	private String username;  // 사용자명
	private int timeout;      // 연결 제한 시간
	
	// 2. 생성자(객체 초기화)
	public DatabaseConfig(String url, String username) {
		this.url = url;
		this.username = username;
		this.timeout = 30; // 기본 값 설정
	}
	
	// 생성자 오버로딩(다양한 방식으로 객체 생성 가능)
	public DatabaseConfig(String url, String username, int timeout){
		this.url = url;
		this.username = username;
		this.timeout = timeout;
	}
	
	// 3. 메서드(행위 정의)
	public void printConnectionInfo() {
		System.out.println("--- DB Connection Info ---");
		System.out.println("Driver: " + DEFAULT_DRIVER);
		System.out.println("URL: " + this.url);
		System.out.println("User: " + this.username);
		System.out.println("Timeout: " + this.timeout + "s");
	}
	
	// Getter/Setter(캡슐화 유지)
	public void seTimeout(int timeout) {
		if (timeout > 0) {
			this.timeout = timeout;
		}
	}	
}

public class Main {
	public static void main(String[] args) {
		// 객체 생성(인스턴스화)
		DatabaseConfig myDB = new DatabaseConfig("jdbc:mysql://localhost:3306/mydb", "admin"");
		
		// 메서드 호출
		myDB.setTimeout(60);
		myDB.printConnectionInfo();
	}
}
```



---



---

## 02. 패키지

Java에서 기본적으로 제공하는 표준 라이브러리(Java API) 주요 패키지

JDK(Java Development Kit)를 설치하면 별도의 추가 설정 없이 사용할 수 있다.

### java.lang(가장 핵심적인 기본 패키지)

- 자바 프로그래밍에 가장 필수적인 클래스들을 모아둔 패키지
- 특징: 자바에서 유일하게 `import`문을 작성하지 않아도 컴파일러가 자동으로 포함시킵니다.
- 주요 클래스: `String`, `Object`, `System`, `Math`, `Thread`, 기본 자료형의 포장(wrapper) 클래스(Integer, Double 등).

#### `Object` 클래스(모든 클래스의 조상)

자바에서 생성되는 모든 클래스는 자동으로 `Object` 클래스를 상속받습니다.

클래스 계층 구조에서 루트(Root)가 되는 클래스입니다.

따라서 `Object`가 제공하는 메소드는 모든 객체에서 사용 가능하며, 필요에 따라 재정의(Overriding)하여 사용합니다. 

| **주요 메소드**           | **설명**                                                   | **오버라이딩(재정의) 주요 사례**                                      |
| -------------------- | -------------------------------------------------------- | --------------------------------------------------------- |
| `toString()`         | 객체를 문자열로 표현 (`클래스이름@16진수해시코드` 형태).                       | `String`, `Integer` 등에서 객체의 실제 값을 반환하도록 재정의               |
| `equals(Object obj)` | 두 객체의 **참조값(메모리 주소)**이 같은지 비교 (`==` 연산과 동일).             | `String` 등에서 객체의 주소가 아닌 **실제 데이터 값**을 비교하도록 재정의           |
| `clone()`            | 객체를 복제하여 새로운 객체를 반환. (`Cloneable` 인터페이스 구현 필수, 예외 처리 필수) | 원본 유지가 필요한 객체 복사 시 사용                                     |
| `getClass()`         | 현재 객체의 클래스 정보(`Class` 객체)를 반환. (이름, 필드, 메소드 등 확인 가능)     | 리플렉션(Reflection) 등 런타임에 클래스 정보를 분석할 때 사용                  |
| `hashCode()`         | 객체를 식별하는 고유한 정수값 반환.                                     | 해시 기반 컬렉션(`HashMap`, `HashSet` 등) 사용 시 `equals()`와 함께 재정의 |

#### 문자열 처리 클래스 (`String` vs `StringBuffer` / `StringBuilder`)

문자열을 다루는 세 가지 클래스는 '변경 가능성(Mutability)'에 따라 용도가 명확히 구분됩니다.

| **구분**     | **String**                                                       | **StringBuffer(멀티스레드에서 안전) / StringBuilder(단일스레드에서 빠름)** |
| ---------- | ---------------------------------------------------------------- | -------------------------------------------------------- |
| **특징**     | **불변 (Immutable)**                                               | **가변 (Mutable)**                                         |
| **메모리**    | 한 번 생성되면 내용 변경 불가. 값을 더하면(`+`) 새로운 객체가 계속 생성됨.                   | 내부 버퍼(Buffer)를 사용하여 하나의 객체 안에서 문자열을 변경함.                 |
| **성능**     | 문자열이 자주 변경될 경우 메모리 낭비가 심하고 속도가 저하됨.                              | 문자열 추가/삭제가 빈번한 환경에서 성능이 압도적으로 우수함.                       |
| **주요 메소드** | `indexOf()`, `substring()`, `replace()`, `trim()`, `valueOf()` 등 | `append()`, `insert()`, `delete()`, `reverse()` 등        |
| **권장 용도**  | 변하지 않는 고정된 문자열, 단순 조회용                                           | 반복문 내에서의 문자열 조작, 로그 데이터 축적 등                             |

#### 포장 클래스(Wrapper Class)

기본 자료형(Primitive Type)을 객체(Reference Type)처럼 다루어야 할 때 사용하는 클래스들입니다.
(`Number` 클래스를 상속받는 숫자형 및 `Character`, `Boolean` 등)

- 존재 이유: 컬렉션(`ArrayList` 등)에 데이터를 넣거나, 유용한 상수(`MAX_VALUE` 등) 및 변환 메소드를 활용하기 위함입니다.
- 박싱(`Boxing`)과 언박싱(`Unboxing`):
	- 박싱: 기본형 → 객체형 변환(예: `Integer.valueOf(5)`)
	- 언박싱: 객체형 → 기본형 반환(예: `객체.intValue()`)
	- 오토 박싱/언박싱: 자바 컴파일러가 대입이나 연산 시 자동으로 위 과정을 처리해줍니다.
- 핵심 메소드(데이터 형 변환):
	- `문자열` → `숫자`: `Integer.parseInt("123")` 또는 `Double.parseDouble("3.14")`
	- `숫자:` → `문자열`: `String.valueOf(123)` 또는 `Integer.toString(123)`

#### System 클래스

운영체제 및 자바 가상 머신(JVM)과 관련된 시스템 수준의 기능을 객체 생성 없이(static 멤버) 바로 사용 할 수 있게 해줍니다.

| **주요 필드 / 메소드**                            | **기능**                                   |
| ------------------------------------------ | ---------------------------------------- |
| `System.in`                                | 표준 입력 스트림 (키보드 입력). `InputStream` 타입.    |
| `System.out`                               | 표준 출력 스트림 (콘솔 화면 출력). `PrintStream` 타입.  |
| `System.err`                               | 표준 에러 스트림 (에러 메시지 출력). `PrintStream` 타입. |
| `System.nanoTime()`, `currentTimeMillis()` | 현재 시간을 나노초 또는 밀리초 단위로 반환 (실행 시간 측정에 활용). |
| `System.exit(int status)`                  | 프로그램(JVM) 강제 종료.                         |
| `System.arraycopy()`                       | 배열의 요소를 빠르고 효율적으로 복사.                    |
#### 핵심 개념 코드

```java
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
```

---
### java.util (유틸리티 및 자료구조)

- 프로그램 개발에 유용한 다양한 유틸리티 클래스와 데이터 구조를 다루는 ==컬렉션 프레임워크(Collection Framework)==를 포함합니다.
- 주요 클래스: `ArrayList`, `HashMap`, `List`, `Map`(자료구조), `Scanner`(입력), `Random`(난수 발생), `Arrays`, `Collections`(배열 및 컬렉션 조작).

```java
package Java;

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
```

핵심 개념 요약 및 코드 매핑

- **입력 및 도구 (`Scanner`, `Random`)**: 외부에서 조건(개수)을 주입받고(`Scanner`), 그에 맞춰 임의의 테스트 데이터를 대량으로 생성(`Random`)합니다.
    
- **선형 자료구조 (`List`, `ArrayList`)**: 생성된 데이터를 순차적으로 담습니다. 배열과 달리 크기가 동적으로 늘어나므로, 데이터의 양을 미리 알 수 없을 때 유용합니다.
    
- **데이터 정제 (`Collections`)**: 수집된 원본 데이터를 분석하기 쉽도록 `Collections.sort()`를 통해 오름차순으로 정렬합니다.
    
- **키-값 자료구조 및 집계 (`Map`, `HashMap`)**: 정렬된 데이터를 순회하며 '짝수'와 '홀수'라는 **Key**를 기준으로 발생 빈도(**Value**)를 누적 합산합니다. 데이터를 특정 기준에 따라 분류하고 집계할 때 핵심적으로 사용됩니다.
    
- **배열 유틸리티 (`Arrays`)**: 최종적으로 다른 레거시 시스템이나 고정 크기의 자료형을 요구하는 메서드에 데이터를 전달해야 할 때, List를 일반 배열로 변환하고 `Arrays.toString()`을 통해 손쉽게 출력 및 확인합니다.

---
### java.io

- java.io: 파일, 콘솔, 네트워크 등을 통한 데이터의 스트림(Stream) 기반 입출력 기능을 제공합니다.
  (`File`, `InputStream`, `OutputStream`, `Reader`, `Writer`)
- java.nio: 자바 4부터 추가된 패키지로, 기존 `java.io`의 속도와 성능을 개선한 버퍼(Buffer) 및 채널(Channel) 기반의 비동기 입출력 기능을 제공합니다.

```java
package Java;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.LineNumberReader;
import java.io.RandomAccessFile;

public class JavaIO {
    public static void main(String[] args) {

        String dirPath = "data_pipeline";
        String filePath = dirPath + File.separator + "sample_data.csv";

        // 1. File 클래스: 입출력 기능은 없으나 파일과 디렉터리의 경로 및 상태를 제어합니다.
        File dir = new File(dirPath);
        if (!dir.exists()) {
            dir.mkdir(); // 디렉터리 생성
        }
        File file = new File(filePath);

        // 2. 캐릭터 기반 스트림(기본) + 보조 스트림: 텍스트 데이터 쓰기
        // 파일에 문자 단위로 접근하는 FileWriter(기본 스트림)를 BufferedWriter(보조 스트림)로 감싸 성능을 높입니다.
        try (FileWriter fw = new FileWriter(file);
            BufferedWriter bw = new BufferedWriter(fw)) {
                
                bw.write("id,name,role\n");
                bw.write("1,Alice,Data Engineer\n");
                bw.write("2,Bob,Data Scientist\n");
                bw.flush(); // 스트림에 남아있는 데이터를 목적지로 강제 전송
                System.out.println("[1 단계] 버퍼(BufferedWriter)를 활용한 텍스트 데이터 적재 완료");
                
            } catch (IOException e) {
            System.out.println("파일 쓰기 오류: " + e.getMessage());
            }

        // 3. 보조 스트림(LineNumberReader): 텍스트 데이터 읽기
        // 텍스트 라인 번호를 추적하면서 데이터를 읽어 들입니다. (BufferedReader의 서브클래스)
        try (FileReader fr = new FileReader(file);
            LineNumberReader lnr = new LineNumberReader(fr)) {

                System.out.println("\n[2 단계] LineNumberReader를 이용한 데이터 읽기");;
                String line;
                while ((line = lnr.readLine()) != null) {
                    // getLineNumber()를 통해 현재 읽은 줄 번호를 함께 출력합니다.
                    System.out.printf("Line %d: %s\n", lnr.getLineNumber(), line);
                }

            } catch (IOException e) {
                System.out.println("파일 읽기 오류: " + e.getMessage());
            }

            // 4. RandomAccessFile: 파일 포인터를 이용한 임의 위치 접근
            // 스트림처럼 순차적이지 않고, 원하는 위치로 이동(seek)하여 읽고 쓸 수 있습니다.
            try (RandomAccessFile raf = new RandomAccessFile(file, "rw")) {
                System.out.println("\n[3 단계 RandomAccessFile을 이용한 데이터 수정");

                // 파일의 맨 처음(0번 바이트)으로 포인터 이동
                raf.seek(0);
                char firstChar = (char) raf.read();
                System.out.println("수정 전 첫 글자: " + firstChar); // 'i' 출력 예상
                
                // 다시 맨 처음으로 돌아가서 'i'를 대문자 'I'로 덮어쓰기
                raf.seek(0);
                raf.write('I');
                System.out.println("첫 글자를 'I'로 변경 완료 (sample_data.csv 파일 확인)");

            } catch (IOException e) {
                System.out.println("랜덤 액세스 오류: " + e.getMessage());
            }
    }    
}

```

핵심 개념 요약

- **`File` 클래스의 역할 한계**: 코드의 첫 단계에서 보듯 `File` 객체 자체로는 데이터를 읽거나 쓸 수 없습니다. 경로 확인, 파일 존재 여부(`exists()`), 생성(`mkdir()`)과 같은 메타데이터 관리용으로만 사용됩니다.
    
- **기본 스트림과 보조 스트림의 결합 (데코레이터 패턴)**:
    
    - `FileWriter fw = new FileWriter(file)`는 파일과 직접 연결되는 **기본 스트림**입니다.
        
    - `new BufferedWriter(fw)`는 이 기본 스트림을 감싸서 내부적으로 버퍼링을 수행하는 **보조 스트림**입니다. 실제 I/O 횟수를 줄여 시스템 성능을 대폭 향상시킵니다.
        
- **바이트(Byte) vs 캐릭터(Character) 스트림**: 제공하신 마크다운 내용처럼 `InputStream`/`OutputStream`은 이미지나 실행 파일 같은 1바이트 기반 이진 데이터를, `Reader`/`Writer`는 위 예제와 같은 CSV, TXT 등의 2바이트 문자열 데이터를 처리하는 데 목적이 있습니다.
    
- **비순차적 접근 (`RandomAccessFile`)**: 일반적인 스트림은 물이 흐르듯 한 방향으로만 순차적으로 데이터를 처리하지만, `RandomAccessFile`은 `seek(long pos)` 메서드를 통해 마치 배열의 인덱스에 접근하듯 파일 내부의 특정 바이트 위치로 즉시 점프하여 데이터를 읽거나 수정할 수 있습니다.

### java.nio


```java
package Java;

import java.nio.file.*;
import java.io.IOException;

import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;

public class JavaNIO {
    public static void main(String[] args) {

        // NioFileManipulation
        // Path와 Files: 모던 파일 및 디렉터리 제어
        // 기존 java.io.File을 대체하며, 운영체제의 파일 시스템과 독립적으로 경로를 다루고 유틸리티 메서드를 통해 간편하게 파일을 조작합니다.

        // 1. Path 객체 생성(데이터를 적재할 디렉터리 대상)
        Path dirPath = Paths.get("data_pipeline");
        Path filePath = dirPath.resolve("javaNIO.csv");

        try {
            // 2. 디렉터리 생성(존재하지 않을 경우)
            if (Files.notExists(dirPath)) {
                Files.createDirectories(dirPath);
                System.out.println("디렉터리 생성 완료: " + dirPath);
            }

            // 3. 파일 쓰기(Files 유틸리티 활용 - 소용량 데이터에 적합)
            String content = "id,name,value\n1, test, 100";
            Files.write(filePath, content.getBytes());
            System.out.println("파일 크기: " + Files.size(filePath) + " bytes");

            // 4. 경로 정보 추출
            System.out.println("파일명: " + filePath.getFileName());
            System.out.println("부모 경로: " + filePath.getParent());

        } catch (IOException e) {
            e.printStackTrace();
        }
    
        // NioBufferAndChannel
        /* Buffer와 FileChannel: 대용량 데이터 고속 입출력 
            NIO의 핵심은 데이터를 스트림(Stream) 방식이 아닌 버퍼(덩어리) 단위로 채널을 통해 이동시키는 것입니다.
            이는 디스크 I/O 병목을 줄이는 데 필수적입니다.
            특히 flip()과 clear()를 통한 버퍼 상태(position, limit) 제어 흐름을 이해하는 것이 중요합니다.
         */

        Path dirPath2 = Paths.get("ExData");
        Path filePath2 = dirPath2.resolve("javanio.txt");

        // 1. 디렉터리가 없을 시 생성
        try {
            if (Files.notExists(dirPath2)) {
                Files.createDirectories(dirPath2);
                System.out.println("디렉터리 생성 완료: " + dirPath2);
            }

            // 2. 쓰기 및 읽기 모드로 채널 오픈(파일이 없으면 생성)
            try (FileChannel channel = FileChannel.open(filePath2,
                StandardOpenOption.CREATE,
                StandardOpenOption.WRITE,
                StandardOpenOption.READ)) {

                // 3. 버퍼 생성(임시 메모리 공간 할당)
                ByteBuffer buffer = ByteBuffer.allocate(1024); // 1KB

                // 4. 버퍼에 데이터 쓰기(프로그램 -> 버퍼)
                String inputData = "Data Engineering Pipeline Test";
                buffer.put(inputData.getBytes());

                // 5. 버퍼 모드 전환(쓰기 모드 -> 읽기 모드)
                // position을 0으로, limit을 현재 쓰인 데이터 끝으로 이동
                buffer.flip();

                // 6. 채널을 통해 파일에 쓰기(버퍼 -> 파일)
                channel.write(buffer);

                // --- 파일에서 다시 데이터 읽기 테스트 ---
                channel.position(0); // 파일 포인터를 처음으로 되돌림
                buffer.clear(); // 버퍼 초기화(새로운 데이터를 담을 준비)

                // 7. 파일에서 데이터 읽기(파일 -> 버퍼)
                int bytesRead = channel.read(buffer);

                if (bytesRead > 0) {
                    buffer.flip(); // 읽은 데이터를 꺼내기 위해 모드 전환
                    byte[] readData = new byte[buffer.limit()];
                    buffer.get(readData); // 버퍼에서 데이터 꺼내기
                    System.out.println("읽어온 데이터: " + new String(readData));
                }
            } 
        } catch (IOException e) {
                e.printStackTrace();
        }
        
        // NioWatchService
        /* WatchService: 특정 디렉터리 실시간 감시
	         정기적인 배치(Batch) 작업 외에, FTP나 외부 시스템으로부터 새로운 파일이 특정 폴더에 떨어졌을 때
	         즉각적으로 이벤트를 감지하고 후속 처리(ex: 데이터 파싱, DB 적재)를 시작하도록 구성할 때 사용됩니다.
        */
        try {
        
            //1. WatchService 객체 생성
            WatchService watchService = FileSystems.getDefault().newWatchService();
            Path path = Paths.get("Exdata");

            // 2. 감시할 이벤트 종류 등록 (생성, 수정, 삭제)
            path.register(watchService,
                StandardWatchEventKinds.ENTRY_CREATE,
                StandardWatchEventKinds.ENTRY_MODIFY,
                StandardWatchEventKinds.ENTRY_DELETE);
            
            System.out.println("디렉터리 감시 시작: " + path);

            // 3. 이벤트 발생 대기 루프
            while (true) {
                WatchKey key = watchService.take(); // 이벤트 발생까지 블로킹 대기
                
                // 4. 발생한 이벤트 목록 순회 및 처리
                for (WatchEvent<?> event : key.pollEvents()) {
                    WatchEvent.Kind<?> kind = event.kind();
                    Path targetPath = (Path) event.context(); // 이벤트가 발생한 파일명

                    if (kind == StandardWatchEventKinds.ENTRY_CREATE) {
                        System.out.println("[신규 데이터 유입 감지] 파일명: " + targetPath);
                        // TODO: 해당 파일을 읽어서 가공하는 파이프라인 로직 호출                        
                    } else if (kind == StandardWatchEventKinds.ENTRY_MODIFY) {
                        System.out.println("[파일 수정 감지] 파일명: " + targetPath);                        
                    } else if (kind == StandardWatchEventKinds.ENTRY_DELETE) {
                        System.out.println("[파일 삭제 감지 파일명: " + targetPath);
                    }

                }

                // 5. 다음 이벤트를 받기 위해 WatchKey 상태 초기화
                boolean valid = key.reset();
                if (!valid) {
                    System.out.println("디렉터리 감시가 더 이상 유효하지 않습니다. 루프를 종료합니다.");
                    break;
                }
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

---
### java.time

- 자바 8부터 도입된 패키지로, 기존의 `java.util.Date`나 `Calendar`의 단점을 보완하고 직관적이고 안전한 날짜/시간 API를 제공합니다.
- 주요 클래스: `LocalDate`, `LocalTime`, `LocalDateTime`, `ZonedDateTime`.

---
### java.net

- 인터넷 및 네트워크 통신과 관련된 기능을 제공합니다.
- 주요 클래스: `URL`, `Socket`, `ServerSocket`, `HttpURLConnection`.


---
### java.math 

- 기본 자료형의 범위를 벗어나거나 소수점 오차 없이 매우 정밀한 계산이 필요할 때 사용합니다.
- 주요 클래스: `BigInteger`(무한대의 정수, `BigDecimal`(오차없는 실수 연산).

---
### java.sql

- 자바 프로그램과 관계형 데이터베이스(RDBMS)를 연결하고 데이터를 조작하기 위한 JDBC(Java Database Connectivity) API를 제공합니다.
- 주요 인터페이스: `Connection`, `Statement`, `PreparedStatement`, `ResultSet`.

---

## 03. 

## 04. 

## 05. 

## 06. 

## 07. 