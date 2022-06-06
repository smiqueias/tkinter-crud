import repository

initial_menu = 99


def show_header():
    number_of_columns = 60
    print("-" * number_of_columns)
    print("{:^60}".format("TAREFAS"))
    print("-" * number_of_columns)
    print("{:^60}".format("tecle 99 volta para o menu inicial, [CTRL+C] sai"))
    print("-" * number_of_columns)
