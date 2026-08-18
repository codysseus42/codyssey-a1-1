import function as fn

ACTIONS = {
    1: fn.add_prompt,
    2: fn.show_list,
    3: fn.view_by_category,
    4: fn.search_prompt,
    5: fn.prompt_details,
    6: fn.manage_favorites,
    7: fn.show_favorites,
}

def main():
    CAT_ANALYZER = """You are a content analyzer.
Read the following title and content, then follow these steps:

1. Check if it is about a cat.
   - If NOT about a cat, set isCat to "N", 
     leave sentiment and summary empty, and stop.
   - If about a cat, set isCat to "Y" and continue.

2. Write a brief summary of the post (1-2 sentences).

3. Analyze the sentiment and choose ONE:
   'positive', 'negative', or 'neutral'.

Return ONLY valid JSON in this exact format:
{
  "isCat": "Y or N",
  "sentiment": "positive, negative, or neutral",
  "summary": "brief summary here"
}

title: {{ $('Merge').item.json.title }}
content: {{ $('Merge').item.json.content }}"""
    MJ_CAT = """hyperrealistic photograph of an anthropomorphic ragdoll cat standing upright on two legs, gray bicolor coat with soft gray markings on the head and ears, 
creamy white face blaze, chest, arms and paws in uniform solid cream white, long fluffy silky fur, 
striking blue eyes, pink nose, wearing blue denim overalls, alert curious expression looking at camera, natural relaxed posture with weight on one leg and one paw slightly raised,
full body, plain light gray studio background, soft warm natural lighting, shot on 85mm lens, shallow depth of field, cinematic advertising photography
 --ar 3:4 --style raw --stylize 130 --weird 0"""
    MJ_FAMILY = """photorealistic candid family portrait, American family of three in a bright modern living room, 
father in his late 30s wearing a casual navy sweater, 
mother in her mid 30s wearing a beige cardigan, 
7 year old boy in a striped t-shirt, 
cinematic advertising photography, soft warm key light, shallow depth of field
--ar 3:2  --raw  --stylize 120 """
    prompts  = [{"id":1, "title":"노코드 고양이 정보","content":CAT_ANALYZER,"category":"자동화","favorite":True},{"id":2, "title":"고양이 사진 생성","content":MJ_CAT,"category":"이미지 생성","favorite":False},{"id":3, "title":"가족사진생성","content":MJ_FAMILY,"category":"이미지 생성","favorite":True}]
 #   prompts  = []
    while True:
        fn.show_menu()
        choice = input("선택: ").strip()

        if not choice.isdigit():
            print("메뉴에 있는 숫자를 입력해주세요.")
            continue

        choice = int(choice)
        if choice == 0:
            break
        if choice in ACTIONS:
            ACTIONS[choice](prompts)
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

    print("프로그램을 종료합니다.")

if __name__ == "__main__":
    main()