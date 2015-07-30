#!/usr/bin/python
#coding:utf-8
__author__ = 'liuhang'
import sys
import os
import shutil
import codecs
from os import path,access,R_OK

import chardet

def print_help():
    print "用法说明："
    print "convert_linda_code_encode.py PATH OPERATOR_TYPE"
    print "PATH:路径，自动递归"
    print "OPERATOR_TYPE: 要做的操作类型："
    print "    utf8 - 脚本自动检测源代码编码类型，将gbk编码的文件转换成utf8"
    print "    gbk - 自动检测源代码编码类型，将utf8编码的文件转换成gbk"
    print "    check - 输出所有源码编码类型"
    print "支持的文件后缀名:.cpp .c .h .hpp"
    print "在转换文件编码前，会在文件同级目录进行备份，此脚本不会访问备份的文件夹进行转换"

def read_file_by_encode_type(filefullpath, encodetype):
    with codecs.open(filefullpath, "r", encodetype) as dst_file:
        buf = dst_file.read()
        #dst_file.close()
        return buf

def write_file_with_encode_type(filefullpath, content_buf, encodetype):
    with codecs.open(filefullpath, "w", encodetype) as dst_file:
        dst_file.write(content_buf)
        # dst_file.close()

def dect_one_file_base(file_full_name):
    f_file = open(file_full_name)
    tmp_buf = f_file.read();
    return chardet.detect(tmp_buf)['encoding']

def dect_one_file_pro(file_full_name):
    f_file = open(file_full_name)
    tmp_buf = f_file.read();
    return chardet.detect(tmp_buf)

def convert_by_line(src, dst, src_type, dst_type):
    f_src = codecs.open(src, "r", src_type)
    f_dst = codecs.open(dst+".tmp", "w", dst_type)
    while 1:
        tmp_buf = f_src.readline()
        if not tmp_buf:
            break
        else:
            f_dst.writelines(tmp_buf)
    f_src.close()
    f_dst.close()
    shutil.move(dst+".tmp", dst)

def convert(src, dst, src_type, dst_type):
        tmp_buf = read_file_by_encode_type(src, src_type)
        write_file_with_encode_type(dst, tmp_buf, dst_type)


def func_obj_check_file_encode_type(file_full_name):
    #print file_full_name + " encode:" + dect_one_file_pro(file_full_name)
    print file_full_name + "  encode info:"
    print dect_one_file_pro(file_full_name)

def func_obj_utf8_to_gbk(file_full_name):
    file_enc_type = dect_one_file_base(file_full_name)
    if file_enc_type == "utf-8":
        print "filename: " + file_full_name + ", encode_type: " + file_enc_type + " begin utf-8 convert to gb18030"
        utf8backup = os.path.split(file_full_name)[0] + "/" + file_enc_type + "_enc_backup"
        if not path.exists(utf8backup):
            os.mkdir(utf8backup);
        filename = os.path.join(utf8backup, os.path.split(file_full_name)[1])
        shutil.copy(file_full_name, filename)
        convert_by_line(file_full_name, file_full_name, file_enc_type, "gb18030")


def func_obj_gbk_to_utf8(file_full_name):
    file_enc_type = dect_one_file_base(file_full_name)
    if file_enc_type.lower() == "gbk" or file_enc_type.lower() == "gb2312" or file_enc_type.lower() == "gb18030":
        print "filename: " + file_full_name + ", encode_type: " + file_enc_type + " begin gbk convert to utf-8"
        gbk_backup = os.path.split(file_full_name)[0] + "/" + file_enc_type + "_enc_backup"
        if not path.exists(gbk_backup):
            os.mkdir(gbk_backup);
        filename = os.path.join(gbk_backup, os.path.split(file_full_name)[1])
        shutil.copy(file_full_name, filename)
        #convert(file_full_name, file_full_name, file_enc_type, "utf-8")
        convert_by_line(file_full_name, file_full_name, file_enc_type, "utf-8")


def iterate_dir(dir_root, func_process_file):
    if not os.path.exists(dir_root):
        print "输入的文件夹:" + dir_root + "不存在"
    for parent_dir, dirnames, filenames in os.walk(dir_root):
        # for dir in dirnames:
        #     print "parent:" + parent_dir
            # print "dir:" + dir
        for file in filenames:
            if not "_enc_backup" in parent_dir:
                spltxt = os.path.splitext(file)[1]
                if spltxt == ".cpp" or spltxt == ".h" or spltxt == ".c" or spltxt == ".hpp":
                    file_full_name = os.path.join(parent_dir, file)
                    try:
                        func_process_file(file_full_name)
                    except Exception, e:
                        print "error! process " + file_full_name + "failed!"
                        print e;





def main():
    argv_len = len(sys.argv)
    if argv_len != 3:
        print_help()
        exit();

    #print dect_one_file_base("/Users/liuhang/convert_encode_test/linDASlave/linDACamera.cpp")

    if sys.argv[2] == "check":
        iterate_dir(sys.argv[1], func_obj_check_file_encode_type)
    elif sys.argv[2] == "utf8":
        iterate_dir(sys.argv[1], func_obj_gbk_to_utf8)
    elif sys.argv[2] == "gbk":
        iterate_dir(sys.argv[1], func_obj_utf8_to_gbk)
    else:
        print_help()

main()
