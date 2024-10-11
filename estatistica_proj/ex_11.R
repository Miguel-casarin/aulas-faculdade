setwd("C:/Users/migue/Documents/estatistica_proj")

dados <- read.table("exercicio11.txt", header = TRUE)
dados_coluna <- dados[,1]


frequencia_absoluta <- table("frequencia_absoluta" = dados_coluna)
frequencia_percentual <- prop.table(table("frequecia_percentual"= dados_coluna))*100

tabela_final <- data.frame(frequencia_absoluta, frequencia_percentual)
tabela_final
