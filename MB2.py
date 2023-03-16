from AssistantClass import Assistant

name = ["madbone", 'bone', 'mad', 'boom'] # Formas de llamar al asistente
sensibilidad = 4000 # Milisegundos
mb = Assistant(name, sensibilidad)

mb.runAssistant(manual=True)