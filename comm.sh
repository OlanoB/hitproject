#Guru B scripting tutorial
while true
do 
	echo "Please choose any number to see the day attached"
	echo "1"
	echo "2"
	echo "3"
	echo "4"
	echo "5"
	echo "6"
	echo "7"
	echo "(Press 'q' to exit)"
	read choice
	case $choice in
		1) echo "Today is $1 Monday";;
		2) echo "Today is $2 Tuesday";;
		3) echo "Today is $3 Wednesday";;
		4) echo "Today is $4 Thursday";;
		5) echo "Today is $5 Friday";;
		6) echo "Today is $6 Saturday";;
		7) echo "Today is $7 Sunday";;
		q) break;;
		*) echo "That was not one of the choices";;
	esac
done
		