

class EjerciciosPython:
    def suma(self, a, b):
        """
        Función que suma dos números.

        Args:
        a (int, float): El primer número.
        b (int, float): El segundo número.

        Returns:
        int, float: La suma de los dos números.
        """
        return a + b

    def area_triangulo(self, base, altura):
        """
        Función que calcula el área de un triángulo.

        Args:
        base (int, float): La base del triángulo.
        altura (int, float): La altura del triángulo.

        Returns:
        float: El área del triángulo.
        """
        return (base * altura) / 2

    def inverso_cadena(self, cadena):
        """
        Función que invierte una cadena.

        Args:
        cadena (str): La cadena a invertir.

        Returns:
        str: La cadena invertida.
        """
        return cadena[::-1]

    def conteo_vocales(self, cadena):
        """
        Función que cuenta el número de vocales en una cadena.

        Args:
        cadena (str): La cadena en la que se contarán las vocales.

        Returns:
        int: El número de vocales en la cadena.
        """
        contador = 0
        for letra in cadena:
            if letra.lower() in "aeiou":
                contador += 1
        return contador

    def ordenar_lista(self, lista):
        """
        Función que ordena una lista de números de menor a mayor.

        Args:
        lista (list): La lista de números a ordenar.

        Returns:
        list: La lista ordenada.
        """
        return sorted(lista)

    def factorial(self, n):
        """
        Función que calcula el factorial de un número.

        Args:
        n (int): El número para calcular el factorial.

        Returns:
        int: El factorial de n.
        """
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

    def es_palindromo(self, cadena):
        """
        Función que verifica si una cadena es un palíndromo.

        Args:
        cadena (str): La cadena a verificar.

        Returns:
        bool: True si la cadena es un palíndromo, False de lo contrario.
        """
        return cadena == cadena[::-1]

    def numeros_primos(self, n):
        """
        Función que genera una lista de números primos menores o iguales a n.

        Args:
        n (int): El número límite.

        Returns:
        list: Lista de números primos menores o iguales a n.
        """
        primos = []
        for num in range(2, n + 1):
            es_primo = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.append(num)
        return primos

    def promedio(self, lista):
        """
        Función que calcula el promedio de una lista de números.

        Args:
        lista (list): La lista de números.

        Returns:
        float: El promedio de la lista.
        """
        if not lista:
            return 0
        return sum(lista) / len(lista)

    def eliminar_duplicados(self, lista):
        """
        Función que elimina los elementos duplicados de una lista.

        Args:
        lista (list): La lista de números.

        Returns:
        list: La lista sin elementos duplicados.
        """
        return list(set(lista))