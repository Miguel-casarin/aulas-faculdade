getwd()
setwd("C:/Users/migue/Documents/estatistica_proj")

dados<- read.table("exercicio9.txt", header = TRUE)

frequencia_absoluta <- table(dados$Provedor)
frequencia_relativa <- prop.table(table(dados$Provedor))
frequencia_percentual <- prop.table(table(dados$Provedor)) * 100

tabela_final <- data.frame(
  Provedor = names(frequencia_absoluta),
  Frequencia_Absoluta = as.numeric(frequencia_absoluta),
  Frequencia_Relativa = as.numeric(frequencia_relativa),
  Frequencia_Percentual = as.numeric(frequencia_percentual)
)

tabela_final
