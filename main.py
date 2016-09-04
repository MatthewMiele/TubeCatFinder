import click
import catsfinder


@click.command()
@click.argument('numofcats', required=True, type=int)
@click.option('--max_steps', default=100000, type=int, help='Maximum steps a cat and owner can take. Default 100,000')
def run(numofcats, max_steps):
    """ NUMOFCATS: The number of inital lost cats and owners """
    catsfinder.cat_finder(numofcats, max_steps)

if __name__ == '__main__':
    run()
