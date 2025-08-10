"""
ISP - 인터페이스 분리 원칙
클라이언트가 사용하지 않는 인터페이스에 의존하지 않게 한다.
"""

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self):
        print("문서 출력")
    def scan_document(self):
        print("문서 스캔")

class SimplePrinter(Printer):
    def print_document(self):
        print("문서 출력")

if __name__ == "__main__":
    mfp = MultiFunctionPrinter()
    mfp.print_document()
    mfp.scan_document()

    printer = SimplePrinter()
    printer.print_document()
