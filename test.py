
import srttrans

# configurate 
to_lang = 'es'
filename_in = 'SRTMOVI'
filename_out = 'SRTMOVI_OUT'

# translate
srttrans.srt_trasnlate_all(filename_out,filename_in,to_lang)

