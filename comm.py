while true
do 
	echo "Please choose your day"
	echo "1 Monday"
	echo "2 Tuesday"
	echo "3 Wednesday"
	echo "4 Thursday"
	echo "5 Friday"
	echo "6 Saturday"
	echo "7 Sunday"
	echo "(Press 'q' to exit)"
	read choice
	case $choice in
		1) Monday;;
		2) Tuesday;;
		3) Wednesday;;
		4) Thursday;;
		5) Friday;;
		6) Saturday;;
		7) Sunday;;
		q) break;;
		*) echo "That was not one of the choices";;
	esac
done
		