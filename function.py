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
def show_list(prompts): 
    while True:
        if not prompts:
            print("프롬프트가 없습니다. 메뉴로 나가려면 0을 입력해주세요.")
        else:
            print("=== 프롬프트 목록 ===\n메뉴로 나가려면 0을 입력해주세요.")
            for i,p in enumerate(prompts,1):
                star = " ⭐️" if p["favorite"] else ""
                print(f"{i}. [{p['category']}] 제목: {p['title']}{star}, ID: {p['id']}")
            print(f"총 {len(prompts)}개의 프롬프트가 있습니다.")
        choice = input("선택: ").strip()
        if choice == "0":
            return "menu"
def view_by_category(prompts): return "menu"
def search_prompt(prompts): return "menu"
def manage_favorites(prompts): return "menu"
def show_favorites(prompts): return "menu"