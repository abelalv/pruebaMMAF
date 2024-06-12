## Conjunto de datos: swiss


data(swiss)

summary(swiss)

library(lattice)
splom(swiss, pscale=0, type=c('p', 'smooth'),
      groups=swiss$Catholic > 50, xlab='')

## Resumen de  información

summary(swiss)