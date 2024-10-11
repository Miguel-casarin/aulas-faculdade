.code
         lda N
         
INICIO:  add M
         sta N
FIM:     hlt

.endcode

         



.data
N:    db #04h
M:    db #02h

.enddata