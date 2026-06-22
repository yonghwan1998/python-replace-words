HWP Word Replacer (Windows Executable)

이 프로젝트는 Windows 실행 파일(.exe) 형태로 동작하는 한글 문서(HWP/HWPX) 일괄 치환 프로그램입니다.

실행 파일과 같은 폴더에 있는 모든 한글 문서를 탐색하여 지정한 단어를 다른 단어로 변경한 후, 변경된 단어를 노란색 형광펜으로 표시하여 결과 파일을 생성합니다.

원본 파일은 별도로 보관되며, 수정된 파일은 별도 폴더에 저장됩니다.

⸻

📌 주요 기능

* HWP / HWPX 파일 자동 탐색
* 특정 단어 일괄 변경
* 변경된 단어 자동 하이라이트 처리
* 원본 파일 자동 백업
* 수정본 자동 분리 저장
* 파일명 유지
* Windows 단일 실행 파일(.exe) 배포 가능

⸻

📁 폴더 구조 예시

실행 전

문서작업/
 ├─ 계약서1.hwp
 ├─ 계약서2.hwp
 ├─ 견적서.hwpx
 └─ hwp_word_replacer.exe

실행 후

문서작업/
 ├─ 계약서1.hwp
 ├─ 계약서2.hwp
 ├─ 견적서.hwpx
 ├─ hwp_word_replacer.exe
 │
 ├─ origin/
 │   ├─ 계약서1.hwp
 │   ├─ 계약서2.hwp
 │   └─ 견적서.hwpx
 │
 └─ replaced/
     ├─ 계약서1.hwp
     ├─ 계약서2.hwp
     └─ 견적서.hwpx

⸻

👤 사용자 매뉴얼 (User Manual)

1️⃣ 사용 방법

1. hwp_word_replacer.exe를 한글 파일이 있는 폴더에 복사합니다.
2. 실행 파일을 더블 클릭합니다.
3. 첫 번째 입력창에 바꿀 단어를 입력합니다.
4. 두 번째 입력창에 바뀔 단어를 입력합니다.
5. 자동으로 모든 문서를 처리합니다.
6. 완료 메시지가 표시됩니다.

⸻

2️⃣ 처리 결과

origin 폴더

원본 문서를 보관합니다.

origin/
 ├─ 계약서1.hwp
 ├─ 계약서2.hwp
 └─ 견적서.hwpx

replaced 폴더

단어가 변경된 결과 문서를 저장합니다.

replaced/
 ├─ 계약서1.hwp
 ├─ 계약서2.hwp
 └─ 견적서.hwpx

⸻

3️⃣ 하이라이트 처리

예시

변경 전

홍길동

변경 후

김철수

변경된 단어는 노란색 형광펜으로 표시됩니다.

⸻

4️⃣ 주의사항

* 원본 문서는 수정되지 않습니다.
* 결과 문서는 replaced 폴더에 생성됩니다.
* 한컴오피스 한글이 설치되어 있어야 합니다.
* HWP/HWPX 파일만 처리됩니다.
* 암호가 걸린 문서는 처리되지 않을 수 있습니다.

⸻

🧑‍💻 개발자 매뉴얼 (Developer Manual)

1️⃣ 개발 환경

* Python 3.10 이상
* Windows 10 / 11
* 한컴오피스 한글 설치

사용 라이브러리

pywin32
pyinstaller
tkinter

⸻

2️⃣ 라이브러리 설치

pip install pywin32 pyinstaller

⸻

3️⃣ 프로젝트 구조

project/
 ├─ replace_hwp_words.py
 ├─ README.md
 └─ dist/
     └─ hwp_word_replacer.exe

⸻

4️⃣ 실행 흐름

1. 사용자 입력
    * 변경 전 단어
    * 변경 후 단어
2. 현재 폴더 탐색
3. HWP/HWPX 파일 검색
4. origin 폴더 생성
5. replaced 폴더 생성
6. 원본 백업
7. 단어 일괄 치환
8. 변경 단어 하이라이트
9. 결과 저장
10. 완료 메시지 출력

⸻

5️⃣ EXE 빌드 방법

pyinstaller --onefile --noconsole --name hwp_word_replacer replace_hwp_words.py

생성 파일

dist/hwp_word_replacer.exe

⸻

6️⃣ 기술 스택

기술	용도
Python	메인 로직
pywin32	한글 COM 자동화
tkinter	입력창 UI
PyInstaller	EXE 빌드

⸻

7️⃣ 동작 원리 요약

사용자 입력
      ↓
한글 파일 검색
      ↓
원본 백업
      ↓
단어 일괄 치환
      ↓
하이라이트 적용
      ↓
결과 저장
      ↓
완료 메시지

⸻

📄 라이선스

본 프로젝트는 개인 및 사내 업무 자동화 용도로 자유롭게 사용할 수 있습니다.
