
# pip install -U git+https://github.com/cdown/srt.git@develop
# https://github.com/mouuff/mtranslate
# python setup.py install

import srt
from mtranslate import translate
import os
import sys
import codecs


def readsrt(pathname):
    try:
        # read subtitle
        fr = open(pathname, 'r')
        return fr.read();

    except Exception as e:
        print('Error readsrt(): ', pathname, ':', e )

def writesrt(pathname, text):
    try:
        # write subtitle 
        fw = open(pathname, 'w', encoding='utf8')        
        fw.write(text)              
    except Exception as e:
        print('Error writesrt(): ', pathname, ':', e )

def srt_trasnlate(text, to_lang):
    
    srttext = srt.parse(text)
    subtitles = list(srttext)
    # for each content
    for subtitle in subtitles:
        
        txtcontent = subtitle.content
        #print(txtcontent)
        #print('...')
		
        txtcontent_translate = ""
        # translate for line
        for line in txtcontent.splitlines():
            linetranslate = translate(line, to_lang )
            txtcontent_translate += linetranslate + '\n'
            
        #print(txtcontent_translate)
        #print('...')
        
        # update 
        subtitle.content = txtcontent_translate 
    
    
    srttextcmp = srt.compose(subtitles)
    return srttextcmp

def srt_trasnlate_all(filename_out, filename_in, to_lang):
    
    # include file root
    root = os.path.splitext(os.path.splitext(filename_in)[0])[0]
    srt_files = os.listdir(root)

    # trasnlate of the each file 
    for srt_file in srt_files:            
        
        print(srt_file)
        
        # read
        text = readsrt(os.path.join(root,srt_file))
        # translate
        text_transalate = srt_trasnlate(text,to_lang);
        # write
        writesrt(os.path.join(filename_out,srt_file), text_transalate)









