# Definindo o vetor corretamente com valores separados por vírgula
vector1 <- c(20.1, 21.1, 27.0, 26.4, 25.4, 22.3, 26.1, 24.0, 23.2, 27.0, 25.2, 24.6, 26.5, 22.5, 25.8, 27.1, 26.2, 24.1)


mean_vector1 <- mean(vector1)
mean_vector1

median_vector1 <- median(vector1)
median_vector1

moda = function(x) {
  # Encontra os valores únicos
  valores = unique(x)
  
  contagem = tabulate(match(x, valores))
  
  saida = sort(valores[contagem == max(contagem)])
  
  if (max(contagem) != 1) {
    print(saida)
    cat("Número de vezes que as modas se repetem:", max(contagem), "\n")
  } else {
    cat("A variável é amodal\n")
  }
}

vector1 <- c(20.1, 21.1, 27.0, 26.4, 25.4, 22.3, 26.1, 24.0, 23.2, 27.0, 25.2, 24.6, 26.5, 22.5, 25.8, 27.1, 26.2, 24.1)

moda(vector1)

print('terceiro qualtil')
# Calculando o terceiro quartil (Q3)
terceiro_quartil <- quantile(vector1, 0.75)

# Mostrando o terceiro quartil
terceiro_quartil

print("quadragegimo percentil ")
quadragesimo_percentil <- quantile(vector1, 0.40)


print(quadragesimo_percentil)

valor_maximo <- max(vector1)
valor_minimo <- min(vector1)

print('amplitude')
amplitude <- valor_maximo - valor_minimo
print((amplitude))

variancia <- var(vector1)
print(variancia)

desvio <- variancia * 0.5
print(desvio)

print('coef variabilidade')
coef <- (desvio / mediana_vector1) * 100
print(coef)

