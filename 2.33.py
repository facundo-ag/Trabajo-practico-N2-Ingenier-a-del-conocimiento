def hacer_reserva(reservas, fecha, huesped, habitacion, precio):
   
    if fecha not in reservas:
        reservas[fecha] = []
    
    for _, hab, _ in reservas[fecha]:
        if hab == habitacion:
            return f"La habitación {habitacion} ya está reservada en {fecha}"
  
    reservas[fecha].append((huesped, habitacion, precio))
    return f"Reserva confirmada para {huesped} en habitación {habitacion} el {fecha}"


reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}
print(hacer_reserva(reservas, "2024-08-15", "María", 101, 200)) 
print(hacer_reserva(reservas, "2024-08-15", "Pedro", 103, 170))  
print(hacer_reserva(reservas, "2024-08-17", "Lucía", 104, 190))  
print("\nEstado final de reservas:")
print(reservas)
