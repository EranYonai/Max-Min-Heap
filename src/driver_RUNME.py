from handlers import UserHandler

if __name__ == "__main__":
    driver = UserHandler()
    while driver.alive:
        driver.show_menu()
        driver.operate_on_heap(driver.get_user_input(prompt="\nEnter your choice: "))
        print("--------")