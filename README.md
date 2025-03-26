# Gaming Night WhatsApp Bot 🎮
# Bot de Noche de Juegos para WhatsApp 🎮

## Español

### Descripción General
Este bot de WhatsApp ayuda a coordinar noches de CONTER mediante un sistema de encuestas diarias con un mecanismo de seguimiento de asistencia basado en puntos. Fomenta la participación constante mediante recompensas y penalizaciones.

### Cómo Funciona

#### Horario Diario (Hora Argentina - ART)
- 20:00 (8 PM) - Se envía la encuesta diaria al grupo
- 21:00 (9 PM) - Se verifica el estado del juego
- 22:00 (10 PM) - Hora de juego
- 23:59 (11:59 PM) - Se actualizan los puntos según la participación

#### Sistema de Puntos
- **Puntos Iniciales**: Cada nuevo miembro comienza con 100 puntos
- **Penalizaciones**:
  - No responder a la encuesta: -10 puntos
  - Decir "no" a la noche de juegos: -5 puntos
  - Cancelación tardía (dentro de 1 hora): -15 puntos
- **Recompensas**:
  - Asistir a una noche de juegos: +3 puntos
  - Límite máximo de puntos: 100 puntos

#### Sistema de Eliminación
- Cuando los puntos de un jugador llegan a 0, se crea una encuesta de eliminación
- Los jugadores activos votan para decidir si el jugador debe permanecer en el grupo
- Los puntos se pueden recuperar mediante asistencia constante

### Requisitos de Configuración
1. Credenciales de WhatsApp Business API
2. Python 3.7+
3. Paquetes requeridos: 
   ```
   pip install schedule whatsapp-api-client-python
   ```
4. Configurar el bot editando `config.py`:
   - Agregar tu número de WhatsApp
   - Agregar tu clave API
   - Agregar el ID del grupo

### Ejecutar el Bot
```
python bot.py
```

---

## Configuration Example / Ejemplo de Configuración
```python
# config.py
WHATSAPP_CONFIG = {
    "PHONE_NUMBER": "+1234567890",
    "API_KEY": "your-api-key-here",
    "GROUP_ID": "group-id-here"
}
```

---


## English

### Overview
This WhatsApp bot helps coordinate gaming nights by managing a daily poll system with a point-based attendance tracking mechanism. It encourages consistent participation through rewards and penalties.

### How It Works

#### Daily Schedule (Argentina Time - ART)
- 20:00 (8 PM) - Daily poll is sent to the group
- 21:00 (9 PM) - Game status is checked
- 22:00 (10 PM) - Game time
- 23:59 (11:59 PM) - Points are updated based on participation

#### Point System
- **Initial Points**: Every new member starts with 100 points
- **Penalties**:
  - Not responding to poll: -10 points
  - Saying "no" to gaming night: -5 points
  - Late cancellation (within 1 hour of game time): -15 points
- **Rewards**:
  - Attending a game night: +3 points
  - Maximum points cap: 100 points

#### Elimination System
- When a player's points reach 0, an elimination poll is created
- Active players vote to decide if the player should remain in the group
- Points can be recovered through consistent attendance

### Setup Requirements
1. WhatsApp Business API credentials
2. Python 3.7+
3. Required packages: 
   ```
   pip install schedule whatsapp-api-client-python
   ```
4. Configure the bot by editing `config.py`:
   - Add your WhatsApp phone number
   - Add your API key
   - Add your group ID

### Running the Bot
```
python bot.py
```

---