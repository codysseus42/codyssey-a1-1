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

CATEGORY = {
            1: "텍스트 생성", 
            2: "이미지 생성",
            3: "영상 생성",
            4: "페르소나",
            5: "자동화",
            6: "기타"
        }

def find_by_id(prompts, target_id):
    for p in prompts:
        if p["id"] == target_id:
            return p
    return None

def show_menu():
        print("=== 나만의 프롬프트 관리 ===")
        for key, label in MENU.items():
            print(f"{key}. {label}")

def prompt_details(prompts,index = None): 
    print("=== 프롬프트 상세 보기 ===")
    while True:
        if index is not None:
            p=prompts[index]
        else:
            choice = input("프롬프트 ID를 입력해주세요. 메뉴로 나가려면 0을, 이전메뉴로 돌아가려면 b를 입력해주세요..\n 번호 입력: ").strip()
            if choice == "b":
                return "back"
            if not choice.isdigit():
                print("올바른 번호를 입력해주세요.")
                continue
            if choice == "0":
                    return "menu"
            p = find_by_id(prompts, int(choice))
            if p is None:
                print("해당 ID를 가진 프롬프트가 없습니다.")
                continue   
        star = "⭐️" if p["favorite"] else ""
        print(
                f"제목: {p['title']}\n"
                f"카테고리: {p['category']}\n"
                f"즐겨찾기: {star}\n"
                f"내용:\n{p['content']}\n\n"
            )
        index = None

def add_prompt(prompts):
    while True:
        print("=== 프롬프트 추가 ===")
        print("메뉴로 나가려면 0을 이전메뉴로 돌아가려면 99을 입력해주세요..")
        while True:
            title = input("제목:").strip()
            if not title:
                print("제목을 입력 해주세요.")
                continue
            if title == "0":
                return "menu"
            if title == "99":
                return "back"
            duplicated = False
            for p in prompts:
                if p["title"] == title:
                    duplicated = True
                    break
            if duplicated:    
                print("중복된 제목의 프롬프트를 추가 할 수 없습니다.")
                continue
            break

        while True:
            content = input("내용:").strip()
            if not content:
                print("내용을 입력 해주세요.")
                continue
            if content == "0":
                return "menu"
            if content == "99":
                return "back"
            break

        while True:
            print("카테고리 선택")
            for key, label in CATEGORY.items():
                print(f"{key}) {label}")
            category = input("선택:").strip()
            if not category:
                print("카테고리를 선택해주세요.")
                continue
            if not category.isdigit():
                print("카테고리 목록의 번호를 선택해주세요.")
                continue
            if category == "0":
                return "menu"
            if category == "99":
                return "back"
            category = int(category)
            if category in CATEGORY:
                break
            print("카테고리 목록의 번호를 선택해주세요.") 

        prompt = {"id":max((p["id"] for p in prompts), default=0) + 1, "title":title,"content":content,"category":CATEGORY[category],"favorite":False}
        prompts.append(prompt)
        print("프롬프트가 추가 되었습니다.")
        if prompt_details(prompts, len(prompts)-1) == "menu":
            return "menu"

def show_list(prompts):
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return "menu"

    while True:
        print("=== 프롬프트 목록 ===\n상세보기를 하려면 번호를, 메뉴로 나가려면 0을 입력해주세요.")
        for i, p in enumerate(prompts, 1):
            star = " ⭐️" if p["favorite"] else ""
            print(f"{i}. [{p['category']}] 제목: {p['title']}{star}, ID: {p['id']}")
        print(f"총 {len(prompts)}개의 프롬프트가 있습니다.")

        choice = input("선택: ").strip()
        if choice == "0":
            return "menu"
        if not choice.isdigit():
            print("목록의 번호를 선택해주세요.")
            continue

        idx = int(choice)
        if 1 <= idx <= len(prompts):
            if prompt_details(prompts, idx - 1) == "menu":
                return "menu"
        else:
            print("목록에 있는 번호를 선택해주세요.")
def view_by_category(prompts): return "menu"
def search_prompt(prompts): return "menu"
def manage_favorites(prompts): return "menu"
def show_favorites(prompts): return "menu"