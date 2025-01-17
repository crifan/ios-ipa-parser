#coding=utf-8
'''
Created on 2015年5月18日

@author: hzwangzhiwei
'''
import json
import os
import re
import tempfile
import zipfile

from biplist import readPlist
# from .biplist import readPlist

class IpaParse(object):
    '''
    DEMO
    parse = IpaParse(filename)
    print parse.app_name() #app 名称
    print parse.bundle_identifier() #package
    print parse.version()
    print parse.target_os_version() #target version
    print parse.minimum_os_version() #min version
    print parse.icon_file_name() # icon name
    print parse.icon_file_path() #path
    
    print parse.mv_icon_to('test.png') #ico复制到指定位置，图片被加密暂时无法处理
    '''
    ipa_file_path = None
    ipa_base_path = None
    
    plist_temp_file = None
    plist_info_list = None
    
    def __init__(self, ipa_file_path):
        '''
        Constructor
        '''
        self.ipa_file_path = ipa_file_path
        
    def saveBinDataToFile(self, binaryData, fileToSave):
        """save binary data into file"""
        saveOK = False
        try:
            # open a file, if not exist, create it
            savedBinFile = open(fileToSave, "wb")
            #print "savedBinFile=",savedBinFile
            savedBinFile.write(binaryData)
            savedBinFile.close()
            saveOK = True
        except :
            saveOK = False
        return saveOK

    def _get_plist_temp_file(self):
        self.plist_temp_file = ''
        
        zfile = zipfile.ZipFile(self.ipa_file_path)
        zip_name_list = zfile.namelist()
        for name in zip_name_list:
            if ".app/Info.plist" in name:
                # print("name=%s" % name)

                fileContent = zfile.read(name)
                # print("type(fileContent)=%s" % type(fileContent))

                # tup = tempfile.mkstemp(suffix = '.plist')
                # fd = os.fdopen(tup[0], "w")
                tmpFdNum, tmpFilename = tempfile.mkstemp(suffix = '.plist')
                # print("tmpFdNum=%s, tmpFilename=%s" % (tmpFdNum, tmpFilename))
                # fd = os.fdopen(tmpFdNum, "w")
                # fd.write(fileContent)
                # fd.close()

                self.saveBinDataToFile(fileContent, tmpFilename)

                # self.plist_temp_file = tup[1]
                self.plist_temp_file = tmpFilename
        zfile.close()
        
        return self.plist_temp_file
    
    def _parse_plist(self):
        try:
            if self.plist_temp_file == None:
                self._get_plist_temp_file()
                
            if self.plist_temp_file == '':
                self.plist_info_list = {}
                return False
            
            self.plist_info_list = readPlist(self.plist_temp_file)
            os.remove(self.plist_temp_file)
            return self.plist_info_list
        except Exception as e:
            print("Not a plist: %s" % e)
            self.plist_info_list = {}
            return False
    
    def _check(self):
        if self.plist_info_list == None:
            self._parse_plist()
     
    def all_info(self):
        self._check()
        return self.plist_info_list
    
    def app_name(self):
        self._check()
        if 'CFBundleDisplayName' in self.plist_info_list:
            return self.plist_info_list['CFBundleDisplayName']
        elif 'CFBundleName' in self.plist_info_list:
            return self.plist_info_list['CFBundleName']
        return None
    
    def bundle_identifier(self):
        self._check()
        if 'CFBundleIdentifier' in self.plist_info_list:
            return self.plist_info_list['CFBundleIdentifier']
        return ''
    
    def target_os_version(self):
        self._check()
        if 'DTPlatformVersion' in self.plist_info_list:
            return re.findall(r'[\d\.]*', self.plist_info_list['DTPlatformVersion'])[0]
        return ''
    
    def minimum_os_version(self):
        self._check()
        if 'MinimumOSVersion' in self.plist_info_list:
            return re.findall(r'[\d\.]*', self.plist_info_list['MinimumOSVersion'])[0]
        return ''
        
    def version(self):
        self._check()
        if 'CFBundleVersion' in self.plist_info_list:
            return self.plist_info_list['CFBundleVersion']
        return ''
    
    def icon_file_name(self):
        if 'CFBundleIcons' in self.plist_info_list and \
            'CFBundlePrimaryIcon' in self.plist_info_list["CFBundleIcons"] and \
            'CFBundleIconFiles' in self.plist_info_list["CFBundleIcons"]["CFBundlePrimaryIcon"]:
            icons = self.plist_info_list["CFBundleIcons"]["CFBundlePrimaryIcon"]['CFBundleIconFiles']
            if icons != None and len(icons) > 0:
                return icons[len(icons) - 1]
        elif 'CFBundleIcons~ipad' in self.plist_info_list and \
            'CFBundlePrimaryIcon' in self.plist_info_list["CFBundleIcons~ipad"] and \
            'CFBundleIconFiles' in self.plist_info_list["CFBundleIcons~ipad"]["CFBundlePrimaryIcon"]:
            icons = self.plist_info_list["CFBundleIcons~ipad"]["CFBundlePrimaryIcon"]['CFBundleIconFiles']
            if icons != None and len(icons) > 0:
                return icons[len(icons) - 1]
        else:
            return False
    
    def icon_file_path(self):
        icon_file_name = self.icon_file_name()
        if icon_file_name:
            zfile = zipfile.ZipFile(self.ipa_file_path)
            zip_name_list = zfile.namelist()
            for name in zip_name_list:
                tempkey = ".app/" + icon_file_name
                if tempkey in name:
                    zfile.close()
                    return name
            zfile.close()
            
            return False
    
    def mv_icon_to(self, file_name):
        icon_path = self.icon_file_path()
        if icon_path:
            zfile = zipfile.ZipFile(self.ipa_file_path)
            
            icon_file =  open(file_name, "wb")
            icon_file.write(zfile.read(icon_path))
            icon_file.close()
            zfile.close()
            return True
    
        return False
    
if __name__ == '__main__':
    # testIpadFullPath = u'C:\\Users\\hzwangzhiwei\\Desktop\\H28_150514121833_resign.ipa'
    testIpadFullPath = "/xxx/WhatsApp_v23.25.85.ipa"
    print("testIpadFullPath=%s" % testIpadFullPath)
    parse = IpaParse(testIpadFullPath)

    ipaAllInfo = parse.all_info()
    print("ipaAllInfo=%s" % ipaAllInfo)
    # print(json.dumps(ipaAllInfo, default = lambda o: o.__dict__))
    print("app_name=%s" % parse.app_name())
    print("bundle_identifier=%s" % parse.bundle_identifier())
    print("target_os_version=%s" % parse.target_os_version())
    print("minimum_os_version=%s" % parse.minimum_os_version())
    print("icon_file_name=%s" % parse.icon_file_name())
    print("icon_file_path=%s" % parse.icon_file_path())
    # print("mv_icon_to=%s" % parse.mv_icon_to('test.png'))
