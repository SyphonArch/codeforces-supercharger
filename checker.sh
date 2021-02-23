#!/bin/bash
UPPER=${1^^}
if [[ "$1" == *.py ]]; then
    FILENAME=${UPPER::-3}
    EX_NUM=0
    while [ -f ./ex_io/${FILENAME}_in_${EX_NUM}.txt ]; do
        python3 $1 < ./ex_io/${FILENAME}_in_${EX_NUM}.txt > ./output/${FILENAME}_${EX_NUM}.txt
        ((EX_NUM=EX_NUM+1))
    done

else if [[ "$1" == *.cpp ]]; then
    FILENAME=${UPPER::-4}
    g++ $1 -o ${FILENAME}
    EX_NUM=0
    while [ -f ./ex_io/${FILENAME}_in_${EX_NUM}.txt ]; do
        ./${FILENAME} < ./ex_io/${FILENAME}_in_${EX_NUM}.txt > ./output/${FILENAME}_${EX_NUM}.txt
        ((EX_NUM=EX_NUM+1))
    done

else if [[ "$1" == *.c ]]; then
    FILENAME=${UPPER::-2}
    gcc $1 -o ${FILENAME}
    EX_NUM=0
    while [ -f ./ex_io/${FILENAME}_in_${EX_NUM}.txt ]; do
        ./${FILENAME} < ./ex_io/${FILENAME}_in_${EX_NUM}.txt > ./output/${FILENAME}_${EX_NUM}.txt
        ((EX_NUM=EX_NUM+1))
    done
else
    echo "Unsupported file extension!"
    exit 1
fi;fi;fi

EX_NUM=0
while [ -f ./ex_io/${FILENAME}_in_${EX_NUM}.txt ]; do
    echo "-EX ${EX_NUM}----->"
    cat ./output/${FILENAME}_${EX_NUM}.txt
    echo
    ((EX_NUM=EX_NUM+1))
done
echo ""
echo "------ DIFF RESULTS ------"
EX_NUM=0
while [ -f ./ex_io/${FILENAME}_in_${EX_NUM}.txt ]; do
    echo "-EX ${EX_NUM}----->"
    diff <(nl ./ex_io/${FILENAME}_out_${EX_NUM}.txt) <(nl ./output/${FILENAME}_${EX_NUM}.txt)
    echo
    ((EX_NUM=EX_NUM+1))
done
