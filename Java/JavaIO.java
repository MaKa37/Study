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
