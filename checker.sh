#!/bin/bash
UPPER=${1^^}
if [[ "$1" == *.py ]]
then
    FILENAME=${UPPER::-3}
    python3 $1 < ./ex_io/${FILENAME}_in.txt > ./output/${FILENAME}.txt
else if [[ "$1" == *.cpp ]]
then
    FILENAME=${UPPER::-4}
    g++ $1 -o ${FILENAME}
    ./${FILENAME} < ./ex_io/${FILENAME}_in.txt > ./output/${FILENAME}.txt
else if [[ "$1" == *.c ]]
then
    FILENAME=${UPPER::-2}
    gcc $1 -o ${FILENAME}
    ./${FILENAME} < ./ex_io/${FILENAME}_in.txt > ./output/${FILENAME}.txt
else
    echo "Unsupported file extension!"
fi
fi
fi

cat ./output/${FILENAME}.txt
echo ""
echo "------DIFF RESULTS------"
diff ./ex_io/${FILENAME}_out.txt ./output/${FILENAME}.txt
