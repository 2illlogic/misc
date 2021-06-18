library(tidyverse)

##Euler's Method for solving a first order ODE
x_n <- function(a, b, N, x_0, t_0) {
  h <- abs(a-b)/N
  n <- 0
  x <- c(x_0)
  t <- c(t_0)
  while (n < N + 1) {
    t <- c(t, t[n] + h)
    x <- c(x, x[n] + h * (1 + x[n] ^ 2))
    n <- n + 1
  }
  return (data.frame('t' = t,'x' = x))
}

df <- x_n(0,1,20,0,0)

df <- mutate(df, y = tan(t))

plot <- ggplot(data = df)

plot <- plot + geom_line(mapping = aes(x = t, y = x, color = "red"))
     
plot + geom_line(mapping = aes(x = t, y = y))


