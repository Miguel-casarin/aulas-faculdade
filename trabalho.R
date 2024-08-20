install.packages("e1071")


dados = c(122.2, 124.2, 124.3, 125.6, 126.3, 126.5, 126.5, 127.2, 127.3, 127.5, 127.9, 128.8, 129.0,
           129.2, 129.4, 129.6, 130.2, 130.4, 130.8, 131.3, 131.4, 131.4, 131.5, 131.6, 131.6, 131.8,
           131.8, 132.3, 132.4, 132.4, 132.5, 132.5, 132.5, 132.5, 132.6, 132.7, 132.9, 133.0, 133.1,
           133.1, 133.1, 133.1, 133.2, 133.2, 133.2, 133.3, 133.3, 133.5, 133.5, 133.6, 133.8, 133.9,
           134.0, 134.0, 134.0, 134.0, 134.1, 134.2, 134.3, 134.4, 134.4, 134.6, 134.7, 134.7, 134.7,
           134.8, 134.8, 134.8, 134.9, 134.9, 135.2, 135.2, 135.2, 135.3, 135.3, 135.4, 135.5, 135.5,
           135.6, 135.6, 135.7, 135.8, 135.8, 135.8, 135.8, 135.8, 135.9, 135.9, 135.9, 135.9, 136.0,
           136.0, 136.1, 136.2, 136.2, 136.3, 136.4, 136.4, 136.6, 136.8, 136.9, 136.9, 137.0, 137.1,
           137.2, 137.6, 137.6, 137.8, 137.8, 137.8, 137.9, 137.9, 138.2, 138.2, 138.3, 138.3, 138.4,
           138.4, 138.4, 138.5, 138.5, 138.6, 138.7, 138.7, 139.0, 139.1, 139.5, 139.6, 139.8, 139.8,
           140.0, 140.0, 140.7, 140.7, 140.8, 140.9, 141.2, 141.4, 141.5, 141.6, 142.9, 143.4, 143.5,
           143.6, 143.8, 143.8, 143.9, 144.1, 144.5, 144.5, 147.7, 147.7)



# numero total elementos 
total_dados = length(dados)
print(total_dados)



media = mean(dados)
print(media)
mediana = median(dados)
print(mediana)



#desvio interquartilico
desvio_interqua = IQR(dados)
print(desvio_interqua)

#primeiro quartil
primeiro_quartil <- quantile(dados, 0.25)
print(primeiro_quartil)

#terceiro quartil
terceiro_quartil <- quantile(dados, 0.75)
print(terceiro_quartil)

valor_maximo <- max(dados)
valor_minimo <- min(dados)
print(valor_maximo)
print(valor_minimo)

print('amplitude')
amplitude <- valor_maximo - valor_minimo
print((amplitude))

print('variancia')
variancia <- var(dados)
print(variancia)

print('desvio')
desvio <- variancia ** 0.5
print(desvio)

percentis = quantile(dados, probs = c(0.10, 0.90))
c10 = percentis[1]
c90 = percentis[2]
print(c10)
print(c90)

# Coeficiente de assimetria de Pearson
pearson <- function(dados) {
  me <- mean(dados)
  m <- median(dados)
  sd <- sd(dados)
  pearson <- 3 * (me - m) / sd
  names(pearson) <- "pearson"
  return(pearson)
}
pearson_value <- pearson(dados)
print(paste("Coeficiente de Assimetria de Pearson:", pearson_value))

# Função para calcular o coeficiente de assimetria de Yule
yule <- function(x) {
  q1 <- quantile(x, 0.25, type = 5)
  q2 <- quantile(x, 0.5, type = 5)
  q3 <- quantile(x, 0.75, type = 5)
  yule <- (q3 + q1 - 2 * q2) / (q3 - q1)
  names(yule) <- "yule"
  return(yule)
}

# Calcular o coeficiente de Yule
yule_value <- yule(dados)
print(paste("Coeficiente de Assimetria de Yule:", yule_value))

# Função para calcular o coeficiente de assimetria de Kelley
kelley <- function(x) {
  q1 <- quantile(x, 0.1, type = 5)
  q2 <- quantile(x, 0.5, type = 5)
  q3 <- quantile(x, 0.9, type = 5)
  kelley <- (q3 + q1 - 2 * q2) / (q3 - q1)
  names(kelley) <- "kelley"
  return(kelley)
}

# Calcular o coeficiente de Kelley
kelley_value <- kelley(dados)
print(paste("Coeficiente de Assimetria de Kelley:", kelley_value))