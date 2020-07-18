import asyncio
import time
import PySimpleGUI as sg


async def task1():

    await asyncio.sleep(2.5)
    print('finished task1')


async def task2():

    await asyncio.sleep(2.0)
    print('finished task2')


def blocking_task():

    time.sleep(1.5)
    print('finished blocking task')


async def test_gui():

    while True:  # The Event Loop
        event, values = window.read(timeout=100)
        if event != '__TIMEOUT__':
            print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        await asyncio.sleep(.1)


async def main():

    loop = asyncio.get_event_loop()

    job1 = loop.create_task(task1())
    job2 = loop.create_task(task2())
    job3 = loop.run_in_executor(None, blocking_task)
    job4 = loop.create_task(test_gui())

    await job1
    await job2
    await job3
    await job4


if __name__ == "__main__":

    ct = time.time()
    layout = [[sg.Text('Persistent window')],
              [sg.Input(key='-IN-')],
              [sg.Button('Read'), sg.Exit()]]
    window = sg.Window('Window that stays open', layout)
    asyncio.run(main())
    print(f'Total runtime {time.time() - ct}')