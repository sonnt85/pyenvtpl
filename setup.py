from setuptools import setup

long_description = '''
pyenvtpl
======

_Render jinja2 templates on the command line with shell environment variables_

Installation
------------

    pip install pyenvtpl

How-to
------

Say you have a configuration file called whatever.conf that looks like this

    foo = 123
    bar = "abc"

You can use pyenvtpl to set `foo` and `bar` from the command line by creating a file called whatever.conf.tpl

    foo = {{ FOO }}
    bar = "{{ BAR }}"

If you run

    FOO=123 BAR=abc pyenvtpl < whatever.conf.tpl > whatever.conf

you'll get back the original whatever.conf.

You can also specify default values

    foo = {{ FOO | default(123) }}
    bar = "{{ BAR | default("abc") }}"

Running

    FOO=456 pyenvtpl < whatever.conf.tpl > whatever.conf

will generate

    foo = 456
    bar = "abc"

This is all standard [Jinja2 syntax](http://jinja.pocoo.org/docs/templates/), so you can do things like

    {% if BAZ is defined %}
    foo = 123
    {% else %}
    foo = 456
    {% endif %}
    bar = "abc"

If an environment variable is missing, pyenvtpl will throw an error

    $ echo '{{ FOO }} {{ BAR }}' | FOO=123 pyenvtpl
    Error: 'BAR' is undefined

You can change this behaviour to insert empty strings instead by passing the `--allow-missing` flag.

Instead of reading from stdin and writing to stdout, you can pass the input filename as an optional positional argument,
and set the output filename with the `--output-file` (`-o`) argument.

    pyenvtpl -o whatever.conf  whatever.conf.tpl

As a convenience, if you don't specify an output filename and the input filename ends with `.tpl`, the output filename will be the input filename without the `.tpl` extension, i.e.

    pyenvtpl whatever.conf.tpl
    # is equivalent to
    pyenvtpl -o whatever.conf whatever.conf.tpl

By default, pyenvtpl will **delete** the input template file. You can keep it by passing the `--keep-template` flag.

There's a special `environment(prefix='')` function that you can use as a kind of wildcard variable. If you have `hello.tpl`

    hello = {{ FOO }}
    {% for key, value in environment('MY_') %}{{ key }} = {{ value }}
    {% endfor %}

and compile it using

    FOO=world MY_baz=qux MY_foo=bar pyenvtpl hello.tpl

You end up with

    hello = world
    baz = qux
    foo = bar

What's the point?
-----------------

I use this script quite a lot in Docker images. Usually I'll have the CMD execute some file, like /bin/start_container, that sets up the runtime configuration for the container by inserting environment variables into config files before starting the main process. A redis example could look like this

    #!/bin/bash
    # start_container

    pyenvtpl /etc/redis.conf.tpl

    redis-server

This is the use case I've optimised for, so that's why pyenvtpl by default will delete the original template file.

New functions:
Check file exists()
    {{ exists("/etc") }}
'''  # noqa

setup(
    name='pyenvtpl',
    version='1.0.0',
    py_modules=['pyenvtpl'],
    entry_points={
        'console_scripts': ['pyenvtpl = pyenvtpl:main']
    },
    install_requires=[
        'argparse>=1.0',
        'Jinja2>=2.7',
    ],
    author='thanhson.rf@gmail.com',
    author_email='thanhson.rf@gmail.com',
    description=('Render jinja2 templates on the command line using shell environment variables'),
    license='GPL v3',
    keywords='template environment variables parameter substitution shell jinja2 docker',
    long_description=long_description,
    url='https://github.com/sonnt85/pyenvtpl',
)
