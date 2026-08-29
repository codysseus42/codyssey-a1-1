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
            6: "기타",
            0: "종료"
        }

def find_by_id(prompts, target_id):
    for p in prompts:
        if p["id"] == target_id:
            return p
    return None
    
def print_prompt_lines(prompts):
    for i, p in enumerate(prompts, 1):
        star = " ⭐️" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] 제목: {p['title']}{star}, ID: {p['id']}, CNT:{p['cnt']}")
    print(f"총 {len(prompts)}개의 프롬프트가 있습니다.")

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
        p["cnt"] += 1
        print(
                f"제목: {p['title']}\n"
                f"카테고리: {p['category']}\n"
                f"즐겨찾기: {star}\n"
                f"조횟수: {p['cnt']}\n"
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

        prompt = {"id":max((p["id"] for p in prompts), default=0) + 1, "title":title,"content":content,"category":CATEGORY[category],"favorite":False, "cnt":0}
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
        print_prompt_lines(prompts)

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

def view_by_category(prompts):
    print("=== 카테고리별 조회 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return "menu"
    print("카테고리 선택")
    for key, label in CATEGORY.items():
        print(f"{key}) {label}")
    while True:
        category = input("선택:").strip()
        if not category:
            print("카테고리를 선택해주세요.")
            continue
        if not category.isdigit():
            print("카테고리 목록의 번호를 선택해주세요.")
            continue
        category = int(category)
        if category == 0:
            return "menu"
        if category in CATEGORY:
            category_prompts = []
            for p in prompts:
                if p['category'] == CATEGORY[category]:
                    category_prompts.append(p)
            if not category_prompts:
                print(f"{category}) {CATEGORY[category]}에 속한 프롬프트가 없습니다.")
                continue
            else:
                print_prompt_lines(category_prompts)
                continue
        else : 
            print("카테고리 목록의 번호를 선택해주세요.")

def search_prompt(prompts):
    print("=== 프롬프트 검색 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return "menu"
    while True:
        print("프롬프트 검색 메뉴로 나가려면 0을 눌러주세요.===")
        keyword = input("검색어:").strip()
        if keyword == "0":
                return "menu"
        if not keyword:
            print("검색어를 입력해주세요.")
            continue
        results = []
        for p in prompts:
            if keyword.lower() in p['title'].lower() or keyword.lower() in p['content'].lower():
                results.append(p)
        if not results:
            print("검색 결과가 없습니다.")
            continue
        for i, p in enumerate(results, 1):
            star = " ⭐️" if p["favorite"] else ""
            print(f"{i}. [{p['category']}] 제목: {p['title']}{star}, ID: {p['id']}, CNT:{p['cnt']}\n")
            pos = p['content'].lower().find(keyword)
            if pos != -1:
                start = max(0, pos - 10)
                end = pos + len(keyword) + 10
                print(f"   ...{p['content'][start:end]}...")
        print(f"총 {len(results)}개의 프롬프트가 있습니다.")
    
def manage_favorites(prompts):
    while True:
        print("===즐겨찾기 관리===")
        if not prompts:
            print("등록된 프롬프트가 없습니다.")
            return "menu"
        print_prompt_lines(prompts) 
        print("즐겨찾기에 추가할 또는 이미 추가 되어 있으면 제외할 프롬프트 번호를 입력해주세요. 메뉴로 나가려면 0을 입력해주세요.")
        choice = input("선택: ").strip()
        if choice == "0":
            return "menu"
        if not choice.isdigit():
            print("목록의 번호를 선택해주세요.")
            continue
        idx = int(choice)
        if 1 <= idx <= len(prompts):
            p = prompts[idx-1]
            p['favorite'] = not p['favorite']
            state = "추가" if p['favorite'] else "제외"
            print(f"\"{p['title']}\"을(를) 즐겨찾기 {state}했습니다.")
        else:
            print("목록에 있는 번호를 선택해주세요.")

def show_favorites(prompts):
    print("=== 즐겨찾기 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return "menu"
    favorites_prompts = []
    for p in prompts:
        if p['favorite']:favorites_prompts.append(p)
    if not favorites_prompts:
        print("즐겨찾기에 등록된 프롬프트가 없습니다.")
        return "menu"
    else:
        print_prompt_lines(favorites_prompts)
        return "menu"
                
