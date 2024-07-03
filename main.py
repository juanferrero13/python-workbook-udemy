############################################################ Programa simple que identifica palabras denegadas y las censura

# deny_words = ["bar", "cerveza"]

# phrase = "hola amigo como estas? vamos a algun bar a tomar cerveza"
# words = phrase.split()

# final_phrase = ""

# for word in words:
#     if word in deny_words:
#         final_phrase += "***** "
#     else:
#         final_phrase += f"{word} "
        

# print(final_phrase)

# Forma un poco mas elaborada de hacerlo
# lista de palabras censuradas
# deny_words = ["manzana", "sabor", "cacao", "vida"]


# recibo un string de frase y retorno otro string convertido
# def phrase_filter(phrase: str) -> str:
#     # separo la frase en palabras: split() = split(" ")
#     words = phrase.split()
#     final_words = ""
#     # utilizo enumerate para tener index
#     # y evitar el espacio al principio del string
#     for index, word in enumerate(words):
#         if word in deny_words:
#             final_words += " [censurado]"
#         else:
#             final_words += word if index == 0 else f" {word}"
#     return final_words

# print(phrase_filter("La vida sin un poco de sabor seria aburrida."))        


############################################################### CALCULADORA
# Calculadora simple utilizando condicional if...else

# def calculadora():
#     num1 = int(input("Numero 1: "))
#     num2 = int(input("Numero 2: "))
#     operacion = input("Ingresa la operacion a realizar: ")
#     if operacion == "+":
#         print(f"El resultado de {num1} {operacion} {num2} es: {num1 + num2}")
#     elif operacion == "-":
#         print(f"El resultado de {num1} {operacion} {num2} es: {num1 - num2}")
#     elif operacion == "*":
#         print(f"El resultado de {num1} {operacion} {num2} es: {num1 * num2}")
#     elif operacion == "/":
#         print(f"El resultado de {num1} {operacion} {num2} es: {num1 / num2}")
#     else:
#         print("Operación no encontrada.")


# calculadora()


# Calculadora utilizando bucle while y match-case
# def calculadora():
#     while True:
#         num1_input = input("Numero 1 (o 'salir' para terminar): ")
        
#         if num1_input.lower() == 'salir':
#             print("Saliendo de la calculadora.")
#             break
        
#         num1 = int(num1_input)
        
#         num2 = int(input("Numero 2: "))
        
#         operacion = input("Ingresa la operación a realizar (+, -, *, /): ")
        
#         # Usar match-case en lugar de if...elif para realizar la operación
#         match operacion:
#             case "+":
#                 resultado = num1 + num2
#                 print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
#             case "-":
#                 resultado = num1 - num2
#                 print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
#             case "*":
#                 resultado = num1 * num2
#                 print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
#             case "/":
#                 if num2 == 0:
#                     print("Error: No se puede dividir por cero.")
#                 else:
#                     resultado = num1 / num2
#                     print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
#             case _:
#                 print("Operación no encontrada. Por favor, ingresa una operación válida.")


# calculadora()


############################################ Hangman (Ahorcado)

# import random

# # Función para crear una lista de guiones bajos del mismo largo que la palabra a adivinar
# def get_word_lines(word):
#     guess_word = []  # Lista para almacenar los guiones bajos

#     for _ in word:
#         guess_word.append("_")  # Agrega un guion bajo por cada letra en la palabra

#     return guess_word

# word_list = ["conejo", "casa", "alfonbra", "auto"]
# chosen_word = random.choice(word_list)  # Selecciona una palabra aleatoria de la lista
# guess_word = get_word_lines(chosen_word)  # Crea la lista de guiones bajos para la palabra seleccionada
# guessed = False  # Variable para controlar si la palabra ha sido adivinada
# lives = len(guess_word) - 2  # Establece el número de vidas

# print(guess_word)  # Imprime los guiones bajos iniciales

# while not guessed:
#     print(f"Lives: {lives}")

#     guess = input("Guess a letter: ").lower()  # Solicita una letra al usuario y la convierte a minúscula
#     match = False  # Variable para controlar si la letra adivinada está en la palabra

#     # Recorre cada letra de la palabra seleccionada
#     for i, letter in enumerate(chosen_word):
#         if guess == letter:  # Si la letra adivinada coincide con una letra en la palabra
#             print("Good choice!")
#             guess_word[i] = letter  # Reemplaza el guion bajo con la letra adivinada en la posición correspondiente
#             match = True  # Indica que se encontró una coincidencia

#     print(guess_word)  # Imprime el estado actual de la palabra adivinada

#     if not match:
#         lives -= 1  # Si no hubo coincidencia, se resta una vida
#         print("Wrong!")

#     if lives <= 0:
#         print("You lose...")
#         break

#     if "_" not in guess_word:
#         guessed = True  # Si no hay más guiones bajos, la palabra ha sido adivinada
#         print("You Win!") 


#########################################   Contador de palabras en un texto (y si la palabra se repite, cuantas veces está)

# # Función para eliminar signos de puntuación de un texto
# def remove_punctuation_marks(text: str):
#     punctuation_marks = [".", ",", ";", ":", "!", "?", "-", "_", "(", ")"]  # Lista de signos de puntuación a eliminar

#     for mark in punctuation_marks:
#         text = text.replace(mark, "")  # Reemplaza cada signo de puntuación en el texto con una cadena vacía

#     return text  

# # Función para contar la cantidad de veces que aparece cada palabra en un texto
# def count_words(text):
#     text = text.lower()  # Convierte todo el texto a minúsculas para evitar duplicados con mayúsculas
#     text = remove_punctuation_marks(text)  # Elimina signos de puntuación del texto

#     words = text.split()  # Divide el texto en una lista de palabras

#     word_count = {}  # Diccionario para almacenar la cantidad de veces que aparece cada palabra
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1  # Si la palabra ya está en el diccionario, incrementa su contador
#         else:
#             word_count[word] = 1  # Si la palabra no está en el diccionario, la agrega con un contador de 1

#     return word_count  

# sample_text = "Hola mundo, este es un texto de prueba, un simple texto."
# result = count_words(sample_text)  
# for word, count in result.items():
#     print(f"'{word}': {count} times")
#     if count >= 2:
#         print(f"'{word}': {count} times")
#     else:
#         print(f"'{word}': {count} time")


