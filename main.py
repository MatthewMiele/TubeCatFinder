import click
import catsfinder


@click.command()
@click.argument('numofcats', required=True, type=int)
def run(numofcats):
    """ NUMOFCATS: The number of inital lost cats and owners """
    click.echo(numofcats)
    catsfinder.findmycat(numofcats)

if __name__ == '__main__':
    run()
