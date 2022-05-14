from copy import deepcopy

# 기본 답변
base_response = {"version": "2.0", "template": {"outputs": [], "quickReplies": []}}
card_base_response = {"contents": [], "quickReplies": []}


# 카카오톡 채널 - 텍스트 응답
def insert_text(text):
    new_response = deepcopy(base_response)
    new_response["template"]["outputs"] = [{"simpleText": {"text": text}}]
    return new_response


# 카카오톡 채널 - 이미지 응답
def insert_image(image_url, alt_text):
    new_response = deepcopy(base_response)
    new_response["template"]["outputs"] = [
        {"simpleImage": {"imageUrl": image_url, "altText": alt_text}}
    ]
    return new_response


# 카카오톡 채널 - 카드 응답
def make_card(title, description, image_url):
    new_response = deepcopy(card_base_response)
    new_response["contents"] = [
        {
            "type": "card.image",
            "cards": [
                {
                    "title": title,
                    "imageUrl": image_url,
                    "description": description,
                    "linkUrl": {},
                    "buttons": [
                        {"type": "url", "label": "이미지 상세", "data": {"url": image_url}}
                    ],
                }
            ],
        }
    ]

    return new_response


def insert_card(new_response, title, description, image_url):
    new_response["contents"][0]["cards"].append(
        {
            "title": title,
            "imageUrl": image_url,
            "description": description,
            "linkUrl": {},
            "buttons": [{"type": "url", "label": "이미지 상세", "data": {"url": image_url}}],
        }
    )


# 카카오톡 채널 - 카드 버튼 추가
def insert_card_button(new_response, label, webUrl):
    new_response["template"]["outputs"][0]["basicCard"]["buttons"].append(
        {"action": "webLink", "label": label, "webLinkUrl": webUrl}
    )
    return new_response


# 카카오톡 채널 - 하단 버튼 추가
def insert_replies(new_response, reply):
    new_response["template"]["quickReplies"].append(reply)
    return new_response


# 카카오톡 채널 - 하단 버튼 생성
def make_reply(label, message):
    return {"action": "message", "label": label, "messageText": message}


def make_item(title, description, url):
    items = {
        "title": title,
        "description": description,
        "imageUrl": None,
        "link": {"web": url},
    }
    return items


def list_card(title, subtitle, description, url):
    new_response = deepcopy(base_response)
    new_response["template"]["outputs"] = [
        {
            "listCard": {
                "header": {"title": title},
                "items": [
                    {
                        "title": subtitle,
                        "description": description,
                        "imageUrl": None,
                        "link": {"web": url},
                    },
                ],
                "buttons": None,
            }
        }
    ]
    return new_response


def carousel_basic_card(title, description):
    new_response = deepcopy(base_response)
    new_response["template"]["outputs"] = [
        {
            "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "title": title,
                        "description": description,
                        "buttons": [],
                        "thumbnail": {}
                    }
                ]
            }
        }
    ]
    return new_response


def insert_carousel_image(new_response, image_url):
    new_response["template"]["outputs"][0]["carousel"]["items"][-1]["thumbnail"]["imageUrl"] = image_url
    return new_response


def insert_carousel_button(new_response, label, web_url):
    new_response["template"]["outputs"][0]["carousel"]["items"][-1]["buttons"].append(
        {"action": "webLink", "label": label, "webLinkUrl": web_url}
    )
    return new_response


def insert_carousel_item(new_response, title, description, output_index=0):
    new_response["template"]["outputs"][output_index]["carousel"]["items"].append(
        {
            "title": title,
            "description": description,
            "buttons": [],
            "thumbnail": {}
        }
    )
    return new_response


def insert_carousel_output(new_response, title, description):
    new_response["template"]["outputs"].append(
        {
            "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "title": title,
                        "description": description,
                        "buttons": [],
                        "thumbnail": {}
                    }
                ]
            }
        }
    )
    return new_response


def insert_multiple_reply(answer, replies):
    for label, real in replies:
        tmp_reply = make_reply(label, real)
        answer = insert_replies(answer, tmp_reply)
    return answer

