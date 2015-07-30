# script_tool
汇总工作和业余常用的脚本小工具

##freqScale_l4t.sh
TK1板子CPU和GPU超频脚本
##find_symbol_by_path.sh
在linux编译链接时，经常遇到找不到符号的情况，利用此脚本可快速定位符号所在的.a和.so的位置，批量查找某目录下的.a和.so包含的符号信息。例如：
	
	find_symbol_by_path.sh /usr/lib/vion-base-sdk scSleep
	列出所有包含scSleep符号的库
	
##convert_linda_code_encode.py
公司中经常会有一些比较庞大，维护人员较多的工程代码。由于IDE不同、或历史原因，很多源码的编码格式不同，多是UTF-8和GBK参杂在一起。我们需要一个工具能自动识别源码编码格式，并转换成统一格式。

此脚本的作用是，遍历某目录下的所有源码，自动识别源码格式功能，自动转换成用户指定的格式。例如:
	
	convert_linda_code_encode.py ./code gbk
	将code目录下的所有源码转换成gbk编码
	
	convert_linda_code_encode.py ./code check
	识别code目录下所有源码的编码格式

##change_workspace.sh
同一linux系统中，需要编译多种不同平台的程序(x86,arm,x86_64)，不同的目标平台有不同版本的库路径，环境变量改来改去很不方便。此脚本的作用是按照预设值修改LD_LIBRARY_PATH等环境变量并生效	