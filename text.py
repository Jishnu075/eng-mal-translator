from google_trans_new import google_translator  
import time


file_name = open("words.txt","r")
err_count = 1
done_file = open("done.txt","w")
count = 0

for line in file_name:
    #lists = line.split()
    text = line  
    count = count + 1
    try:

            translator = google_translator()  
            translate_text = translator.translate(text,lang_tgt='ml')  
            print(translate_text)
            done_file.write(translate_text)
        
    except Exception:
            print("couldnt find! , row number ", count)


    done_file.write("\n")  
    err_count = err_count + 1
    time.sleep(2)




