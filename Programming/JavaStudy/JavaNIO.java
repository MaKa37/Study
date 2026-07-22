package JavaStudy;

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