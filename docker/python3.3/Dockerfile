FROM    python:3.3

RUN     pip install nose
RUN     mkdir /pyenvtpl-dev
WORKDIR /pyenvtpl-dev
RUN     git clone https://github.com/andreasjansson/pyenvtpl.git
WORKDIR /pyenvtpl-dev/pyenvtpl
RUN     python setup.py develop
RUN     pip install -r tests/requirements.txt

CMD     ["nosetests", "tests"]
