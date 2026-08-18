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

def prompt_details(prompts): return "menu"
def add_prompt(prompts): return "menu"
def show_list(prompts): return "menu"
def view_by_category(prompts): return "menu"
def search_prompt(prompts): return "menu"
def manage_favorites(prompts): return "menu"
def show_favorites(prompts): return "menu"