#/bin/bash
set -u
source shared.sh

for version in $VERSIONS; do
    tag=pyenvtpl-dev:$version
    echo "Testing Python $version"
    docker run -it -v $PWD/..:/pyenvtpl-dev/pyenvtpl $tag
    echo
done
