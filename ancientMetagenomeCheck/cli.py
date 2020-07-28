import click
from ancientMetagenomeCheck import __version__
from ancientMetagenomeCheck.main import run_tests
from pathlib import Path


@click.command()
@click.version_option(__version__)
@click.argument('standards', type=click.Path(exists=True))
@click.argument('dataset', type=click.Path(exists=True))
def cli(no_args_is_help=True, **kwargs):
    """\b
    AncientMetagenomeCheck: Performs validity check of ancientMetagenomeDir datasets
    Author: Maxime Borry
    Contact: <borry[at]shh.mpg.de>
    Homepage & Documentation: github.com/maxibor/AncientMetagenomeCheck
    \b
    STANDARDS: path to standards defining tsv file
    DATASET: path to tsv file of dataset to check
    """
    run_tests(**kwargs)


if __name__ == "__main__":
    cli()