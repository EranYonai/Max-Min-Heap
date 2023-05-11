from handlers import UserHandler

if __name__ == "__main__":
    driver = UserHandler()
    while driver.alive:
        driver.show_menu()
        driver.operate_on_heap(driver.get_user_input(prompt="\nEnter your choice: "))
        print("--------")
# Failed to delete an element [1298, -938, 5, -1699], attempted to delete 2
# OG input: [-1699, -1976, -41, 1298, -938, 860, 5, -1699]