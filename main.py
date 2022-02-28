import schedule
import time
import vk_api

token = "ee1f9f574bbd1f374401329b1ab0ea2b81dccbb526aa520a80b1cd6d918f7ba1aa933bb2059704c1d6b10"
user_id = "282697786"
message = "message"

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()


def message_delivery():
    vk.messages.send(user_id=user_id, message=message, random_id=0)


schedule.every().hour.do(message_delivery)

while True:
    schedule.run_pending()
    time.sleep(1)
