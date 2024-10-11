getwd()

dados<-read.table("exemplo.BD.txt",head = TRUE)
dados
summary(dados)

genero<-dados[,2]
genero2<-dados$genero
genero2
tabela1<-table(genero)
tabela1
tabela2<-prop.table(table(genero))
tabela2
