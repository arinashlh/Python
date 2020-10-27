def mergesort(A):
    print("splitting ", A)
    # To Do 
    if len(A) > 1 : #kalo panjang A nya > 1 maka akan : 
        mid = len(A)//2 # mencari titik tengah dari array menggunakan len(A) dibagi 2
        left = A[:mid]  # mengambil nilai left dari posisi awal sampai batas mid
        right = A[mid:] # mengambil nilai right dari posisi batas mid sampai akhir
        mergesort(left) # untuk mengurutkan bagian sebelah kiri
        mergesort(right)   #  untuk mengurutkan bagian sebelah kanan
        merge(A, left, right)   #untuk memanggil program merge

def merge(A, left, right):
    i= j = k = 0 # To Do # mengambil pointer untuk left(i), right(j), A(k)
    while i < len(left) and j < len(right): # melakukan perulangan 
        # To Do #
        if left[i] <= right[j]: #mengecek apakah left[i] <= right [j] 
            A[k] = left[i]  #jika iya,nilai left[i] akan tersimpan di A[k]
            i = i + 1   #dan melakukan penambahan index i + 1
        else:   # jia tidak:
            A[k] = right[j] # maka nilai right[j] akan tersimpan di A[k]
            j = j + 1   #dan melakukan penambahan index j + 1
        k = k + 1   #dan setiap melakukan proses tersebut k akan melakukan penambahan

    while i < len(left):    #melakukan perulangan jika i < dari len(left)
        # To Do
        A[k] = left [i] #kemudian disimpan ke A[k]
        i = i + 1   #dan melakukan penambahan index i + 1
        k = k + 1   #dan melakukan penambahan index k + 1

    while j < len(right):    #melakukan perulangan jika j < dari len(right)
        # To Do
        A[k] = right[j] #kemudian disimpan ke A[k]
        j = j + 1   #dan melakukan penambahan index j + 1
        k = k + 1   #dan melakukan penambahan index k + 1
    #pokoknya 2 while terakhir itu mengecek sisa gitu, saya ngejelasinnya juga bingung :)
    print("merging", A)  
 
  
A = [15, 4, 9, 2, 16, 7, 0, 19, 5, 8]
mergesort(A)
print(A)

#sumber:
#Diktat bu pudy
#Google meet bersama bu pudy
#https://www.geeksforgeeks.org/merge-sort/


