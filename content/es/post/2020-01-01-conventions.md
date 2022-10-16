---
title: Convenciones
date: "2020-01-01T00:00:00+00:00"
draft: false
tags: ["software engineering", "career", "onboarding", "spanish"]
---

*Las convenciones son lo que construye la sociedad*.

Por *nadie conocido*, pero entenderás mi punto de vista al leer esta entrada.

# Convenciones


## Escribe el código de manera que sea obvio

Cada ingeniero de software desarrolla un estilo único de
programación a lo largo de su carrera. Usualmente empieza
programando *código espagueti* que es extremadamente
difícil de entender (salvo para él mismo). Después,
llega al punto en el es incapaz de entender su propio
código, preguntándose cómo es posible. Más tarde aún,
llegará al punto en el que su código es obvio y fácil
de entender, sin *trucos* y es... Aburrido.

Usualmente eliminará funciones recursivas (a menos que
sea totalmente requerido), elevada complejidad y
reducirá el número de parámetros, eliminando o encapsulando
el estado en objetos, etc.

De acuerdo, ahora tu código es predecible y con un poco de
documentación puede ser entendido por cualquiera.

## No trabajamos solos

Sin embargo, cuando trabajas en un equipo, has de adaptar
tu estilo al *consenso* que ya se haya alcanzado en ese
equipo.

Por ejemplo, puedes desarrollar funciones con múltiples
puntos de retorno pero tus colegas siguen las [reglas de la NASA](https://web.cecs.pdx.edu/~kimchris/cs201/handouts/The%20Power%20of%2010%20-%20Rules%20for%20Developing%20Safety%20Critical%20Code.pdf) que obligan a tener un control de flujo
simplificado y en el equipo lo interpretan como un único
*return* en cada función.

Lo que quiero decir es que mientras puede que no aprecies las reglas
al principio, te ayudarán a llegar al mismo estándar de código que
el que tiene el equipo Así, se evitan discusiones áridas sobre
el estilo y el equipo se puede centrar en funcionalidad.

## Haz las convenciones públicas

Las convenciones que son desconocidas por nuevos miembros del
equipo les harán sentir que sus contribuciones no se aprecian.
Todos los miembros del equipo tienen que tener acceso a las guías
de estilo del proyecto.

## Usa herramientas para alcanzar un estilo

Los humanos somos falibles y las herramientas que
rescriben "código malo" a código que sigue la convención deben usarse.
Una buena manera de hacer esto, es evitar que el poder subir código
que no siga las convenciones, y además, comprobar el estilo de código
en una etapa de integración continua.

Los desarrolladores de Ruby on Rails suelen usar [Rubocop](https://github.com/rubocop-hq/rubocop) y comparten tus configuraciones de rubocop con la comunidad.

## Conclusión

Una de las cosas que hace bueno a un ingeniero de software es su
habilidad para adaptarse a diferentes equipos.
