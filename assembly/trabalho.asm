.code
      lda N1
      not
      add #01h
      add N2
      jn CASO2


CASO1:       lda N2
             add N2
             sta N2
             jmp FIM

CASO2:       lda N1
             add N1
             add N1
             add N1
             jmp FIM

FIM:         hlt
      
.endcode



.data

N1: db #02h
N2: db #04h

.enddata