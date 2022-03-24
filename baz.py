from foo_package.bar import add_one
from .bar import add_one as add_one_rel


def baz_fun():
    print("baz_fun")
    print("testing add_one via absolute/normal import...")
    add_one(1)
    print("testing add_one via absolute import complete.")

    print("testing add_one via relative import...")
    add_one_rel(1)
    print("testing add_one via relative import complete.")
