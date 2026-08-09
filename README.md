# mission02 두번째 미션

<< 환경 구축 >>
 - GitHub에서 mission02 repository 생성
 - git clone https://github.com/Patrick-sangwook/mission02.git //내 컴퓨터로 내려받기
  * 갓대희's 작은 공간 / codex, codex CLI / Superpowers 참고 예정


## 1. 🎮 Pokemon Quiz Game 프로젝트 개요

객체지향 프로그래밍(OOP)을 활용하여 제작한 Python 콘솔 기반의 포켓몬 퀴즈 게임
사용자는 퀴즈를 풀고, 새로운 퀴즈를 직접 추가할 수 있으며,
프로그램을 종료한 후 다시 실행해도 추가한 퀴즈와 최고 점수가
`state.json` 파일에 저장되어 그대로 유지됩니다.

## 2. 퀴즈 주제 선정 이유

포켓몬은 남녀노소 누구나 알고 있는 친숙한 캐릭터이며,
다양한 문제를 만들기 쉬워 퀴즈 프로그램의 주제로 선정
기본적으로 포켓몬의 타입, 특징 등을 문제로 구성하였으며,
사용자가 원하는 포켓몬 문제를 직접 추가할 수도 있도록 구현

## 3. 실행 방법

   - 저장소 이동 : cd mission02
   - 프로그램 실행 : python3 main.py

## 4. 기능 목록

 ① 퀴즈 풀기
- 등록된 모든 퀴즈를 순서대로 출제
- 정답 여부 확인
- 최종 점수 계산
- 최고 점수 자동 저장

 ② 퀴즈 추가
- 새로운 문제 입력
- 선택지 입력
- 정답 번호 입력
- 추가한 퀴즈 자동 저장

 ③ 퀴즈 목록
- 현재 등록된 모든 퀴즈 출력
- 기본 퀴즈와 추가한 퀴즈 확인 가능

 ④ 점수 확인
- 최근 점수 확인
- 최고 점수 확인

 ⑤ 종료
- 프로그램 종료

## 5. 파일 구조

mission02
│
├── main.py          # 프로그램 시작
├── quiz.py          # Quiz 클래스
├── quiz_game.py     # QuizGame 클래스
├── state.json       # 최고 점수 및 추가 퀴즈 저장
└── README.md

## 6. 데이터 파일 설명 (state.json)

프로그램에서 사용하는 데이터는 프로젝트 루트의
`state.json` 파일에 UTF-8 형식으로 저장

저장되는 내용은 다음과 같습니다.
- 최고 점수(best_score)
- 사용자가 추가한 퀴즈(custom_quizzes)

(예시)

{
    "best_score": 3,
    "custom_quizzes": [
        {
            "question": "지우의 대표 포켓몬은?",
            "choices": [
                "피카츄",
                "파이리",
                "꼬부기",
                "이상해씨"
            ],
            "answer": 1
        }
    ]
}

## 7. 사용한 클래스

 Quiz 클래스
퀴즈 한 문제를 관리하는 클래스입니다.

메서드
- `show()`
- `check_answer()`
- `to_dict()`

 QuizGame 클래스
게임 전체를 관리하는 클래스입니다.

메서드
- `start_quiz()`
- `add_quiz()`
- `show_quizzes()`
- `show_score()`
- `save_data()`
- `load_data()`

## 8. 구현한 객체지향 개념

본 프로젝트에서는 다음과 같은 객체지향 개념을 사용
- 클래스(Class)
- 객체(Object)
- 생성자(`__init__`)
- 메서드(Method)
- 캡슐화(데이터와 기능을 클래스 내부에서 관리)

## 9. 사용 기술
- Python 3
- Object-Oriented Programming(OOP)
- JSON 파일 저장
- UTF-8 Encoding
- Git
- GitHub

## 10. 프로젝트 결과

구현 완료 기능
- ✅ 퀴즈 풀기
- ✅ 퀴즈 추가
- ✅ 퀴즈 목록
- ✅ 점수 확인
- ✅ 최고 점수 저장
- ✅ JSON 파일 저장 및 불러오기
- ✅ 프로그램 재실행 후 데이터 유지
