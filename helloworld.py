import click
from datetime import datetime


@click.group()
def main():
    pass


@click.command()
def test():
    start_time = datetime.now()
  
    print("Hello World")
  
  
    end_time = datetime.now()
 

    diff_time = end_time - start_time
    print(str(round(diff_time.total_seconds() * 1000)) + "ms")


main.add_command(test)

if __name__ == "__main__":
    main()
