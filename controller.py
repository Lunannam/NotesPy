
import operation as o
import ui as ui



def button_click():
    ui.greetings_user()
    while True:
        menu = ui.show_menu()
        choice = ui.get_choice(menu)
        if choice == 1:
            note = ui.add_note()
            o.add_note_csv(note)
        elif choice == 2:
            searchstring = ui.get_action('Введите данные для поиска: ')
            searched_note = o.search_note(searchstring)
            ui.view_data(searched_note)
            while True:
                    menu_s = ui.menu_search()
                    choice = ui.get_choice(menu_s)
                    if choice == 1:
                         ui.edit_user_note(searchstring)
                         note = ui.add_note()
                         o.edit_note(searchstring, note)
                    elif choice == 2:
                         o.delete_note(searchstring) # delete_note
                         ui.delete_user_note(searchstring)
                    else:
                         break
        elif choice == 3:
            result = o.read_csv()
            ui.view_data(result)

        else:
            ui.farewell_user()
            break
