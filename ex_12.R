setwd("C:/Users/migue/Documents/estatistica_proj")
library(fdth)

dados <-read.table("exercicio12.txt",header = TRUE)

int <- fdt(dados, h=7, start= 350, end= 392)
int 