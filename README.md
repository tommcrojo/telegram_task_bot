# 🚀 Telegram Task Tracker Bot: Tu Compañero de Productividad

Imagina tener un asistente personal que no solo te ayuda a gestionar tus tareas diarias, sino que también te motiva con recompensas por cada logro que alcanzas. ¡Eso es exactamente lo que este bot de Telegram puede hacer por ti!

## 🌟 La Idea Detrás del Bot

En un mundo lleno de distracciones y múltiples tareas, mantenerse organizado y motivado puede ser un desafío. 

#### ¿Qué tal si, además de registrar tus logros, te motivaras con puntos que puedes canjear por recompensas? 
Eso es lo que me inspiró a crear este bot. 
Quería una herramienta que no solo me ayudara a llevar un registro de mis tareas, sino que también me diera un incentivo para seguir adelante. 

## 🛠️ Tecnologías Utilizadas

Para construir este bot, combiné algunas de las herramientas más poderosas del ecosistema Python:

- **Python**: El lenguaje versátil que me permitió desarrollar un bot robusto y eficiente.
- **pandas**: Para manejar y analizar datos de manera efectiva.
- **telebot**: La biblioteca que me permitió interactuar con la API de Telegram de manera sencilla.
- **reportlab**: Para convertir esos datos en informes PDF claros y atractivos.

## 🚀 Funcionalidades

- **Registro de Tareas**: Simplemente envía un mensaje con el formato `puntos, actividad` y tu tarea se registrará al instante. Cada tarea te otorga puntos que suman en tu total general.
- **Visualización de Datos**: Usa el comando `/data_vis` para recibir un archivo PDF con una visualización detallada de todas tus actividades. ¡Perfecto para ver tu progreso y motivarte!

## 💡 Cómo Empezar

1. **Clonar el Repositorio**:
   Abre tu terminal y clona el repositorio con el siguiente comando:
   ```bash
   git clone https://github.com/tu_usuario/telegram-task-tracker-bot.git
   cd telegram-task-tracker-bot
   ```
2. **Instalar Dependencias:**
Asegúrate de tener un entorno virtual activado (opcional pero recomendado). Luego, instala las librerías necesarias:
```bash
pip install telebot pandas reportlab
```

3. **Configurar el Bot:**
Obtén el token de tu bot de Telegram y reemplaza el valor en el script bot.py:
```python
TOKEN = 'TU_TOKEN_AQUI'
```

4. **Ejecutar el Bot:**
Inicia el bot con:
```bash
CoinTask.telegram_bot.py
```



---
## 📝 Cómo Usar el Bot
Registrar una Tarea: Envía un mensaje al bot con el formato puntos, actividad. Por ejemplo:

´´´bash
10, Estudiar Python
´´´

Ver Datos: Envía el comando /data_vis para recibir un PDF con un resumen visual de tus actividades y puntos acumulados.



---
## 🚀 Un Ejemplo en Acción

![image](https://github.com/user-attachments/assets/b1457305-be55-4e0f-b203-beb4324a45cc)

---
## 📬 Contacto
Si tienes preguntas, comentarios, o solo quieres charlar, no dudes en contactarme a través de GitHub o por correo electrónico. ¡Estoy siempre dispuesto a ayudar!

