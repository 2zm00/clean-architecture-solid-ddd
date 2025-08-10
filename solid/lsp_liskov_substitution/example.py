"""
LSP - 리스코프 치환 원칙
하위 클래스는 상위 클래스의 행위를 대체할 수 있어야 한다.
"""

class Bird:
    def fly(self):
        print("새가 난다")

class Sparrow(Bird):
    pass

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("타조는 날 수 없습니다!")

def make_bird_fly(bird: Bird):
    bird.fly()

if __name__ == "__main__":
    make_bird_fly(Sparrow())  # OK
    make_bird_fly(Ostrich())  # LSP 위반: 실행 시 예외 발생
