from datetime import timedelta, datetime

if __name__ == '__main__':
    days = datetime.now() - datetime(2019, 8, 25)
    print(days.days + "일째 연애중")
