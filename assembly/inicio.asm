.code
        lda N1
        jz FIM
        lda N2
        jz FIM
        not
        add #01h
        add N1
        jn CASO2

CASO1:  lda N1
        sta MAX
        lda N2
        sta MIN
        jmp MTP

CASO2:  lda N1
        sta MIN
        lda N2
        sta MAX

MTP:    lda MIN

INICIO: add #0ffh
        sta MIN
        lda RESULTADO
        add MAX
        sta RESULTADO
        lda MIN
        jz FIM
        jmp INICIO
FIM:    hlt

.endcode


.data

N1:     db #04h
N2:     db #02h

MAX:    db #00h
MIN:    db #00h

RESULTADO: db #00h

.enddata
