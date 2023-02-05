import dearpygui.dearpygui as dpg
import csv
import time


def add_info() -> None:
    if dpg.get_value("group") == "" or dpg.get_value("grade") == "":
        dpg.set_value("logs", "The fields must be filled!")
    elif dpg.get_value("group") not in ["AM-19", "AM-20", "AM-21", "AM-22"]:
        dpg.set_value("logs", "Unknown group!")
    elif not dpg.get_value("grade").isdigit() or not (0 <= int(dpg.get_value("grade")) <= 100):
        dpg.set_value("logs", "The grade must be between 0 and 100!")

    else:
        with open('students.csv', mode='a', encoding='utf-8') as file:
            file_writer = csv.writer(file, delimiter=',', lineterminator='\r')
            file_writer.writerow([dpg.get_value("group"), dpg.get_value("grade")])
            dpg.set_value("logs", "Added!")

    time.sleep(2)
    dpg.set_value("logs", "")


def get_info(group: str) -> list:
    with open('students.csv', mode='r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=',')
        group_info = []
        for row in file_reader:
            if row[0] == group:
                grade = int(row[1])
                if 0 <= grade <= 52:
                    grade = 2
                elif 53 <= grade <= 79:
                    grade = 3
                elif 80 <= grade <= 92:
                    grade = 4
                elif 93 <= grade <= 100:
                    grade = 5
                group_info.append(grade)

        return [group_info.count(grade_i) for grade_i in [2, 3, 4, 5]]


def show_info(sender=None, app_data=None, user_data: str = "AM-19") -> None:
    try:
        dpg.set_value("logs", "")
        data = get_info(user_data)
        dpg.set_value("info", [data, [1, 2, 3, 4]])
        if data == [0, 0, 0, 0]:
            dpg.set_value("logs", "The group data is not found!")
        dpg.set_item_label("group_info", user_data)
    except:
        dpg.set_value("logs", "Something's wrong!")
        time.sleep(2)
        dpg.set_value("logs", "")


dpg.create_context()

with dpg.window(label="Students performance", height=530, width=640,
                no_resize=True, no_close=True, no_collapse=True):

    dpg.add_text("Enter student's info")
    with dpg.group(horizontal=True):
        dpg.add_input_text(label="Group", tag="group", width=260)
        dpg.add_input_text(label="Grade", tag="grade", width=260)

    with dpg.group(horizontal=True):
        dpg.add_button(label="Add into the database", tag="add", callback=add_info, width=190)
        dpg.add_text(tag="logs")

    dpg.add_text()
    with dpg.group(horizontal=True, horizontal_spacing=5):
        dpg.add_button(label="AM-19", callback=show_info, user_data="AM-19", width=150)
        dpg.add_button(label="AM-20", callback=show_info, user_data="AM-20", width=150)
        dpg.add_button(label="AM-21", callback=show_info, user_data="AM-21", width=150)
        dpg.add_button(label="AM-22", callback=show_info, user_data="AM-22", width=150)

    # Initial pie chart (AM-19 group)
    try:
        with dpg.plot(no_title=True, height=380, width=615):
            dpg.add_plot_legend()

            dpg.add_plot_axis(dpg.mvXAxis, label="AM-19", tag="group_info",
                              no_gridlines=True, no_tick_marks=True, no_tick_labels=True)
            dpg.set_axis_limits(dpg.last_item(), 0, 1)

            with dpg.plot_axis(dpg.mvYAxis, no_gridlines=True,
                               no_tick_marks=True, no_tick_labels=True):
                dpg.set_axis_limits(dpg.last_item(), 0, 1)
                dpg.add_pie_series(0.5, 0.5, 0.4, get_info("AM-19"), ['0-52', '53-79', '80-92', '93-100'],
                                   normalize=True, tag="info")
    except:
        dpg.set_value("logs", "Something's wrong!")
        time.sleep(2)
        dpg.set_value("logs", "")


dpg.create_viewport(title='Drawing Plot', height=565, width=645, resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
