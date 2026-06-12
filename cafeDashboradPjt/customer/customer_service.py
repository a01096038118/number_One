import os
import json
from customer import config as customer_config


class CustomerService:

    def __init__(self):
        self.customers = {}
        self.init_database()

    def run(self):
        
        flag = True
        while flag:
            menuNum = int(input('1.고객 등록 2.고객 조회 3.고객 수정 4.고객 삭제 0.종료'))

            if menuNum == customer_config.CUSTOMER_CREATE:
                self.customerCreate()
            elif menuNum == customer_config.CUSTOMER_READ:
                self.customerRead()
            elif menuNum == customer_config.CUSTOMER_UPDATE:
                self.customerUpdate()
            elif menuNum == customer_config.CUSTOMER_DELETE:
                self.customerDelete()
            elif menuNum == customer_config.SERVICE_OUT:
                flag = False
    
    def customerCreate(self):
        cId = input('등록할 ID 입력: ')
        cName = input('등록할 이름 입력: ')
        cPhone = input('등록할 전화번호 입력: ')

        customers = {
            '고객 ID': cId,
            '고객 이름': cName,
            '고객 전화번호': cPhone,
            '등급': '일반',
            '포인트': 0
        }

        self.customers[cId] = customers

        self.save_customers(self.customers)

    def customerRead(self):
        self.customers = self.load_customers()
        print(f'{self.customers}')
        
    def customerUpdate(self):
        cId = input ('정보 수정할 고객 ID입력: ')

        for key in self.customers.keys():
            if key == cId:
                newCName = input ('New 이름 입력: ')
                newCPhone = input ('New 전화번호 입력: ')

        self.customers[key]['고객 이름'] = newCName
        self.customers[key]['고객 전화번호'] = newCPhone

        print('고객님의 정보 수정이 완료되었습니다.')

        self.save_customers(self.customers)

    def customerDelete(self):
        confirm = input('정말 고객 탈퇴를 하시겠습니까? [Y] or [N]')
        if confirm == 'y':
            self.customers = self.load_customers()
            deleteId = input('삭제할 고객님 ID 입력: ')
            if deleteId in self.customers:
                del self.customers[deleteId]
    
        self.save_customers(self.customers)
        
        print('탈퇴 완료되었습니다.')

            
    def init_database(self):
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'customers.json')
        print(f'self.dbFile: {self.dbFile}')

        if not os.path.exists(self.dbFile):
            self.save_customers(self.customers)
        else:
            self.customers = self.load_customers()

    def save_customers(self, customers):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(customers, f, ensure_ascii=False, indent=4)
    
    def load_customers(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)

if __name__ == "__main__":
    customerService = CustomerService()
    customerService.run()