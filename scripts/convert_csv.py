import os
import glob
import json
import csv

def detect_and_read_csv(file_path):
    """한글 인코딩(EUC-KR, CP949, UTF-8)을 안전하게 감지하여 CSV 읽기"""
    encodings = ['utf-8-sig', 'euc-kr', 'cp949', 'utf-8']
    
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                print(f"✅ 성공적으로 읽음: {file_path} (인코딩: {enc})")
                return rows
        except (UnicodeDecodeError, Exception):
            continue
    
    raise ValueError(f"❌ {file_path} 파일의 인코딩을 판별할 수 없습니다.")

def process_dls_data():
    # 저장소 내의 csv 파일 검색 (data/dls.csv 또는 루트의 csv 파일)
    csv_files = glob.glob("*.csv") + glob.glob("data/*.csv")
    
    if not csv_files:
        print("⚠️ 변환할 CSV 파일이 없습니다.")
        return

    # 가장 최근에 추가/수정된 CSV 파일 선택
    target_csv = csv_files[0]
    print(f"📂 대상 CSV 파일: {target_csv}")

    raw_data = detect_and_read_csv(target_csv)
    parsed_books = []

    for row in raw_data:
        # 스마트 헤더 매핑 (DLS 추출 항목 대응)
        title = row.get('도서명') or row.get('서명') or row.get('표제') or row.get('Title') or ''
        author = row.get('저자') or row.get('저자명') or row.get('Author') or ''
        publisher = row.get('출판사') or row.get('Publisher') or ''
        kdc = row.get('KDC') or row.get('분류기호') or ''
        call_no = row.get('청구기호') or ''

        if title.strip():
            parsed_books.append({
                "title": title.strip(),
                "author": author.strip(),
                "publisher": publisher.strip(),
                "kdc": kdc.strip(),
                "callNo": call_no.strip()
            })

    # dls_books.json 파일로 저장
    output_path = "dls_books.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(parsed_books, f, ensure_ascii=False, indent=2)

    print(f"🎉 총 {len(parsed_books)}권의 도서 데이터가 '{output_path}' 파일로 저장되었습니다.")

if __name__ == "__main__":
    process_dls_data()
