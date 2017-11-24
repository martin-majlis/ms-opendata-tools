#!/bin/bash

DATA_DIR=data/

SUFFIX1=_sensor.csv
SUFFIX2=_json_v2.csv

KLICPEROVA="(001EC918|001EE27E|001EE7CA|001EE860|001EFCBB|001EFE2B|001F1D16|001F3844|001F384F|001F396D|001FG94B)"
KRATOCHVILOVA="(001F56DE|001F56D7|001EE17B|001EE750|001F856E|001F712A|001F558A|001EDCA9|001EE4E6|001EC90C)"
OPAVSKA="(001F5607|001F7756|001F5686|001EFD5D|001EF8A4|001F6CED|001EFC94|001F04F9|001F3A88|001EF670|001EFC16)"
RADON="(001FG94B|001EFC16)"
ANEMOMETR="(001EE27E|001F856E|001EF8A4)"
VENKOVNI_HLUK="(001F1D16|001F712A|001F6CED)"

function process() {
	suffix=$1;
	fName=$2;
	find ${DATA_DIR}/ -name '*'"${suffix}" | egrep "${3}" | xargs ./merge.py ${fName}${suffix}
}

suffix=$1
if [ x${suffix} != x${SUFFIX1} -a x${suffix} != x${SUFFIX2} ]; then
	echo "Musi se specifikovat suffix. Bud '${SUFFIX1}' nebo '${SUFFIX2}'";
	exit 1
fi;

case $2 in
	klicperova)
		process $1 $2 ${KLICPEROVA};
		;;
	kratochvilova)
		process $1 $2 ${KRATOCHVILOVA};
		;;
	opavska)
		process $1 $2 ${OPAVSKA};
		;;
	radon)
		process $1 $2 ${RADON};
		;;
	anemometr)
		process $1 $2 ${ANEMOMETR};
		;;
	venkovni-hluk)
		process $1 $2 ${VENKOVNI_HLUK};
		;;
	*)
		echo "Neznamy nazev datasetu";
		echo "Koukni do zdrojaku, aby ses je dozvedel. Napriklad ./merge-files.sh _sensor.csv klicperova";
		exit 1;
esac;


