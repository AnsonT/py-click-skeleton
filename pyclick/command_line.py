import click
@click.group()
def main():
    """ Main CLI """
    click.echo("main")

@main.command()
def test():
    """ Test Command """
    click.echo("test")

@main.command()
def test2():
    """ Test2 Command """
    click.echo("test2")

def test3():
    print('testing')