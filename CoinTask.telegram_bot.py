import telebot
import pandas as pd
from datetime import datetime
import io
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Reemplaza con tu token real
TOKEN = 'PON AQUÍ TU TOKEN'

bot = telebot.TeleBot(TOKEN)

# Crear o cargar el DataFrame
try:
    df = pd.read_csv('actividades.csv', parse_dates=['tiempo'])
except FileNotFoundError:
    df = pd.DataFrame(columns=['Puntos', 'Actividad', 'tiempo'])

@bot.message_handler(commands=['data_vis'])
def visualizar_datos(message):
    if df.empty:
        bot.reply_to(message, "No hay datos para visualizar.")
    else:
        try:
            # Crear un archivo PDF en memoria
            buffer = io.BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []

            # Convertir DataFrame a una lista de listas
            data = [df.columns.tolist()] + df.values.tolist()

            # Crear la tabla
            t = Table(data)
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 12),
                ('TOPPADDING', (0, 1), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))

            elements.append(t)
            doc.build(elements)

            buffer.seek(0)
            
            # Enviar el archivo PDF
            bot.send_document(message.chat.id, buffer, 
                              visible_file_name='actividades.pdf',
                              caption="Aquí tienes el archivo PDF con todos los datos.")
        except Exception as e:
            bot.reply_to(message, f"Ocurrió un error al generar el PDF: {str(e)}")
@bot.message_handler(func=lambda message: True)
def manejar_mensaje(message):
    global df
    
    try:
        puntos, actividad = message.text.split(',', 1)
        puntos = int(puntos)
        actividad = actividad.strip()
        tiempo_actual = datetime.now()
        
        # Crear una nueva fila como un diccionario
        nueva_fila = {'Puntos': [puntos], 'Actividad': [actividad], 'tiempo': [tiempo_actual]}
        
        # Añadir la nueva fila al DataFrame existente
        df = pd.concat([df, pd.DataFrame(nueva_fila)], ignore_index=True)
        
        # Guardar el DataFrame actualizado
        df.to_csv('actividades.csv', index=False)
        
        # Calcular la suma total
        total = df['Puntos'].sum()
        
        # Enviar respuesta
        respuesta = f"✅ Operación realizada con éxito!\nPuntos restantes: **{total}**"
        bot.reply_to(message, respuesta)
    except ValueError:
        bot.reply_to(message, "Formato incorrecto. Usa: número, actividad")
    except Exception as e:
        bot.reply_to(message, f"Ocurrió un error: {str(e)}")

# Iniciar el bot
bot.polling()
