import json

class QuizGame:
    def __init__(self):
        self.quiz_list = []
        self.score = 0
        self.best_score = self.load_best_score()

    def add_quiz(self, quiz):
        self.quiz_list.append(quiz)

    def show_quizzes(self):
        print("\n===== 전체 퀴즈 =====")

        for quiz in self.quiz_list:
            quiz.show()
            print(f"정답: {quiz.answer}")
            
    def start_quiz(self):
        self.score = 0

        print("===== 퀴즈 시작 =====")

        for quiz in self.quiz_list:
            quiz.show()
 
            answer = input("정답을 입력하세요 : ")

            if quiz.check_answer(answer):
                print("정답입니다!")
                self.score += 1
            else:
                print("오답입니다.")

            print("입력한 답 :", answer)

        print()
        print("===== 결과 =====")
        print("최종 점수 :", self.score)            

        self.save_score()

        print("최고 점수 :", self.best_score)

    def save_score(self):
        if self.score > self.best_score:
            self.best_score = self.score
    
        data = {
            "best_score": self.score
        }

        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_best_score(self):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("best_score", 0)

        except FileNotFoundError:
            return 0