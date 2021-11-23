import click
from neural_search.core.index import index_docs

def query():
    pass

@click.command()
@click.option('--task', '-t',
              type=click.Choice(['index', 'query'], case_sensitive=False))
@click.option('--path', '-p',
              type=click.Path(exists=True, dir_okay=False, file_okay=True),
              default='./data/books.csv')
@click.option('--num_docs', '-n',
              type=click.INT, default=None)
@click.option('--index_field', '-i',
              type=click.STRING, default='Name')
@click.option('--index_flow_path', '-f',
              type=click.Path(exists=True, dir_okay=False, file_okay=True),
              default='./flows/index.yml')
@click.option('--num_docs', '-n', default=1000)
def main(task, num_docs, path, index_field, index_flow_path):
    """
    Main function for running the server.
    """
    if task == 'index':
        index_docs(
            path=path,
            num_docs=num_docs,
            index_field=index_field,
            index_flow_path=index_flow_path
        )
    elif task == 'query':
        query()
    else:
        raise NotImplementedError(
            f'Unknown task: {task}.')


if __name__ == "__main__":
    main()