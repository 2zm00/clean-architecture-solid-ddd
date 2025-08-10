"""
SRP - 단일 책임 원칙
한 클래스는 하나의 책임만 가져야 한다.
"""

class InvoicePrinter:
    def print_invoice(self, invoice_data):
        print(f"Invoice: {invoice_data}")

class InvoiceSaver:
    def save_to_db(self, invoice_data):
        print(f"Saving invoice to DB: {invoice_data}")

if __name__ == "__main__":
    data = {"customer": "홍길동", "amount": 50000}
    InvoicePrinter().print_invoice(data)
    InvoiceSaver().save_to_db(data)
