#/bin/bash
#@file change_workspace.sh
#@brief 用法：. /usr/local/bin/change_workspace.sh 平台名（tk1或 server）例如切换tk1
#. /usr/local/bin/change_workspace.sh tk1  注意：命令最前面的 "."是要带的。
#可以根据自己的实际情况，修改此脚本中的环境变量
#@author liuh
#@version 
#@date 2014-06-19


function reset_var()
{
	export C_INCLUDE_PATH=
	export CPLUS_INCLUDE_PATH=
	export LIBRARY_PATH=
	export LD_LIBRARY_PATH=
}


if [[ $1 = "tk1" ]] ; then
	echo $1
	reset_var
	export C_INCLUDE_PATH=/arm-tk1/include/vion-base-sdk:/arm-tk1/include:
	export CPLUS_INCLUDE_PATH=/arm-tk1/include/vion-base-sdk:/arm-tk1/include:
	export LIBRARY_PATH=/arm-tk1/lib/vion-base-sdk:/arm-tk1/lib:/arm-tk1/lib/arm-linux-gnueabihf:/arm-tk1/lib/boost
	export LD_LIBRARY_PATH=/arm-tk1/lib/vion-base-sdk:/arm-tk1/lib:/arm-tk1/lib/arm-linux-gnueabihf:/arm-tk1/lib/boost:
	echo $C_INCLUDE_PATH
	echo $CPLUS_INCLUDE_PATH
	echo $LIBRARY_PATH
	echo $LD_LIBRARY_PATH

elif [[ $1 = "server" ]] ; then
	echo $1
	reset_var
	export C_INCLUDE_PATH=/usr/include/vion-base-sdk:
	export CPLUS_INCLUDE_PATH=/usr/include/vion-base-sdk:/usr/include/postgresql/:/usr/include/postgresql/catalog
	export LIBRARY_PATH=/usr/lib/vion-base-sdk:
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/vion-base-sdk:/usr/local/lib:.:/media/psf/Home/code/ScFrameWork/bin/linux:/opt/thirdplatsdk:
	echo $C_INCLUDE_PATH
	echo $CPLUS_INCLUDE_PATH
	echo $LIBRARY_PATH
	echo $LD_LIBRARY_PATH
else
	echo "please input operation: 'server' or 'tk1' "
fi
