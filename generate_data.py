from faker import Faker
import pandas as pd
import random

# Usa 'es' para español general
fake = Faker('es')

def generate_sales_data(start_date, end_date, num_records, num_clients, num_vendors, num_cities, num_products):
    # Productos con descripciones y unidades especificas
    productos = [
        ('Taladro Inalambrico, 18V', 'unidad', 'Herramientas'),
        ('Sierra Circular, 1500W', 'unidad', 'Herramientas'),
        ('Cemento Portland, 50kg', 'unidad', 'Construccion'),
        ('Bloques de Hormigon, 20x20x40 cm', 'unidad', 'Construccion'),
        ('Pintura Exterior Blanca, 1 Galon', 'unidad', 'Construccion'),
        ('Paracetamol 500mg, 20 tabletas', 'unidad', 'Salud'),
        ('Jarabe para la Tos, 200ml', 'unidad', 'Salud'),
        ('Vitaminas Multivitaminicas, 100 tabletas', 'unidad', 'Salud'),
        ('Antibiotico Amoxicilina 500mg, 30 capsulas', 'unidad', 'Salud'),
        ('Gel Antibacterial, 500ml', 'unidad', 'Salud'),
        ('Bicicleta de Montaña, 26 pulgadas', 'unidad', 'Deportes'),
        ('Balon de Futbol Profesional', 'unidad', 'Deportes'),
        ('Ropa Deportiva Hombre, Talla L', 'unidad', 'Deportes'),
        ('Zapatos de Correr Mujer, Talla 38', 'unidad', 'Deportes'),
        ('Guantes de Boxeo, 12 oz', 'unidad', 'Deportes'),
        ('Aceite de Motor Sintetico, 5W-30, 4L', 'unidad', 'Automotriz'),
        ('Filtro de Aire, Modelo Universal', 'unidad', 'Automotriz'),
        ('Bateria para Auto, 12V', 'unidad', 'Automotriz'),
        ('Llantas para Todo Terreno, 265/70R17', 'unidad', 'Automotriz'),
        ('Limpiaparabrisas, 24 pulgadas', 'unidad', 'Automotriz'),
        ('Refrigerador LG, 20 pies cubicos', 'unidad', 'Electrodomesticos'),
        ('Lavadora Whirlpool, 16kg', 'unidad', 'Electrodomesticos'),
        ('Microondas Panasonic, 1200W', 'unidad', 'Electrodomesticos'),
        ('Horno Electrico Black+Decker, 50L', 'unidad', 'Electrodomesticos'),
        ('Sistema de Sonido Bose, 2.1 Canales', 'unidad', 'Electrodomesticos'),
        ('Novela de Misterio, Edicion de Bolsillo', 'unidad', 'Libros'),
        ('Manual de Cocina Internacional', 'unidad', 'Libros'),
        ('Libro de Ciencia Ficcion, Tapa Dura', 'unidad', 'Libros'),
        ('Enciclopedia de Ciencias Naturales', 'unidad', 'Libros'),
        ('Guia Completa de Programacion en Python', 'unidad', 'Libros'),
        ('Whisky Escoces, 12 años, 750ml', 'unidad', 'Bebidas'),
        ('Vino Tinto Cabernet Sauvignon, 750ml', 'unidad', 'Bebidas'),
        ('Cerveza Artesanal, 355ml', 'unidad', 'Bebidas'),
        ('Jugo de Naranja Natural, 1L', 'unidad', 'Bebidas'),
        ('Agua Mineral con Gas, 1L', 'unidad', 'Bebidas'),
        ('Lego Set de Construccion, 1000 piezas', 'unidad', 'Juguetes'),
        ('Muneca Barbie, Edicion Especial', 'unidad', 'Juguetes'),
        ('Coche de Juguete a Control Remoto', 'unidad', 'Juguetes'),
        ('Rompecabezas 3D, 500 piezas', 'unidad', 'Juguetes'),
        ('Peluche Gigante de Oso', 'unidad', 'Juguetes'),
        ('Kit de Herramientas para Jardin, 5 Piezas', 'unidad', 'Jardin'),
        ('Tierra para Macetas, 50L', 'unidad', 'Jardin'),
        ('Maceta de Ceramica, 30 cm', 'unidad', 'Jardin'),
        ('Semillas de Flores Variadas', 'unidad', 'Jardin'),
        ('Regadera Metalica, 10L', 'unidad', 'Jardin'),
        ('Coche de Bebe Plegable', 'unidad', 'Bebes'),
        ('Silla de Auto para Bebe', 'unidad', 'Bebes'),
        ('Juego de Ropa para Bebe, 5 Piezas', 'unidad', 'Bebes'),
        ('Juguete de Actividades para Bebe', 'unidad', 'Bebes'),
        ('Pañales Desechables, Talla M, 80 Unidades', 'unidad', 'Bebes'),
        ('Freidora de Aire, 4L', 'unidad', 'Electrodomesticos'),
        ('Batidora de Mano, 600W', 'unidad', 'Electrodomesticos'),
        ('Cafetera de Goteo, 12 Tazas', 'unidad', 'Electrodomesticos'),
        ('Ventilador de Pie, 16 pulgadas', 'unidad', 'Electrodomesticos'),
        ('Plancha a Vapor, 2200W', 'unidad', 'Electrodomesticos'),
        ('Router WiFi de Doble Banda', 'unidad', 'Electronica'),
        ('Disco Duro Externo 1TB', 'unidad', 'Electronica'),
        ('Memoria USB 64GB', 'unidad', 'Electronica'),
        ('Tarjeta Grafica Nvidia GTX 1660', 'unidad', 'Electronica'),
        ('Impresora Multifuncional HP', 'unidad', 'Electronica'),
        ('Camiseta de Algodon, Talla M', 'unidad', 'Ropa'),
        ('Pantalones Cortos para Hombre, Talla L', 'unidad', 'Ropa'),
        ('Sueter de Lana, Talla S', 'unidad', 'Ropa'),
        ('Abrigo de Invierno, Talla M', 'unidad', 'Ropa'),
        ('Calcetines de Deporte, Paquete de 6', 'unidad', 'Ropa'),
        ('Alimento para Perro, 20kg', 'unidad', 'Mascotas'),
        ('Juguete para Gato, Raton de Peluche', 'unidad', 'Mascotas'),
        ('Correa para Perro Ajustable', 'unidad', 'Mascotas'),
        ('Arena para Gato, 10kg', 'unidad', 'Mascotas'),
        ('Casa para Mascota, Talla Grande', 'unidad', 'Mascotas'),
        ('Tensiometro Digital para Brazo', 'unidad', 'Salud'),
        ('Termometro Infrarrojo', 'unidad', 'Salud'),
        ('Oximetro de Pulso, Portable', 'unidad', 'Salud'),
        ('Silla de Ruedas Plegable', 'unidad', 'Salud'),
        ('Baston Ajustable para Caminar', 'unidad', 'Salud'),
        ('Cuaderno de 100 Hojas, Rayado', 'unidad', 'Papeleria'),
        ('Boligrafos de Gel, Paquete de 10', 'unidad', 'Papeleria'),
        ('Marcadores Permanentes, Set de 12', 'unidad', 'Papeleria'),
        ('Papel para Impresora, 500 Hojas', 'unidad', 'Papeleria'),
        ('Tijeras Escolares, 2 Piezas', 'unidad', 'Papeleria'),
        ('Guitarra Acustica, Cuerdas de Nylon', 'unidad', 'Musica'),
        ('Teclado Electrico, 61 Teclas', 'unidad', 'Musica'),
        ('Bateria Electronica, 5 Piezas', 'unidad', 'Musica'),
        ('Amplificador de Guitarra, 50W', 'unidad', 'Musica'),
        ('Auriculares In-Ear, Monitoreo de Sonido', 'unidad', 'Musica')
    ]

    clientes = [
        'Juan Perez', 'Maria Fernandez', 'Jose Rodriguez', 'Ana Lopez', 'Luis Gomez', 'Carla Martinez', 
        'Pedro Fernandez', 'Isabel Morales', 'Jorge Soto', 'Laura Ruiz', 'Ricardo Ortega', 'Carmen Soto', 
        'David Pena', 'Sandra Rivas', 'Hector Garcia', 'Patricia Leon', 'Fernando Gonzalez', 'Estela Vargas', 
        'Manuel Castro', 'Veronica Ruiz', 'Javier Romero', 'Gabriela Pena', 'Diego Martinez', 'Nadia Flores', 
        'Antonio Mendez', 'Monica Hernandez', 'Emanuel Torres', 'Beatriz Diaz', 'Ruben Sanchez', 'Marta Lopez', 
        'Oscar Morales', 'Julia Ramirez', 'Carlos Jimenez', 'Lorena Silva', 'Alfredo Guzman', 'Rosa Moreno', 
        'Luis Medina', 'Ana Maria Rodriguez', 'Sergio Alvarez', 'Lucia Martinez', 'Ramon Perez', 'Adriana Vargas', 
        'Andres Fernandez', 'Nancy Salazar', 'Alejandro Castro', 'Raquel Soto', 'Carlos Ramirez', 'Margarita Lopez', 
        'Ivan Rodriguez', 'Lidia Fernandez', 'Mario Gomez', 'Elena Castro', 'Luis Miguel Martinez', 'Laura Garcia',
        'Alba Martinez', 'Emanuel Perez', 'Claudia Gomez', 'Hector Lopez', 'Silvia Rodriguez', 'Rafael Mendoza',
        'Elena Hernandez', 'Santiago Ruiz', 'Maria Jose Castro', 'Oscar Fernandez', 'Carolina Martinez', 
        'Fernando Moreno', 'Sofia Alvarez', 'Luis Fernando Lopez', 'Nicolas Vargas', 'Natalia Torres', 
        'Antonio Rodriguez', 'Carmen Ramirez', 'Julian Perez', 'Paola Ruiz', 'Eduardo Salazar', 'Viviana Sanchez', 
        'Gustavo Gonzalez', 'Juliana Romero', 'Daniela Lopez', 'Angela Torres', 'Santiago Gonzalez', 
        'Laura Martinez', 'Margarita Ramirez', 'Luis Alberto Castro', 'Fabiola Hernandez', 'Victor Soto', 
        'Manuela Diaz', 'Mauricio Vargas', 'Valeria Lopez', 'Esteban Perez', 'Eliana Fernandez', 'Carlos Alberto Ruiz', 
        'Jessica Morales', 'Andres Soto', 'Sandra Jimenez', 'Santiago Hernandez', 'Paola Gomez', 
        'Alejandra Martinez', 'Gonzalo Ramirez', 'Diana Perez', 'Oscar Jimenez', 'Marina Rodriguez', 
        'Ricardo Salazar', 'Catalina Martinez', 'Jose Miguel Fernandez', 'Paola Salazar', 'Gabriela Romero'
    ]
    
    vendedores = [
        'Carlos Ramirez', 'Sonia Diaz', 'Miguel Castro', 'Valeria Pena', 'Andres Gomez', 'Elena Rodriguez', 
        'Ricardo Martinez', 'Natalia Cruz', 'Hector Sanchez', 'Patricia Vargas', 'Juan Martinez', 'Laura Gomez', 
        'Mario Rodriguez', 'Isabel Herrera', 'Luis Castro', 'Carmen Martinez', 'Fernando Reyes', 'Sandra Medina', 
        'Javier Gonzalez', 'Adriana Ruiz', 'Oscar Soto', 'Margarita Rivas', 'David Castro', 'Carolina Rodriguez', 
        'Santiago Vega', 'Paola Morales', 'Gabriel Lopez', 'Claudia Salazar', 'Esteban Jimenez', 'Laura Fernandez', 
        'Sergio Castro', 'Monica Soto', 'Rafael Martinez', 'Nadia Lopez', 'Antonio Sanchez', 'Fabiola Fernandez', 
        'Gustavo Salazar', 'Julia Romero', 'Victor Gonzalez', 'Carmen Garcia', 'Julian Vargas', 'Daniela Jimenez', 
        'Emanuel Ramirez', 'Mariana Herrera', 'Luis Felipe Castro', 'Gabriela Gonzalez', 'Andres Sanchez', 
        'Diana Morales', 'Carlos Andres Perez', 'Ana Vargas', 'Luis Fernando Vega', 'Sofia Lopez', 'Alejandra Gonzalez', 
        'Alejandro Martinez', 'Viviana Torres', 'Maria Paula Jimenez', 'Santiago Morales', 'Catalina Diaz', 
        'Oscar Rodriguez', 'Laura Martinez', 'Adriana Herrera', 'Luis Alberto Gomez', 'Eliana Sanchez', 
        'Viviana Vargas', 'Jessica Castro', 'Gonzalo Medina', 'Paola Jimenez', 'Javier Rodriguez', 'Valeria Gonzalez'
    ]

    ciudades = [
       # Ciudades de República Dominicana
    'Santo Domingo', 'Santiago', 'San Francisco de Macoris', 'La Vega', 'Puerto Plata', 'San Pedro de Macoris', 
    'San Cristobal', 'Moca', 'Bonao', 'La Romana', 'Higuey', 'Azua', 'Barahona', 'Cotui', 'La Altagracia', 
    'Dajabon', 'Monte Plata', 'El Seibo', 'San Juan de la Maguana', 'Jimani', 'San Jose de Ocoa', 
    'San Rafael del Yuma', 'Neiba', 'Pedernales', 'Samana', 'Las Terrenas', 'Bani', 'Jarabacoa', 'Hato Mayor', 
    'Monte Cristi', 'Santo Domingo Este', 'Santo Domingo Oeste', 'Santo Domingo Norte', 'La Isabela', 'Mao', 
    'Los Alcarrizos', 'San Luis', 
    
    # Estados de Estados Unidos
    'California', 'Texas', 'Florida', 'New York', 'Illinois', 'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina', 
    'Michigan', 'New Jersey', 'Virginia', 'Washington', 'Arizona', 'Massachusetts', 'Tennessee', 'Indiana', 
    'Missouri', 'Maryland', 'Wisconsin', 'Colorado', 'Minnesota', 'South Carolina', 'Alabama', 'Louisiana', 
    'Kentucky', 'Oregon', 'Oklahoma', 'Connecticut', 'Utah', 'Iowa', 'Nevada', 'Arkansas', 'Mississippi', 
    'Kansas', 'New Mexico', 'Nebraska', 'West Virginia', 'Idaho', 'Hawaii', 'Maine', 'Montana', 'Rhode Island', 
    'Delaware', 'South Dakota', 'North Dakota', 'Alaska', 'Vermont', 'Wyoming',
    
    # Ciudades de Francia
    'Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux', 'Lille', 
    'Rennes', 'Reims', 'Le Havre', 'Saint-Etienne', 'Toulon', 'Grenoble', 'Dijon', 'Angers', 'Nimes', 'Villeurbanne',

    # Ciudades de otros países
    'Londres', 'Berlin', 'Madrid', 'Roma', 'Ámsterdam', 'Bruselas', 'Lisboa', 'Atenas', 'Viena', 'Estocolmo', 
    'Oslo', 'Helsinki', 'Copenhague', 'Dublín', 'Zurich', 'Moscú', 'Tokio', 'Pekín', 'Nueva Delhi', 'Sídney', 
    'Toronto', 'Vancouver', 'Buenos Aires', 'Sao Paulo', 'Ciudad de México', 'Bogotá', 'Lima', 'Santiago', 
    'Caracas', 'Quito', 'La Paz', 'Montevideo'
    ][:num_cities]
    condiciones_pago = ['creito', 'contado', 'efectivo', 'tarjeta', 'transferencia', 'bitcoin']

    data = []

    for _ in range(num_records):
        date = fake.date_between(start_date=start_date, end_date=end_date)
        cantidad = fake.random_int(min=1, max=100)
        producto, unidad, categoria = random.choice(productos)  # Se añade la categoría al seleccionar el producto
        precio = round(random.uniform(1, 500), 2)
        subtotal = round(cantidad * precio, 2)
        descuento = round(random.uniform(0, subtotal * 0.2), 2)  # Descuento hasta el 20% del subtotal
        subtotal_desc = round(subtotal - descuento, 2)
        impuesto = round(subtotal_desc * 0.18, 2)  # Impuesto del 18% del subtotal después del descuento
        total_vendido = round(subtotal_desc + impuesto, 2)

        data.append({
            'Codigo_Cliente': random.choice(range(1000, 9999)),
            'Fecha_Pedido': date,
            'Ciudad': random.choice(ciudades),
            'Vendedor': random.choice(vendedores),
            'Numero_Pedido': fake.uuid4(),
            'Condicion_Pago': random.choice(condiciones_pago),
            'Cliente': random.choice(clientes),
            'Descripcion': producto,
            'Unidad': unidad,
            'Categoria': categoria,  # Se agrega la categoría al diccionario
            'Cantidad': cantidad,
            'Precio': precio,
            'Subtotal': subtotal,
            'Descuento': descuento,
            'Subtotal_Con_Descuento': subtotal_desc,
            'Impuesto': impuesto,
            'Total_Vendido': total_vendido
        })


    return pd.DataFrame(data)
