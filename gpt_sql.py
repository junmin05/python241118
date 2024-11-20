import sqlite3
import random

class ElectronicsDatabase:
    """전자제품 데이터를 관리하는 데이터베이스 클래스"""
    
    def __init__(self, db_name='electronics.db'):
        """
        데이터베이스 초기화 메서드
        Args:
            db_name (str): 데이터베이스 파일 이름 (기본값: 'electronics.db')
        """
        # SQLite 데이터베이스 연결 생성
        self.connection = sqlite3.connect(db_name)
        # 커서 객체 생성 (SQL 명령을 실행하는 객체)
        self.cursor = self.connection.cursor()
        # 테이블 생성 메서드 호출
        self.create_table()

    def create_table(self):
        """제품 정보를 저장할 테이블 생성"""
        # IF NOT EXISTS를 사용하여 테이블이 없을 때만 생성
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 자동 증가하는 제품 ID
                product_name TEXT NOT NULL,                    -- 제품명 (필수 입력)
                price REAL NOT NULL                           -- 가격 (필수 입력)
            )
        ''')
        # 변경사항 저장
        self.connection.commit()

    def insert_product(self, product_name, price):
        """
        새로운 제품을 데이터베이스에 추가
        Args:
            product_name (str): 제품명
            price (float): 제품 가격
        """
        # 매개변수화된 쿼리를 사용하여 SQL 인젝션 방지
        self.cursor.execute('''
            INSERT INTO products (product_name, price) 
            VALUES (?, ?)
        ''', (product_name, price))
        # 변경사항 저장
        self.connection.commit()

    def update_product(self, product_id, product_name, price):
        """
        기존 제품 정보를 수정
        Args:
            product_id (int): 수정할 제품의 ID
            product_name (str): 새로운 제품명
            price (float): 새로운 가격
        """
        self.cursor.execute('''
            UPDATE products 
            SET product_name = ?, price = ? 
            WHERE product_id = ?
        ''', (product_name, price, product_id))
        self.connection.commit()

    def delete_product(self, product_id):
        """
        제품을 데이터베이스에서 삭제
        Args:
            product_id (int): 삭제할 제품의 ID
        """
        self.cursor.execute('''
            DELETE FROM products 
            WHERE product_id = ?
        ''', (product_id,))
        self.connection.commit()

    def select_products(self):
        """
        모든 제품 정보를 조회
        Returns:
            list: 제품 정보 튜플의 리스트 [(id, name, price), ...]
        """
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def generate_sample_data(self, count=100):
        """
        테스트용 샘플 데이터 생성
        Args:
            count (int): 생성할 샘플 데이터 개수 (기본값: 100)
        """
        # 지정된 개수만큼 반복하여 샘플 데이터 생성
        for _ in range(count):
            # 5자리 랜덤 알파벳으로 제품명 생성
            product_name = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))
            # 10~1000 사이의 랜덤 가격 생성 (소수점 2자리까지)
            price = round(random.uniform(10, 1000), 2)
            # 생성된 데이터를 데이터베이스에 삽입
            self.insert_product(product_name, price)

    def close(self):
        """데이터베이스 연결 종료"""
        self.connection.close()

# 사용 예시
if __name__ == "__main__":
    # 데이터베이스 객체 생성
    db = ElectronicsDatabase()
    
    # 100개의 샘플 데이터 생성
    db.generate_sample_data(100)
    
    # 전체 데이터 조회 예시
    products = db.select_products()
    for product in products[:5]:  # 처음 5개만 출력
        print(f"ID: {product[0]}, Name: {product[1]}, Price: ${product[2]:.2f}")
    
    # 데이터베이스 연결 종료
    db.close()