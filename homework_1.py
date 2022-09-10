
import pathlib
import os
import zipfile
import sys





def main():
    
    if len(sys.argv) < 2:
        print('Enter path to folder which should be cleaned')
        exit()
    path = sys.argv[1]
    if not (os.path.exists(path) and pathlib.Path(path).is_dir()):
        path('Path incorrect')
        exit()
    p = pathlib.Path(path)


    def sort_files(path):
        images = list()
        video = list()
        docs = list()
        musick = list()
        archive = list()
        unknown = list()
        expansion = list()
        expansion_unknown = list()
        folders = list()

        def parse_folder(path):
            for object in path.iterdir():
                if object.is_file():
                    name = object.name.split(".")
                    if name[-1] in ["png","jpg","jpeg","svg"]:
                        images.append(object)
                        if object.suffix not in expansion:
                            expansion.append(object.suffix)
                    elif name[-1] in ["avi","mp4","mov","mkv"] :
                        video.append(object)
                        if object.suffix not in expansion:
                            expansion.append(object.suffix)
                    elif name[-1] in ["doc","docx","txt","pdf","xlsx","pptx"]:  
                        docs.append(object)
                        if object.suffix not in expansion:
                            expansion.append(object.suffix)
                    elif name[-1] in ["mp3","ogg","wav","amr"]:
                        musick.append(object)
                        if object.suffix not in expansion:
                            expansion.append(object)
                    elif name[-1] in ["zip","gz","tar"]:
                        archive.append(object)
                        if object.suffix not in expansion:
                            expansion.append(object)
                    else:
                        unknown.append(object)
                        if object.suffix not in expansion_unknown:
                            expansion_unknown.append(object.suffix)
                elif object.is_dir():
                    name_folder = object.name
                    if name_folder not in ("documents","images","audio","video","archives"):
                        
                        folders.append(object)
                        parse_folder(object)

        parse_folder(path)

        return archive, musick, docs, video, images, unknown, expansion, expansion_unknown, folders
    
    def normalize(list_sorted_files):
        
        def translate(path_name):


            TRANS = {1072: 'a', 1040: 'A', 1073: 'b', 1041: 'B', 1074: 'v', 1042: 'V', 1075: 'g', 1043: 'G', 
            1076: 'd', 1044: 'D', 1077: 'e', 1045: 'E', 1105: 'e', 1025: 'E', 1078: 'j', 1046: 'J', 1079: 'z', 
            1047: 'Z', 1080: 'i', 1048: 'I', 1081: 'j', 1049: 'J', 1082: 'k', 1050: 'K', 1083: 'l', 1051: 'L', 
            1084: 'm', 1052: 'M', 1085: 'n', 1053: 'N', 1086: 'o', 1054: 'O', 1087: 'p', 1055: 'P', 1088: 'r', 1056: 'R', 1089: 's', 
            1057: 'S', 1090: 't', 
            1058: 'T', 1091: 'u', 1059: 'U', 1092: 'f', 1060: 'F', 1093: 'h', 1061: 'H', 1094: 'ts', 1062: 'TS', 1095: 'ch', 
            1063: 'CH', 1096: 'sh', 1064: 'SH', 1097: 'sch', 1065: 'SCH', 1098: '', 1066: '', 1099: 'y', 1067: 'Y', 1100: '', 1068: '', 
            1101: 'e', 1069: 'E', 1102: 'yu', 1070: 'YU', 1103: 'ya', 1071: 'YA', 1108: 'je', 1028: 'JE', 1110: 'i', 1030: 'I', 
            1111: 'ji', 1031: 'JI', 1169: 'g', 1168: 'G' ,"letter_x":"x", "LETTER_X":"X", "letter_c":"c","LETTER_C":"C","letter_q":"q",
            "LETTER_Q":"Q","letter_w":"w","LETTER_W":"W"}

            new_name = str()
            without_3last_symbols = path_name.split(".")
            for letters in without_3last_symbols[:-1]:
                    for letter in letters:
                        if ord(letter) in TRANS : 
                                new_name += TRANS[ord(letter)]
                        elif letter in TRANS.values(): 
                                new_name += letter
                        elif not letter.isdigit():
                                new_name += "_"
                                continue
                        else:
                                new_name += letter
            new_name += "." + without_3last_symbols[-1]  
            return new_name
        
        for archive in  list_sorted_files[0]:
            new_way= os.path.join(archives,archive.name)
            os.replace(archive,new_way)
            new_name = os.path.join(archives,translate(archive.name))
            os.rename(new_way,new_name)
            with zipfile.ZipFile(new_name, 'r') as zip_ref:
                zip_ref.extractall(new_name)
            
        for musick in  list_sorted_files[1]:
            new_way= os.path.join(audio,musick.name)
            os.replace(musick,new_way)
            new_name = os.path.join(audio,translate(musick.name))
            os.rename(new_way,new_name)
            
        
        for docs in  list_sorted_files[2]:
            new_way= os.path.join(documents,docs.name)
            os.replace(docs,new_way)
            new_name = os.path.join(documents,translate(docs.name))
            os.rename(new_way,new_name)
        
            
        for video_old in  list_sorted_files[3]:
            new_way= os.path.join(video,video_old.name)
            os.replace(video_old,new_way)
            new_name = os.path.join(video,translate(video_old.name))
            os.rename(new_way,new_name)
            
        
        for images_old in  list_sorted_files[4]:
            new_way= os.path.join(images,images_old.name)
            os.replace(images_old,new_way)
            new_name = os.path.join(images,translate(images_old.name))
            os.rename(new_way,new_name)
        
        for folder in list_sorted_files[-1]:
            if len(os.listdir(folder)) == 0:
                os.rmdir(folder)

 

    documents = os.path.join(p,"documents")
    if not os.path.exists(documents):
        os.mkdir(documents)

    images = os.path.join(p,"images")
    if not os.path.exists(images):
        os.mkdir(images)


    audio = os.path.join(p,"audio")
    if not os.path.exists(audio):
        os.mkdir(audio)
    
    video = os.path.join(p,"video")
    if not os.path.exists(video):
        os.mkdir(video)

    archives = os.path.join(p,"archives")
    if not os.path.exists(archives):
        os.mkdir(archives)


    list_sorted_files = sort_files(p)


    normalize(list_sorted_files)

  


if __name__ == '__main__':
    exit(main())




