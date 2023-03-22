def main():
    txt  = input()
    txt_into_list = list(txt.strip(" "))
    
    for l in txt_into_list:
        for j in ["a", "e", "i", "o", "u"]:
            if l == j:
                txt_into_list.remove(l)
            else: pass

    print("".join(txt_into_list))
 

main()