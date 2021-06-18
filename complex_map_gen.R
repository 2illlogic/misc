library(tidyverse)

plot_complex <- function(x,y){
  #x is a vector of numbers that will be Re(z)
  #y is a vector of numbers that will be Im(z)
  i = complex(real = 0, imaginary = 1)
  
  #expand domain as grid of points
  domain <- as.tibble(expand.grid(x = x, y = y))
  
  mod <- domain %>% 
    mutate(z = x + i * y) %>%
    mutate(
      modulus = Mod(z), 
      #need to generalize here
      w = sin(z)
    ) %>%
    mutate(
      u = Re(w),
      v = Im(w)
    )
  
  #plot the domain
  plot_domain <- ggplot(data = mod, mapping = aes(x = x, y = y)) +
    geom_point(mapping = aes(color = modulus))
  
  #plot the range 
  #note: points are colored by the original modulus
  plot_range <- ggplot(data = mod, mapping = aes(x = u, y = v)) +
    geom_point(mapping = aes(color = modulus))
  
  print(plot_domain)
  print(plot_range)
}

