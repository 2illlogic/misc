library(tidyverse)
rm(list = ls())
# whole plane
x <- seq(-pi/2,pi/2,0.1)
y <- seq(-pi/2,pi/2,0.1)
# real axis between -pi/2 and pi/2
x <- seq(-pi/2,pi/2,0.1)
y <- rep(0, length(x))
# imaginary axis
y <- seq(-2, 2, 0.1)
x <- rep(0, length(y))
#line -pi/2 + iy
y <- seq(-2, 2, 0.1)
x <- rep(-pi/2, length(y))
#line pi/2 + iy
y <- seq(-2, 2, 0.1)
x <- rep(pi/2, length(y))

#expand domain as grid of points
domain <- as.tibble(expand.grid(x = x, y = y))

mod <- domain %>% 
  mutate(z = complex(real=x, imaginary=y)) %>%
  mutate(
    modulus = Mod(z), 
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
plot_range <- ggplot(data = mod, mapping = aes(x = u, y = v)) +
  geom_point(mapping = aes(color = modulus))

par(mfrow = c(1,2))
plot_domain
plot_range
