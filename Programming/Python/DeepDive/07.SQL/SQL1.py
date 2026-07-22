import os
import psycopg2
from dotenv import load_dotenv

# DB.env 파일의 절대 경로 지정 (r을 붙여 백슬래시 이스케이프 방지)
env_path = r"C:\Users\foodg\Desktop\GoogleDrive\Github\Study\DB.env"

# dotenv_path 파라미터를 사용하여 해당 경로의 파일 불러오기
load_dotenv(dotenv_path=env_path)

# os.getenv()를 사용하여 환경변수 값 가져오기
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': int(os.getenv('DB_PORT', 5432))
}

def fetch_hr_data():
    conn = None
    cursor = None
    
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        sql_query = """
        SELECT
            d.dept_name AS "부서명",
            e.name AS "직원명",
            e.salary AS "급여",
            SUM(e.salary) OVER (
                PARTITION BY e.dept_id
                ORDER BY e.salary DESC
            ) AS "부서내급여_누적합계",
            e.salary - LAG(e.salary, 1, 0) OVER (
                PARTITION BY e.dept_id 
                ORDER BY e.salary DESC
            ) AS "앞사람과의_급여격차"
        FROM hr.employees e
        INNER JOIN hr.departments d ON e.dept_id = d.dept_id
        ORDER BY d.dept_name, e.salary DESC;
        """

        cursor.execute(sql_query)
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]

        header = " | ".join(f"{name:<15}" for name in col_names)
        print(header)
        print("-" * len(header))
        
        for row in rows:
            formatted_row = " | ".join(f"{str(val):<15}" for val in row)
            print(formatted_row)

    except (Exception, psycopg2.Error) as error:
        print("PostgreSQL 데이터를 가져오는 중 오류가 발생했습니다:", error)
        
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    fetch_hr_data()