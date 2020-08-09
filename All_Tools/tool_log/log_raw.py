#!/usr/bin/python
#-*-coding: utf8-*-
__all__ =["",\
          "",\
          ]
#####内置库########内置库#####内置库###内置库###内置库###内置库###内置库###
import time,sys,os
import logging
import logging.handlers
import datetime
#####第三方库#####第三方库######第三方库######第三方库#####第三方库#####第三方库####

#####本项目的库，请标注自己名称#####本项目的库，请标注自己名称#####本项目的库，请标注自己名称

class SetProjLog(object):
    """
    实例化一个SetProjLog（name）对象obj， 填入项目名称name， 特别注意一个项目只需实例化一个obj
    在需要打印的模块导入obj，利用obj.error(msg), 和obj.info(msg)添加信息msg
    """
    # 实列化一个logger
    def __init__(self, project_name:str):
        self.logger = logging.getLogger(project_name + '_Logger')
        self.project_name = project_name
        self.logger.setLevel(logging.CRITICAL)

        # 实例化多个handler
        ##实例化一个包含所有lever的handler
        self.all_level_handler_path = os.path.join(os.path.dirname(__file__), "log_files\\"+ self.project_name)
        self._make_log_dir(self.all_level_handler_path)
        self.all_level_handler = logging.handlers.TimedRotatingFileHandler(self.all_level_handler_path + r"\all.log", \
                                                                  when='midnight', interval=1, backupCount=365,\
                                                                  atTime=datetime.time(0, 0, 0, 0), encoding='utf-8')
        self.all_level_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        ##实例化一个包含ERROR信息的handler
        self.error_handler_path = os.path.join(os.path.dirname(__file__), "log_files\\"+ self.project_name)
        self._make_log_dir(self.error_handler_path)
        self.error_handler = logging.FileHandler(self.error_handler_path + r"\eroor.log")
        self.error_handler.setLevel(logging.ERROR)
        self.error_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
        ##实例化一个包含INFO信息的handler
        self.info_handler_path = os.path.join(os.path.dirname(__file__), "log_files\\"+ self.project_name)
        self._make_log_dir(self.info_handler_path)
        self.info_handler = logging.FileHandler(self.info_handler_path + r"\info.log")
        self.info_handler.setLevel(logging.INFO)
        self.info_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
        #向logger中添加handler
        self.logger.addHandler(self.all_level_handler)
        self.logger.addHandler(self.error_handler)
        self.logger.addHandler(self.info_handler)
    def error(self,error_message):
        return self.logger.error(self,'error_message')

    def info(self, info_message):
        return self.logger.info(self,'info_message')
    def _make_log_dir(self,path):
        print(path)
        if os.path.exists(path):
            print(1)
            return
        else:
            print(0)
            os.mkdir(path)

if __name__ == "__main__":
    print(SetProjLog.__doc__)
    project_0_log = SetProjLog('project_2')
    project_0_log.info('info_message')
    project_0_log.error('error_message')


    pass