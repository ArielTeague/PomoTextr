import time
import send_sms


def startSingleClassicCycle(phone_number):
    send_sms.send_message(phone_number, 'Starting your pomodoro in sixty seconds!')
    time.sleep(60)
    for i in range(0, 3):
        send_sms.send_message(phone_number, 'Start working!')
        time.sleep(1500)
        send_sms.send_message(phone_number, 'Five minute break!')
        time.sleep(300)
    send_sms.send_message(phone_number, 'Start working!')
    time.sleep(1500)
    send_sms.send_message(phone_number, 'Congratulations! Time for a longer break!')
