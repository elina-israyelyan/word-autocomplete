import click

import tree.cli


@click.group()
def cli():
    pass


cli.add_command(tree.cli.commands)
if __name__ == '__main__':
    cli()
