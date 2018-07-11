import datetime
import pandas as pd
import os

sem_date = datetime.datetime.now() + datetime.timedelta(days=-(datetime.datetime.now().weekday() + 7))
semana0 = '2018-05-28'
semana = datetime.datetime.strptime(semana0, '%Y-%m-%d') + datetime.timedelta(days=7)


def txt_like_gen():
    mydir = os.getcwd()

    forecast_data = pd.read_csv(os.path.join(mydir,'Input','batch.txt'))
    output = []
    key = '67235950'
    for index, forecast in forecast_data.iterrows():
        # Get corresponding week number
        week = datetime.datetime.strptime(str(forecast['week']), '%Y-%m-%d').isocalendar()[1]
        if week < 10:
            week = '0' + str(week)
        else:
            week = str(week)
        # Get corresponding year
        # Warning: sometimes a week starts a certain year but belongs to the following one
        year = str(datetime.datetime.strptime(str(forecast['week']), '%Y-%m-%d').isocalendar()[0])
        # Save data
        this_monday = (
                datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday())
        )
        next_tuesday = this_monday + datetime.timedelta(days=7 - this_monday.weekday())
        # print(next_tuesday.replace(day=1))
        begin = (
                (next_tuesday.replace(day=1) + datetime.timedelta(days=32)).replace(day=1) -
                datetime.timedelta(
                    days=(next_tuesday.replace(day=1) + datetime.timedelta(days=32)).replace(day=1).weekday()
                )
        )
        # begin = datetime.datetime.strptime('2018-04-30','%Y-%m-%d').date()
        # print(datetime.datetime.strptime(str(forecast['week']), '%Y-%m-%d').date()), begin
        if datetime.datetime.strptime(str(forecast['week']), '%Y-%m-%d').date() >= begin.date():
            output.append(
                list(key) + [week + year, '', 'CS', str(int(round(forecast['value'])))]
            )
    print(pd.DataFrame(output))


def logica_begin():
    this_monday_new = semana
    this_monday_old = (
            datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday())
    )
    # next_tuesday = this_monday_new + datetime.timedelta(days=7 - this_monday_new.weekday())
    next_tuesday = this_monday_new
    print(this_monday_new)
    begin = (
            (next_tuesday.replace(day=1) + datetime.timedelta(days=32)).replace(day=1) -

            datetime.timedelta(days=(next_tuesday.replace(day=1) + datetime.timedelta(days=32)).replace(day=1).weekday())
    )
    print(begin)


if __name__ == '__main__':
        logica_begin()
