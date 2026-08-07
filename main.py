from quiz import Quiz
from quiz_game import QuizGame

game = QuizGame()

game.add_quiz(
    Quiz(
        "피카츄의 타입은?",
        ["불", "전기", "물", "풀"],
        2
    )
)

game.add_quiz(
    Quiz(
        "이상해씨의 타입은?",
        ["불", "풀", "물", "전기"],
        2
    )
)

game.add_quiz(
    Quiz(
        "파이리의 타입은?",
        ["불", "풀", "물", "전기"],
        1
    )
)

game.add_quiz(
    Quiz(
        "꼬부기의 타입은?",
        ["불", "풀", "물", "전기"],
        3
    )
)

game.add_quiz(
    Quiz(
        "뮤는 전설의 포켓몬인가?",
        ["예", "아니오"],
        1
    )
)

wwhile True:
    print("\n===== 포켓몬 퀴즈 =====")
    print("1. 퀴즈 풀기")
    print("2. 최고 점수 보기")
    print("3. 종료")

    try:
        menu = int(input("번호를 입력하세요 : "))

        if menu == 1:
            game.start_quiz()

        elif menu == 2:
            print(f"\n현재 최고 점수 : {game.best_score}점")

        elif menu == 3:
            print("\n프로그램을 종료합니다.")
            break

        else:
            print("\n1~3 사이의 번호를 입력하세요.")

    except ValueError:
        print("\n숫자만 입력하세요.")
