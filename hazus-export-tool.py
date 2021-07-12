from src.manage_new import Manage

if __name__=='__main__':
    manage = Manage()
    #app_path = 'Python_env/gui_program.py'
    app_path = 'gui_program.py'
    update_path = 'src/update.py'
    try:
        manage.startApp(app_path, update_path)
    except Exception as e:
        print(e)

