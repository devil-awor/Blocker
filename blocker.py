from platform import system
from time import sleep
from rich.console import Console
from rich import print as rprint
from rich.progress import Progress
from rich.table import Table
from rich.padding import Padding

bloks = []
resident = "127.0.0.1"
console = Console()

def get_platform_path():
    plat = system()
    if plat == "Windows":
        return r"C:\Windows\System32\drivers\etc\hosts"
    elif plat == "Linux" or plat == "Mac":
        return r"/etc/hosts"

def unblock_site():
    try:
        ndex = 0
        site = input("Введите ссылку: ")
        host = get_platform_path()
        with open(host, "r") as file:
            content = file.readlines()
            ndex = content.index(f"{resident} {site}\n")
            line_to_delete = ndex+1

        progress = Progress()
        progress.start()
        try:
            task2 = progress.add_task("[green]В процессе...", total=1000)
            while not progress.finished:
                progress.update(task2, advance=1.7)
                sleep(0.002)
        finally:
            progress.stop()

        with open(host, 'r', ) as f:
            lines = f.readlines()
        new_lines = []
        for i, line in enumerate(lines):
            if i != line_to_delete - 1:
                new_lines.append(line)

        with open(host, 'w') as f:
            f.writelines(new_lines)
    except ValueError as er:
        rprint(f"[bold red]Error: {er}[bold red]")

def block_site():
    site = input("Введите ссылку: ")
    bloks.append(site)
    host = get_platform_path()
    progress = Progress()
    progress.start()
    try:
        task2 = progress.add_task("[green]В процессе...", total=1000)
        while not progress.finished:
            progress.update(task2, advance=1.6)
            sleep(0.002)
    finally:
        progress.stop()
    with open(host, "r+") as file:
        content = file.read()
        for site in bloks:
            if site in content:
                pass
            else:
                file.write(f"{resident} {site}\n")


def get_blocks():
    num = 0
    host = get_platform_path()
    table = Table(title="Заблокированные сайты")
    table.add_column("номер", justify="center", style="green")
    table.add_column("сайт", justify="left", style="red")
    
    with open(host, "r") as file:
        content = file.readlines()
    for i in range(len(content)):
        con = content[i].split(" ")
        if "#" in con[0] or con[0] == '\n':
            pass
        else:
            table.add_row(f"{num+1}", con[1])
    console.print(table)


def main():
    name_of = Padding("[bold red]'BLOCKER' By Devil Awor[bold red]", (0,7))
    # name_1f = Padding("[bold red]ЭТА ВЕРСИЯ ПРЕДНАЗНАЧЕНА ТОЛЬКО ДЛЯ WINDOWS[bold red]", (1,5))
    rprint(name_of)
    # console.rule(style="red",characters="-")
    # rprint(name_1f)
    console.rule(style="red",characters="-")
    while True:
        console.print("Выберите действие: \n 1 - блокировка сайта\n 2 - разблокировка сайта\n 3 - показать заблокированные сайты \n 4 - выход", style="green")
        ans = input("ваш выбор: ")
        if ans == "1":
            block_site()
        elif ans == "2":
            unblock_site()
        elif ans == "3":
            get_blocks()
        elif ans == "4":
            break
        else:
            rprint("[bold red]Error: недопустимый вариант ответа[bold red]")
        
if __name__ == "__main__":
    main()