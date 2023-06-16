idioma={}
palabras= input("ingresar frases en español/ingles separadas por (,)")

for i in palabras.split(", "):
    clave, valor= i.split(":")
    idioma[clave]=valor


# Pedir una frase en español para traducir
frase_espanol = input("Introduce una frase en español para traducir: ").title()
palabras_frase = frase_espanol.split(" ")

# Traducir la frase palabra por palabra
frase_traducida = ""
for palabra in palabras_frase:
    if palabra in idioma:
        frase_traducida += idioma[palabra] + " "
    else:
        frase_traducida += palabra + " "

# Mostrar la frase traducida
print("La frase traducida es: ", frase_traducida)

# palabras en español e ingles
# Amor:Love, Casa:House, Gato:Cat, Perro:Dog, Comida:Food, Coche:Car, Aire:Air, Agua:Water, Fuego:Fire, Tiempo:Time, Cielo:Sky, Sol:Sun, Luna:Moon, Estrella:Star, Trabajo:Work, Dinero:Money, Salud:Health, Felicidad:Happiness, Tristeza:Sadness, Alegría:Joy, Miedo:Fear, Odio:Hate, Sueño:Sleep, Vida:Life, Muerte:Death, Amigo:Friend, Enemigo:Enemy, Padre:Father, Madre:Mother, Hombre:Man, Mujer:Woman, Niño:Boy, Niña:Girl, Hermano:Brother, Hermana:Sister, Abuelo:Grandfather, Abuela:Grandmother, Tío:Uncle, Tía:Aunt, Primo:Cousin, Sobrino:Nephew, Sobrina:Niece, Esposo:Husband, Esposa:Wife, Novio:Boyfriend, Novia:Girlfriend, Hijo:Son, Hija:Daughter, Pareja:Couple, Matrimonio:Marriage, Divorcio:Divorce, Viaje:Trip, Vacaciones:Vacation, Naturaleza:Nature, Animal:Animal, Planta:Plant, Bosque:Forest, Montaña:Mountain, Río:River, Mar:Sea

# frase a traducir
# Mi abuela prepara deliciosa comida en su casa, donde siempre hay amor y alegría Los niños juegan con su gato y su perro mientras el tiempo pasa lentamente Mi amigo y yo vamos a viajar en coche a través de la montaña y el bosque disfrutando de la naturaleza y la vida El agua del río y el mar es clara y refrescante y el cielo está lleno de estrellas brillantes La vida es corta pero la felicidad la salud y el amor son siempre importantes