#!/bin/bash

readonly PICHA_VERSION=${1:-1}

[[ ! -d picha ]] && {

  curl \
    --location \
    --remote-name \
    --progress \
    https://github.com/realpython/Picha/archive/v${PICHA_VERSION}.tar.gz

  tar zxf v${PICHA_VERSION}.tar.gz && rm -vf v${PICHA_VERSION}.tar.gz
  mv Picha-${PICHA_VERSION} picha

  docker run -it --rm -v $(pwd):/usr/src/app picha python picha/manage.py migrate

}
