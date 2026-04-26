import requests
import os

def send_morning_alarm():
    # 1. 환경 변수에서 웹훅 주소와 유저 ID 불러오기
    webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
    user_id = os.environ.get('TARGET_USER_ID')

    if not webhook_url or not user_id:
        print("웹훅 URL이나 유저 ID가 설정되지 않았습니다.")
        return

    # 2. 디스코드 멘션 포맷: <@유저ID>
    # 텍스트 안에 이 포맷을 넣으면 디스코드에서 파란색 태그와 함께 알림이 갑니다.
    message_content = f"<@{user_id}> 기상할 시간입니다! ⏰ 좋은 아침이에요!"

    payload = {
        "content": message_content
    }

    # 3. 디스코드로 POST 요청 보내기
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        print("✅ 디스코드 알림 전송 성공!")
    except requests.exceptions.RequestException as e:
        print(f"❌ 전송 실패: {e}")

if __name__ == "__main__":
    send_morning_alarm()
