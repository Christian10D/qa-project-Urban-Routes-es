Urban Routes – Pruebas Automatizadas
Christian Daniel Palafox Adame, Grupo 19, Sprint 8

1.- Descripción del Proyecto
Este proyecto implementa pruebas automatizadas para la plataforma Urban Routes, una aplicación de transporte que permite a los usuarios solicitar taxis y personalizar su viaje con opciones adicionales.
El objetivo de estas pruebas es garantizar la funcionalidad del proceso de solicitud de un taxi, validando cada paso clave de la experiencia del usuario.

2.- Alcance de las Pruebas
Las pruebas están diseñadas para verificar el flujo completo de solicitud de un taxi, asegurando que la aplicación responda correctamente en cada etapa.

Escenarios cubiertos:
Configuración del origen y destino del viaje.
Selección de la tarifa Comfort.
Ingreso y validación del número de teléfono mediante código de confirmación.
Adición de un método de pago con tarjeta de crédito.
Envío de un mensaje al conductor con instrucciones adicionales.
Solicitud de elementos adicionales como mantas y pañuelos.
Pedido de helado como parte del viaje.
Confirmación del pedido y asignación de un conductor.
Verificación de la aparición del modal con la información del conductor.

3.- Tecnologías y Herramientas
Este proyecto utiliza herramientas especializadas en pruebas automatizadas para la validación de aplicaciones web:
Python: Lenguaje de programación principal.
Selenium WebDriver: Framework para la automatización de pruebas en navegadores.
Pytest: Framework de testing en Python.
Chrome WebDriver: Controlador del navegador utilizado para la ejecución de pruebas.