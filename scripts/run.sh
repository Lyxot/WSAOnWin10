#!/bin/bash
ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd ../ && pwd )"
SCRIPTS_DIR="$ROOT_DIR/scripts"
MagiskOnWSALocal_DIR="$SCRIPTS_DIR/MagiskOnWSALocal"


cd $SCRIPTS_DIR
if [ -f "$MagiskOnWSALocal_DIR/.git/config" ]; then
    cd MagiskOnWSALocal
    git pull
else
    if [ -d "$MagiskOnWSALocal_DIR" ];then
        rm -rf MagiskOnWSALocal
    fi
    git clone https://ghproxy.com/https://github.com/LSPosed/MagiskOnWSALocal.git
fi
cd $ROOT_DIR
cp -r installer $MagiskOnWSALocal_DIR
cd $MagiskOnWSALocal_DIR


./scripts/build.sh $*

