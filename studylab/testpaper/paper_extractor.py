#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import re
from PIL import Image
import io
import base64
import json
import time
import uuid
import numpy as np
import zipfile
# In[2]:


def getcleanxml(text):
    return BeautifulSoup(text,'lxml')


# In[3]:


def getcleanhtml(text):
    return BeautifulSoup(text,'html.parser')


# In[4]:


def getsubjects(xml):
    subject_wise_split=re.split('##',str(xml))
    json_obj={}
    for x in range(1,len(subject_wise_split),2):
        json_obj[subject_wise_split[x]]=subject_wise_split[x+1]   
    return json_obj    


# In[5]:


def getsection(xml):
    subject_wise_split=re.split('#',str(xml))
    json_obj={}
    for x in range(1,len(subject_wise_split),2):
        json_obj[subject_wise_split[x]]=subject_wise_split[x+1]
    return json_obj


# In[6]:


def get_img_from_base64(string):
        decoded=base64.b64decode(string)
        return Image.open(io.BytesIO(decoded))


# In[7]:


def encode_base64(obj):
    return base64.b64encode(obj)


# In[8]:


def get_json_from_single_multiple_type(ques,img2ids):    
    ques_arr=re.split("vishwas",ques)
    data=[]
    for part in ques_arr:
        data.append(get_text_img_array(part,img2ids))
    ques_data={}
    ques_data["ques"]=data[0]
    ques_data["options"]=data[1:]
    return ques_data


# In[9]:


def get_json_from_integer_type(ques,img2ids):
    ques_data={}
    ques_data["ques"]=get_text_img_array(ques,img2ids)
    ques_data["value"]=ques_data    
    return ques_data


# In[10]:


def get_json_from_paragraph_type(para,img2ids):
    ques_arr=re.split("Nikhil",para)
    json_para={}
    json_para["paragraph"]=get_text_img_array(ques_arr[0],img2ids)
    json_para["questions"]=[]
    for ques in ques_arr[1:]:
        json_ques=get_json_from_single_multiple_type(ques,img2ids)
        json_para['questions'].append(json_ques)
    return json_para


# In[11]:


def get_json_from_match_type(match,img2ids):
    ques_arr=re.split("vishwas",match)
    json_match={}
    json_match['instruction']=get_text_img_array(ques_arr[0],img2ids)
    json_match['col1']=[]
    json_match['col2']=[]
    for opt in ques_arr[1:]:
        split=re.split("tanmay",opt)
        json_match['col1'].append(get_text_img_array(split[0],img2ids))
        for x in split[1:]:
            json_match['col2'].append(get_text_img_array(x,img2ids))
    return json_match        


# In[12]:


def getcompletejson(xml,img2ids):
    img_json={}
    sub_json=getsubjects(xml)
    complete_json=[]
    for sub in sub_json.keys():
        section=getsection(sub_json[sub])
        for key in section.keys():
            if(key=='Multiple'):
                splitted=re.split('Nikhil',str(section[key]))
                for q in range(1,len(splitted)):
                    question_json=get_json_from_single_multiple_type(splitted[q],img2ids)
                    question_json['type']="Multiple"
                    question_json['subject']=sub
                    complete_json.append(question_json)
            elif(key=='Single'):
                splitted=re.split('Nikhil',str(section[key]))
                for q in range(1,len(splitted)):
                    question_json=get_json_from_single_multiple_type(splitted[q],img2ids)
                    question_json['type']="Single"
                    question_json['subject']=sub
                    complete_json.append(question_json)
            elif(key=='Integer'):
                splitted=re.split('Nikhil',str(section[key]))
                for q in range(1,len(splitted)):
                    question_json=get_json_from_integer_type(splitted[q],img2ids)
                    question_json['type']="Integer"
                    question_json['subject']=sub
                    complete_json.append(question_json)
            elif(key=='Para'):
                splitted=re.split('shubham',str(section[key]))
                for q in range(1,len(splitted)):
                    question_json=get_json_from_paragraph_type(splitted[q],img2ids)
                    question_json['type']="Paragraph"
                    question_json['subject']=sub
                    complete_json.append(question_json)        
            elif(key=='Match'):
                splitted=re.split('Nikhil',str(section[key]))
                for q in range(1,len(splitted)):
                    question_json=get_json_from_match_type(splitted[q],img2ids)
                    question_json['type']="Match"
                    question_json['subject']=sub
                    complete_json.append(question_json)
    return complete_json      


# In[13]:


def get_text_img_array(part,img2ids):
    temp=[]
    n=0
    arr=re.findall('<w:t>(.*?)</w:t>|<w:t xml:space="preserve">(.*?)</w:t>|w:hAnsi="(.*?)"|w:hansi="(.*?)"|<w:vertAlign w:val="(.*?)"|<w:vertalign w:val="(.*?)"|"rId(.*?)"', part)
    text_json={"type":"text","text":None,"font":None,"vertalign":None}
    for x in arr:
        t1,t2,font1,font2,align1,align2,rel_id=x
        t=t1+t2
        if t!="":
            text_json['text']=t
            temp.append(dict(text_json))
            text_json['font']=None
            text_json['text']=None
            text_json['vertalign']=None
        elif(font1!=""):
            text_json['font']=font1
        elif(font2!=""):
            text_json['font']=font2    
        elif(align1!=""):
            text_json['vertalign']=align1
        elif(align2!=""):
            text_json['vertalign']=align2
        elif(rel_id!=""):
            id_="rId"+rel_id
            try:
                temp.append({"type":"img","img":img2ids[id_]['id'],"format":img2ids[id_]['format']})
            except:
                print("invalid id")
    return temp


# In[20]:


def scrap_docx(docx_file):
    uuid2base64img={}
    rids2uuid={}
    imgname2rids={}
    with zipfile.ZipFile(docx_file) as zipa:
        docx=zipa.read('word/document.xml')
        docx_rel=zipa.read('word/_rels/document.xml.rels')
        for x in re.findall('Id="(.*?)" Type="(.*?)" Target="(.*?)"',str(docx_rel)):
            id_,type_,target=x
            if("media" in target):
                imgname2rids[target[6:]]=id_
        for filename in zipa.namelist():
            if filename.startswith("word/media/image"):
                id_=uuid.uuid4().hex
                rids2uuid[imgname2rids[filename[11:]]]={"id":id_,"format":filename[-3:]}
                uuid2base64img[id_]=encode_base64(zipa.read(filename))
    docx=getcleanxml(docx)
    data=getcompletejson(docx,rids2uuid)
    return data,uuid2base64img


# In[21]:


data,img=scrap_docx('Paper 1.docx')




