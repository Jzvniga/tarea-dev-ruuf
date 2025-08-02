def calculate_panels(a: int, b: int, x: int, y: int) -> int:
    """
    Calcula cuántos paneles solares de tamaño a x b caben en un techo de tamaño x x y.
    Se permite rotar los paneles para aprovechar mejor el espacio.
    """

    def max_panels(panel_w, panel_h, roof_w, roof_h):
        max_count = 0
        # Intentamos colocar i columnas de paneles (sin rotar) y ver si podemos rellenar lo que sobra con paneles rotados
        for i in range(roof_w // panel_w + 1):
            ancho_ocupado = i * panel_w
            alto_ocupado = roof_h // panel_h
            total_original = i * alto_ocupado

            # Espacio restante horizontal, tratamos de usarlo con paneles rotados
            ancho_restante = roof_w - ancho_ocupado
            alto_restante = roof_h

            paneles_rotados = (ancho_restante // panel_h) * (alto_restante // panel_w)
            total_combinado = total_original + paneles_rotados

            # Guardamos el máximo
            max_count = max(max_count, total_combinado)

        return max_count

    # Probamos ambas orientaciones
    return max(
        max_panels(a, b, x, y),
        max_panels(b, a, x, y)
    )

if __name__ == "__main__":
    print(calculate_panels(1, 2, 2, 4))  # Esperado: 4
    print(calculate_panels(1, 2, 3, 5))  # Esperado: 7
    print(calculate_panels(2, 2, 1, 10)) # Esperado: 0