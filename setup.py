from setuptools import setup, find_packages

setup(
    name='pygments-graphql-lexer',
    version='0.1',
    packages=find_packages(),
    entry_points=
    """
    [pygments.lexers]
    graphqllexer = graphqllexer.lexer:GraphqlLexer
    """,
)
