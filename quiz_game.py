import json
from quiz import Quiz


class QuizGame:
    def __init__(self, default_quizzes):
        self.default_quizzes = default_quizzes
        self.custom_quizzes = []

        self.quiz_list = list(default_quizzes)

        self.score = 0
        self.best_score = 0

        self.load_data()

    def add_quiz(self, quiz):
        self.custom_quizzes.append(quiz)
        self.quiz_list.append(quiz)

        self.save_data()

    def show_quizzes(self):
        print()
        print(f"📋 등록된 퀴즈 목록 (총 {len(self.quiz_list)}개)")
        print()

        for i, quiz in enumerate(self.quiz_list):
            print(f"[{i + 1}] {quiz.question}")

    def start_quiz(self):
        self.score = 0

        print()
        print("==============================")
        print("🎮 포켓몬 퀴즈를 시작합니다!")
        print("==============================")

        for quiz in self.quiz_list:
            quiz.show()

            while True:
                try:
                    answer = int(input("정답 번호를 입력하세요 : "))

                    if 1 <= answer <= len(quiz.choices):
                        break

                    print(
                        f"⚠️ 1~{len(quiz.choices)} 사이의 번호를 입력하세요."
                    )

                except ValueError:
                    print("⚠️ 숫자만 입력하세요.")

            if quiz.check_answer(answer):
                print("✅ 정답입니다!")
                self.score += 1

            else:
                print("❌ 틀렸습니다!")
                print(f"정답은 {quiz.answer}번입니다.")

        print()
        print("==============================")
        print("🏁 퀴즈 종료")
        print("==============================")
        print(f"최종 점수 : {self.score} / {len(self.quiz_list)}")

        if self.score > self.best_score:
            self.best_score = self.score
            print("🎉 새로운 최고 점수입니다!")

        print(f"최고 점수 : {self.best_score}")

        self.save_data()

    def show_score(self):
        print()
        print("==============================")
        print("🏆 점수 확인")
        print("==============================")
        print(f"최근 점수 : {self.score}")
        print(f"최고 점수 : {self.best_score}")

    def save_data(self):
        data = {
            "best_score": self.best_score,
            "custom_quizzes": []
        }

        for quiz in self.custom_quizzes:
            data["custom_quizzes"].append(
                quiz.to_dict()
            )

        with open(
            "state.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

    def load_data(self):
        try:
            with open(
                "state.json",
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            self.best_score = data.get(
                "best_score",
                0
            )

            saved_quizzes = data.get(
                "custom_quizzes",
                []
            )

            for item in saved_quizzes:
                quiz = Quiz(
                    item["question"],
                    item["choices"],
                    item["answer"]
                )

                self.custom_quizzes.append(quiz)
                self.quiz_list.append(quiz)

        except FileNotFoundError:
            self.best_score = 0

        except json.JSONDecodeError:
            print(
                "⚠️ state.json 파일을 읽을 수 없습니다."
            )
            self.best_score = 0