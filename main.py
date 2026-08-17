import show_menu as sm

ACTIONS = {
    1: sm.add_prompt,
    2: sm.show_list,
    3: sm.view_by_category,
    4: sm.search_prompt,
    5: sm.prompt_details,
    6: sm.manage_favorites,
    7: sm.show_favorites,
}

def main():
    while True:
        sm.show_menu()
        choice = input("선택: ").strip()

        if not choice.isdigit():
            print("메뉴에 있는 숫자를 입력해주세요.")
            continue

        choice = int(choice)
        if choice == 0:
            break
        if choice in ACTIONS:
            ACTIONS[choice]()
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

    print("프로그램을 종료합니다.")

if __name__ == "__main__":
    main()