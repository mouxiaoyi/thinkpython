#!/bin/sh -e

#############################
# the install of requirements
# bison yacc flax autoconf
#############################

Bison_dir='bison-3.0.4'
Yacc_dir='byacc-20160606'
Flex_dir='flex-2.6.0'
Autoconf_dir='autoconf-2.69'

for dir in $Bison_dir $Yacc_dir $Flex_dir $Autoconf_dir;do
    cd $dir
    ./configure &&
    make &&
    make install
    echo $dir' is installed...'
    cd -
done


###############
# ltp's install
###############
Ltp_dir='ltp*'

cd $Ltp_dir
make autotools > /dev/null &&
./configure > /dev/null &&
make > /dev/null &&
make install > /dev/null
echo 'ltp is installed...'
cd -

###################
# run the ltp test
###################
PWD=`pwd`
RESULT_DIR=$PWD'/result'

/opt/ltp/runltp -c 2 -i 2 -m 2,4,10240,1 -D 2,10,10240,1 -p -q  -l $RESULT_DIR/result-log -o $RESULT_DIR/result-output -C $RESULT_DIR/result-failed -T $RESULT_DIR/result-failed.tconf -d $RESULT_DIR -t 10h
