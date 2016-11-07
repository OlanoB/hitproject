while true
do
	echo "Enter choice"
	echo "(Press 'q' to exit)"
	echo "1 date		2 who"
	echo "3 ls			4 pwd"
	read choice
	case $choice in
		1) date;;
		2) who;;
		3) ls;;
		4) pwd;;
		q) break;;
		*) echo "That was not one of the choices";;
	esac
done