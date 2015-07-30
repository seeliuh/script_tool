#/bin/sh

#轮流使用nm命令查找目标目录所有.a和.so的符号。在某个目标文件输出前打印目标文件名。
#参数1:目标文件夹
#参数2:要查找的symbol关键字

find_symbol_one_file()
{
	full_name=$1
	dymbol=$2
	fname=`basename $full_name`
	if [[ `echo "$fname"|grep ".a$"` != "" ]] ; then
		echo "---------------------------------$full_name------------------------------------------";
		nm $full_name|grep -i $2
	elif [[ `echo "$fname"|grep ".so$"` != "" ]] ; then
		echo "---------------------------------$full_name------------------------------------------";
		nm -D $full_name|grep -i $2
	fi
}

echo $#
if [[ -d $1 ]] ;then
	dst_path=$1
else
	echo "error:param 1 is not a dir"
	exit;
fi
echo "dst_path=$dst_path"
for filename in `ls $1`
do
	fname=`basename $filename`
	full_name="$dst_path/$fname"
	find_symbol_one_file $full_name $2
done

