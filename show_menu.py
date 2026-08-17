#show_menu()
def show_menu():
    menu = {1: "프롬프트 추가", 2: "프롬프트 목록", 3: "카테고리별 조회",4:"프롬프트 검색",5:"프롬프트 상세 보기",6:"즐겨찾기 관리",7:"즐겨찾기 목록" ,0: "종료"}
    function = {1: add_prompt, 2: show_list, 3: view_by_category, 4: search_prompt, 5: prompt_details, 6: manage_favorites, 7: show_favorites}
    choice = None
    while choice != "0":
        print("=== 나만의 프롬프트 관리 ===")
        for key in menu:
            print(f"{key}. {menu[key]}")
        choice = input("선택: ")
        if choice.isdigit() and int(choice) in function:
            function.get(int(choice))()
        elif choice == "0":
            break
        else: 
            print("잘못된 선택입니다. 다시 선택해주세요.")
    print("프로그램을 종료합니다.")

def add_prompt(): print("[미구현] 프롬프트 추가")
def show_list(): print("[미구현] 프롬프트 목록")
def view_by_category(): print("[미구현] 카테고리별 조회")
def search_prompt(): print("[미구현] 프롬프트 검색")
def prompt_details(): print("[미구현] 프롬프트 상세 보기")
def manage_favorites(): print("[미구현] 즐겨찾기 관리")
def show_favorites(): print("[미구현] 즐겨찾기 목록")

if __name__ == "__main__":
    show_menu()