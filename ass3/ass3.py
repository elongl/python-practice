import os
from datetime import datetime


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def line_to_event(event_line):
    event = event_line.split('\t')
    return {'name': event[0], 'location': event[1], 'datetime': datetime.strptime(event[2], '%d.%m.%y %H:%M')}


def event_to_line(e):
    return f'{e["name"]}\t{e["location"]}\t{e["datetime"].strftime("%d.%m.%y %H:%M")}\n'


with open('events') as events_file:
    events_lines = events_file.read().splitlines()
events = [line_to_event(el) for el in events_lines]
events = [e for e in events if e['datetime'] > datetime.now()]

while True:
    clear()
    print("Please choose your action.\n1. See today's events.\n2. Add an event.\n-1. Exit")
    try:
        action_index = int(input())
        if action_index == -1:
            events_lines = map(event_to_line, events)
            with open('events', 'w') as events_file:
                events_file.writelines(events_lines)
            print('Thank you for using our service. Bye bye!')
            break
        elif action_index == 1:
            todays_events = [
                e for e in events if e['datetime'].date() == datetime.now().date()]
            if len(todays_events) == 0:
                print('You have no events.')
            else:
                print("Today's Events:")
                print('Event\tLocation\tDate & Time')
                for e in todays_events:
                    print(
                        f'{e["name"]}\t{e["location"]}\t{e["datetime"].strftime("%d.%m.%y %H:%M")}')
            print('Press enter to return to the main menu.')
            input()
        elif action_index == 2:
            print('Please enter the name of the event.')
            event_name = input()
            print('Please enter the location of the event.')
            event_location = input()
            while True:
                print(
                    f'Please enter the date of the event ({datetime.now().date().strftime("%d.%m.%y")}).')
                event_date = datetime.strptime(input(), '%d.%m.%y').date()
                if event_date < datetime.now().date():
                    print('You cannot create an event in the past.')
                    continue
                else:
                    break
            print(
                f'Please enter the time of the event ({datetime.now().time().strftime("%H:%M")}).')
            event_time = datetime.strptime(input(), '%H:%M').time()
            events.append({'name': event_name, 'location': event_location,
                           'datetime': datetime.combine(event_date, event_time)})
            print('Your event has been added.')
            print('Press enter to return to the main menu.')
            input()

    except ValueError:
        print("Please make sure you're entering the correct values.")
        print('Press enter to return to the main menu.')
        input()
        continue
