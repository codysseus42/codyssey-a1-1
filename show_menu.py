#show_menu()
MENU = {1: "프롬프트 추가", 
            2: "프롬프트 목록",
            3: "카테고리별 조회",
            4: "프롬프트 검색",
            5: "프롬프트 상세 보기",
            6: "즐겨찾기 관리",
            7: "즐겨찾기 목록",
            0: "종료"
        }
def show_menu():
        print("=== 나만의 프롬프트 관리 ===")
        for key, label in MENU.items():
            print(f"{key}. {label}")

def add_prompt(): print("[미구현] 프롬프트 추가")
def show_list(): print("[미구현] 프롬프트 목록")
def view_by_category(): print("[미구현] 카테고리별 조회")
def search_prompt(): print("[미구현] 프롬프트 검색")
def prompt_details(): print("[미구현] 프롬프트 상세 보기")
def manage_favorites(): print("[미구현] 즐겨찾기 관리")
def show_favorites(): print("[미구현] 즐겨찾기 목록")