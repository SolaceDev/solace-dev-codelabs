author: MrPoncho30
summary: "Chat/Messaging App Light and Dark Theme"
id: reportCodelabs
tags: Flutter, App Móvil, Chat, Message
categories: 
environments: Web
status: Published
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/reportCodelabs

# Chat/Messaging App Light and Dark Theme

## Creación de un proyecto Flutter con Dart
Aquí tienes una guía paso a paso para instalar Flutter y crear un proyecto básico:

### 1. Instalar Flutter

1. **Descargar Flutter**:
   - Si aún no tienes Flutter instalado, ve a [flutter.dev](https://flutter.dev) y descarga el SDK de Flutter para tu sistema operativo (Windows, macOS o Linux).
   - Sigue las instrucciones específicas para tu sistema operativo, las cuales incluyen la configuración de las variables de entorno necesarias. Asegúrate de que el comando `flutter` esté disponible en la línea de comandos después de la instalación.

---

### 2. Crear un Nuevo Proyecto Flutter

1. **Abrir Terminal/Comando**:
   - Abre la terminal (en macOS/Linux) o la línea de comandos (en Windows) en tu sistema.

2. **Ejecutar el Comando de Flutter**:
   - Ejecuta el siguiente comando para crear un nuevo proyecto Flutter:
   
     ```bash
     flutter create my_project
     ```

   - **Nota**: Reemplaza `my_project` con el nombre que prefieras para tu proyecto. Esto creará una estructura básica para tu aplicación Flutter.

---

### 3. Acceder al Proyecto

Una vez creado el proyecto, navega dentro de la carpeta del proyecto con el siguiente comando:

```bash
cd my_project
```

---

### 4. Explorar la Estructura del Proyecto

El proyecto creado tendrá la siguiente estructura básica:

- **`lib/`**: Carpeta principal donde escribirás el código Dart de tu aplicación.
  - **`main.dart`**: Este es el archivo de entrada principal de tu aplicación. Aquí es donde se inicializa la aplicación Flutter.
  
- **`test/`**: Carpeta para escribir pruebas unitarias para tu aplicación.
  
- **`pubspec.yaml`**: Este es el archivo de configuración de tu proyecto. Aquí defines las dependencias que tu proyecto usará, como paquetes y bibliotecas externas.

---

Con estos pasos, ya habrás instalado Flutter, creado un proyecto y explorado su estructura básica. Ahora estás listo para comenzar a desarrollar tu aplicación Flutter.

## Incluir los componentes en el **pubspec.yaml**

El archivo **pubspec.yaml** es un componente esencial en cualquier proyecto de Flutter. Este archivo se utiliza para definir dependencias, configuraciones del entorno de desarrollo y recursos adicionales como imágenes y fuentes. A continuación, se desglosan y explican cada una de las secciones presentes en este archivo.

### Información general del proyecto

```yaml
name: chat 
description: A new Flutter project. 
publish_to: "none"
```

- **name**: Define el nombre del proyecto. Aquí, el nombre es `chat`, que es utilizado por Flutter y el entorno de desarrollo para identificar el proyecto.  
- **description**: Proporciona una descripción breve del propósito del proyecto. En este caso, es simplemente un proyecto de Flutter sin una descripción extendida.  
- **publish_to**: Este campo especifica si el paquete se va a publicar en pub.dev. `"none"` significa que no se publicará en un registro de paquetes externo.

### Configuración del entorno de desarrollo

```yaml
environment:
  sdk: ">=3.5.0 <4.0.0"
```

- **environment**: Configura el rango de versiones del SDK de Dart que es compatible con este proyecto. Aquí se especifica que la versión de Dart debe ser al menos la 3.5.0, pero menor a la 4.0.0.

### Dependencias del proyecto

Las dependencias son bibliotecas o paquetes adicionales que se integran en el proyecto para proporcionar funcionalidades específicas.

```yaml
dependencies:
  flutter: 
    sdk: flutter 
  cupertino_icons: ^1.0.8 
  google_fonts: ^6.2.1 
  flutter_svg: ^2.0.10
```

- **flutter**: Es la dependencia base necesaria para todos los proyectos Flutter. Permite que el proyecto utilice el framework de Flutter.  
- **cupertino_icons**: Proporciona un conjunto de iconos prediseñados de estilo iOS. La versión especificada, `^1.0.8`, garantiza que se usen versiones compatibles.  
- **google_fonts**: Paquete que permite integrar y utilizar fuentes de Google en la aplicación. La versión `^6.2.1` se utiliza para asegurar compatibilidad y estabilidad.  
- **flutter_svg**: Paquete que permite mostrar imágenes SVG. Esto es útil para gráficos vectoriales escalables. La versión `^2.0.10` asegura compatibilidad y soporte para las últimas funcionalidades.

### Dependencias del desarrollo

Las dependencias de desarrollo son paquetes necesarios durante el desarrollo y las pruebas, pero no se incluyen en la versión final de la aplicación.

```yaml
dev_dependencies: 
  flutter_test: 
    sdk: flutter 
  flutter_lints: ^4.0.0
```

- **flutter_test**: Se utiliza para realizar pruebas unitarias y de integración en Flutter. Permite asegurarse de que el código funcione como se espera.  
- **flutter_lints**: Proporciona un conjunto de reglas de linting (análisis de código) para ayudar a mantener la calidad y la consistencia del código. La versión `^4.0.0` incluye las mejores prácticas actualizadas.

### Configuración de Flutter

Esta sección se utiliza para definir configuraciones específicas relacionadas con Flutter, como el uso de Material Design y la inclusión de recursos personalizados.

```yaml
flutter: 
  uses-material-design: true 
  assets: 
    - assets/images/ 
    - assets/icons/
```

- **uses-material-design**: Esta línea habilita el uso de los iconos de Material Design en la aplicación, lo cual es importante si se siguen las guías de diseño de Google.  
- **assets**: Se usa para incluir recursos personalizados, como imágenes y iconos. Las rutas especificadas (`assets/images/` y `assets/icons/`) indican las carpetas donde se almacenan estos recursos. Es importante asegurarse de que los nombres de las carpetas sean correctos y que contengan los archivos necesarios.

### Nota
Asegúrate de mantener este archivo actualizado con las versiones correctas de las dependencias y de incluir todos los recursos que la aplicación necesita para funcionar correctamente. Un manejo adecuado de este archivo contribuye a la estabilidad y funcionalidad del proyecto.

---

## Creación de código "FillOutlineButtom"

El archivo contiene una clase llamada `FillOutlineButton` que crea un botón estilizado con opciones para ser completamente relleno o solo con un contorno. Este widget es un ejemplo de cómo personalizar un botón en Flutter utilizando propiedades y estilos específicos. Este archivo debe ser ubicado dentro de una carpeta llamada `components` en el directorio `lib`.

### 1. Importación de paquetes y constantes

```dart
import 'package:flutter/material.dart'; 
import '../constants.dart';
```

- `import 'package:flutter/material.dart';`: Importa la biblioteca principal de Flutter, que proporciona los widgets y herramientas esenciales para el diseño de la interfaz de usuario.
- `import '../constants.dart';`: Importa un archivo de constantes personalizadas, que probablemente contiene valores reutilizables como colores y otras configuraciones de la aplicación.

### 2. Descripción de la clase `FillOutlineButton`

```dart
class FillOutlineButton extends StatelessWidget {
```

- `FillOutlineButton`: Es un widget personalizado que extiende `StatelessWidget`. Esto significa que el botón no mantiene ningún estado interno y su apariencia depende solo de las propiedades proporcionadas.

### 3. Constructor de la clase

```dart
const FillOutlineButton({ 
  super.key, 
  this.isFilled = true, 
  required this.press, 
  required this.text, 
});
```

- `super.key`: Pasa la clave al constructor de la clase base (`StatelessWidget`). Es útil para manejar el estado del widget en el árbol de widgets.
- `isFilled`: Un booleano que determina si el botón debe estar completamente relleno o solo con un contorno. Por defecto es `true`.
- `press`: Una función de callback que se ejecuta cuando se presiona el botón. Es de tipo `VoidCallback`, lo que significa que no tiene valor de retorno.
- `text`: El texto que se muestra en el botón. Es obligatorio.

### 4. Método `build`

```dart
@override 
Widget build(BuildContext context) {
```

El método `build` crea y devuelve el diseño del botón.

### 5. Estructura del botón

```dart
return MaterialButton(
  shape: RoundedRectangleBorder(
    borderRadius: BorderRadius.circular(30),
    side: const BorderSide(color: Colors.white),
  ),
  elevation: isFilled ? 2 : 0,
  color: isFilled ? Colors.white : Colors.transparent,
  onPressed: press,
  child: Text(
    text,
    style: TextStyle(
      color: isFilled ? kContentColorLightTheme : Colors.white,
      fontSize: 12,
    ),
  ),
);
```

- `MaterialButton`: Crea un botón material con varias propiedades personalizables.
- `shape`: Define la forma del botón. En este caso, se utiliza `RoundedRectangleBorder` con bordes redondeados de 30 píxeles y un contorno blanco.
- `elevation`: Controla la sombra debajo del botón. Si `isFilled` es `true`, la elevación es 2; si no, es 0, lo que da un efecto de botón plano.
- `color`: Define el color de fondo del botón. Si `isFilled` es `true`, el fondo es blanco; si no, es transparente.
- `onPressed`: Define la acción que se ejecuta cuando el botón es presionado, utilizando el callback `press`.
- `child`: El contenido del botón. En este caso, un `Text` que muestra el texto proporcionado.
- `style`: Define el estilo del texto, como el color y el tamaño de la fuente. Si `isFilled` es `true`, el color del texto se establece como `kContentColorLightTheme`; si no, es blanco.

### 6. Uso y personalización

Este widget es útil cuando necesitas botones que puedan cambiar entre un estilo relleno y uno transparente con borde.

Ejemplo de uso:

```dart
FillOutlineButton(
  isFilled: false,
  press: () {
    print('Botón presionado');
  },
  text: 'Mi Botón',
)
```

En este ejemplo, el botón tiene un contorno sin relleno y ejecuta una función que imprime un mensaje en la consola cuando se presiona.

### 7. Propiedades de la clase `FillOutlineButton`

- `final bool isFilled;`: Determina si el botón está relleno o solo con un contorno. Valor por defecto: `true`.
- `final VoidCallback press;`: Función de callback que se ejecuta cuando se presiona el botón.
- `final String text;`: El texto que se muestra dentro del botón.

**Descripción de las propiedades:**

- **isFilled**:
  - Tipo: `bool`
  - Descripción: Si `true`, el botón está relleno; si `false`, el botón solo tiene contorno.
  - Valor por defecto: `true`.
  
- **press**:
  - Tipo: `VoidCallback`
  - Descripción: Función que se ejecuta cuando el botón es presionado. No toma parámetros ni retorna valor.

- **text**:
  - Tipo: `String`
  - Descripción: El texto que aparece dentro del botón.

Este widget permite crear botones flexibles y personalizables para diversas interfaces de usuario en Flutter.

--- 

## Creación del código "PrimaryButtom"

### 1. **Importación de paquetes y constantes**

```dart
import 'package:flutter/material.dart';
import '../constants.dart';
```

- **`import 'package:flutter/material.dart';`**: Importa la biblioteca principal de Flutter, que proporciona todos los widgets y herramientas esenciales para el diseño de la interfaz de usuario.
- **`import '../constants.dart';`**: Importa un archivo de constantes personalizado. Este archivo probablemente contiene valores reutilizables como colores, padding, o cualquier otro valor constante utilizado en toda la aplicación.

---

### 2. **Descripción de la Clase PrimaryButton**

```dart
class PrimaryButton extends StatelessWidget {
```

- **`PrimaryButton`**: Es un widget personalizado que extiende de `StatelessWidget`, lo que significa que su apariencia depende de las propiedades proporcionadas y no mantiene un estado interno mutable.

---

### 3. **Constructor de la clase**

```dart
const PrimaryButton({
  super.key,
  required this.text,
  required this.press,
  this.color = kPrimaryColor,
  this.padding = const EdgeInsets.all(kDefaultPadding * 0.75),
});
```

- **`super.key`**: Se utiliza para pasar la clave al constructor de la clase base (`StatelessWidget`), útil para identificar el widget en el árbol de widgets.
- **`text`**: Es un `String` obligatorio que representa el texto que se muestra en el botón.
- **`press`**: Es una función de tipo `VoidCallback` que se ejecuta cuando el botón es presionado. También es obligatorio.
- **`color`**: Define el color de fondo del botón. Es opcional y tiene un valor por defecto (`kPrimaryColor`) que está definido en el archivo `constants.dart`.
- **`padding`**: Define el espacio interno (padding) del botón. Es opcional y tiene un valor por defecto que se basa en `kDefaultPadding` de `constants.dart`.

---

### 4. **Propiedades**

```dart
final String text;
final VoidCallback press;
final Color color;
final EdgeInsets padding;
```

- **`text`**: El texto que se muestra en el botón. (Tipo: `String`, Obligatorio).
- **`press`**: La función de callback que se ejecuta cuando se presiona el botón. (Tipo: `VoidCallback`, Obligatorio).
- **`color`**: El color de fondo del botón. (Tipo: `Color`, Opcional, con un valor por defecto de `kPrimaryColor`).
- **`padding`**: El padding o espacio interno del botón. (Tipo: `EdgeInsets`, Opcional, con un valor por defecto de `EdgeInsets.all(kDefaultPadding * 0.75)`).

---

### 5. **Método `build`**

```dart
@override
Widget build(BuildContext context) {
  return MaterialButton(
    shape: const RoundedRectangleBorder(
      borderRadius: BorderRadius.all(Radius.circular(40)),
    ),
    padding: padding,
    color: color,
    minWidth: double.infinity,
    onPressed: press,
    child: Text(
      text,
      style: const TextStyle(color: Colors.white),
    ),
  );
}
```

- **`build`**: Este método es responsable de construir el widget y devolver el diseño del botón.
- **`MaterialButton`**: El widget básico para el botón, que sigue las directrices de Material Design y permite personalización en diversos aspectos.
  - **`shape`**: Define la forma del botón. Se utiliza `RoundedRectangleBorder` con un radio de 40 píxeles para redondear las esquinas del botón.
  - **`padding`**: Se establece según la propiedad `padding` proporcionada al widget.
  - **`color`**: Establece el color de fondo del botón, basado en la propiedad `color`.
  - **`minWidth`**: Hace que el botón ocupe todo el ancho disponible (`double.infinity`).
  - **`onPressed`**: La acción que se ejecuta cuando se presiona el botón, usando el callback `press`.
  - **`child`**: El contenido del botón, en este caso un widget `Text` que muestra el texto con un estilo de fuente blanca.

---

### 6. **Uso y personalización**

Este widget es ideal para crear botones con un diseño uniforme en toda la aplicación, manteniendo la consistencia en cuanto a estilo, color y espaciado.

Ejemplo de uso:

```dart
PrimaryButton(
  text: 'Enviar',
  press: () {
    print('Botón Enviar presionado');
  },
)
```

- En este ejemplo, el botón tiene el texto **"Enviar"** y ejecutará una función que imprime un mensaje en la consola cuando se presiona.

---

Con este diseño, el `PrimaryButton` es un botón personalizado que se puede reutilizar en toda la aplicación, proporcionando consistencia visual y funcional.

## Creación del código "Chat"

Para crear el archivo `chat.dart` que contiene la clase `Chat` y la lista de chats simulados, sigue estos pasos:

1. Crea una carpeta llamada `models` dentro de la carpeta `lib`.
2. Dentro de la carpeta `models`, crea un archivo llamado `chat.dart`.

El contenido de `chat.dart` será el siguiente:

```dart
// chat.dart
class Chat {
  final String name;       // Nombre del contacto
  final String lastMessage; // Último mensaje enviado o recibido
  final String image;      // Ruta de la imagen del contacto
  final String time;       // Hora del último mensaje
  final bool isActive;     // Estado del contacto (activo o inactivo)

  // Constructor de la clase Chat
  Chat({
    this.name = '',        // Nombre predeterminado vacío
    this.lastMessage = '', // Último mensaje predeterminado vacío
    this.image = '',       // Imagen predeterminada vacía
    this.time = '',        // Hora predeterminada vacía
    this.isActive = false, // Estado predeterminado: inactivo
  });
}

// Lista de datos de ejemplo con chats simulados
List<Chat> chatsData = [
  Chat(
    name: "Jenny Wilson",      // Nombre del contacto
    lastMessage: "Hope you are doing well...", // Último mensaje
    image: "assets/images/user.png",          // Ruta de la imagen
    time: "3m ago",            // Tiempo transcurrido desde el último mensaje
    isActive: false,           // Contacto inactivo
  ),
  Chat(
    name: "Esther Howard", 
    lastMessage: "Hello Abdullah! I am...", 
    image: "assets/images/user_2.png", 
    time: "8m ago", 
    isActive: true, 
  ),
  Chat(
    name: "Ralph Edwards", 
    lastMessage: "Do you have an update on the project?", 
    image: "assets/images/user_3.png", 
    time: "5d ago", 
    isActive: false, 
  ),
  Chat(
    name: "Alice Johnson", 
    lastMessage: "Let's meet tomorrow morning!", 
    image: "assets/images/user_4.png", 
    time: "1h ago", 
    isActive: true, 
  ),
  // Agrega más chats simulados según sea necesario.
];
```

### Explicación del Código:

1. **Clase `Chat`**:
   - Define las propiedades de un chat individual como `name`, `lastMessage`, `image`, `time` y `isActive`.
   - El constructor permite inicializar estas propiedades, con valores predeterminados si no se proporcionan explícitamente.

2. **Lista `chatsData`**:
   - Contiene varios objetos de la clase `Chat`, representando conversaciones con contactos simulados. Cada `Chat` tiene información sobre el contacto, el último mensaje, la imagen, la hora y si el contacto está activo o no.

### ¿Cómo usar esta clase y lista?

En otras partes de tu aplicación, puedes usar `chatsData` para mostrar una lista de chats. Por ejemplo, puedes usar un `ListView` en tu interfaz de usuario para mostrar cada chat con su nombre, último mensaje, imagen y hora.

```dart
ListView.builder(
  itemCount: chatsData.length,
  itemBuilder: (context, index) {
    final chat = chatsData[index];
    return ListTile(
      leading: CircleAvatar(
        backgroundImage: AssetImage(chat.image),
      ),
      title: Text(chat.name),
      subtitle: Text(chat.lastMessage),
      trailing: Text(chat.time),
      tileColor: chat.isActive ? Colors.green[100] : Colors.white,
      onTap: () {
        // Acción cuando se toca el chat, por ejemplo, navegar a la pantalla de conversación.
      },
    );
  },
)
```

### Siguiente paso:

- Puedes agregar este archivo `chat.dart` dentro de la estructura de tu proyecto y utilizarlo para mostrar chats simulados o integrarlo en una funcionalidad más avanzada, como la creación de una lista de chats en una aplicación de mensajería.

## Creación del código "ChatMessage"

Para crear el archivo `chat_message.dart` con la clase `ChatMessage`, los enumeradores `ChatMessageType` y `MessageStatus`, y la lista de mensajes simulados, sigue estos pasos:

1. Asegúrate de que el archivo `chat_message.dart` esté ubicado en la misma carpeta `models` donde se encuentra el archivo `chat.dart`.

El contenido de `chat_message.dart` será el siguiente:

```dart
// chat_message.dart

// Enumerador para los tipos de mensaje
enum ChatMessageType {
  text,   // Mensaje de texto
  audio,  // Mensaje de audio
  image,  // Mensaje con imagen
  video   // Mensaje con video
}

// Enumerador para el estado del mensaje
enum MessageStatus {
  notSent,  // El mensaje no ha sido enviado
  notView,  // El mensaje no ha sido visto
  viewed    // El mensaje ha sido visto
}

// Clase que modela un mensaje de chat
class ChatMessage {
  final String text;               // Texto del mensaje
  final ChatMessageType messageType; // Tipo de mensaje (texto, audio, imagen, video)
  final MessageStatus messageStatus; // Estado del mensaje (no enviado, no visto, visto)
  final bool isSender;              // Indica si el mensaje fue enviado por el usuario actual

  // Constructor de la clase ChatMessage
  ChatMessage({
    this.text = '',              // Texto del mensaje, predeterminado vacío
    required this.messageType,   // Tipo de mensaje, obligatorio
    required this.messageStatus, // Estado del mensaje, obligatorio
    required this.isSender,      // Si el mensaje fue enviado por el usuario, obligatorio
  });
}

// Lista de mensajes de ejemplo
List<ChatMessage> demeChatMessages = [
  ChatMessage(
    text: "Hi Lee,",                      // Mensaje de texto
    messageType: ChatMessageType.text,     // Tipo de mensaje: texto
    messageStatus: MessageStatus.viewed,   // Estado del mensaje: visto
    isSender: false,                       // No fue enviado por el usuario actual
  ),
  ChatMessage(
    text: "Hello, How are you?",          // Mensaje de texto
    messageType: ChatMessageType.text,     // Tipo de mensaje: texto
    messageStatus: MessageStatus.viewed,   // Estado del mensaje: visto
    isSender: true,                        // Fue enviado por el usuario actual
  ),
  ChatMessage(
    text: "",                             // Mensaje de audio (sin texto)
    messageType: ChatMessageType.audio,    // Tipo de mensaje: audio
    messageStatus: MessageStatus.viewed,   // Estado del mensaje: visto
    isSender: false,                       // No fue enviado por el usuario actual
  ),
  ChatMessage(
    text: "",                             // Mensaje de video (sin texto)
    messageType: ChatMessageType.video,    // Tipo de mensaje: video
    messageStatus: MessageStatus.viewed,   // Estado del mensaje: visto
    isSender: true,                        // Fue enviado por el usuario actual
  ),
  ChatMessage(
    text: "Error happened",               // Mensaje de texto con error
    messageType: ChatMessageType.text,     // Tipo de mensaje: texto
    messageStatus: MessageStatus.notSent,  // Estado del mensaje: no enviado
    isSender: true,                        // Fue enviado por el usuario actual
  ),
];
```

### Explicación del Código:

1. **Enumeradores `ChatMessageType` y `MessageStatus`**:
   - `ChatMessageType` define los posibles tipos de mensajes: `text`, `audio`, `image`, y `video`.
   - `MessageStatus` define el estado de un mensaje: `notSent` (no enviado), `notView` (no visto), y `viewed` (visto).

2. **Clase `ChatMessage`**:
   - La clase `ChatMessage` tiene propiedades que definen un mensaje de chat: `text` (contenido del mensaje), `messageType` (tipo de mensaje), `messageStatus` (estado del mensaje), y `isSender` (indica si el mensaje fue enviado por el usuario actual).
   - El constructor permite crear instancias de `ChatMessage` con los valores proporcionados.

3. **Lista `demeChatMessages`**:
   - Contiene ejemplos de mensajes de chat, representando diferentes tipos de mensajes (texto, audio, video) y su respectivo estado (enviado, no enviado, visto).
   - Esta lista es útil para realizar pruebas de la funcionalidad de mensajes en una aplicación de chat.

### ¿Cómo usar estas clases?

En otros lugares de tu aplicación, puedes utilizar la lista `demeChatMessages` para mostrar los mensajes. Por ejemplo, en un `ListView` para representar una conversación:

```dart
ListView.builder(
  itemCount: demeChatMessages.length,
  itemBuilder: (context, index) {
    final message = demeChatMessages[index];
    return ListTile(
      title: Text(message.text),
      subtitle: Text(message.messageStatus.toString().split('.').last),
      leading: Icon(message.isSender ? Icons.send : Icons.receive),
      trailing: Icon(
        message.messageType == ChatMessageType.text
            ? Icons.text_fields
            : message.messageType == ChatMessageType.audio
                ? Icons.audiotrack
                : message.messageType == ChatMessageType.image
                    ? Icons.image
                    : Icons.video_call,
      ),
    );
  },
)
```

### Siguiente paso:
- Puedes agregar este archivo `chat_message.dart` en la misma carpeta `models` y usarlo para manejar los mensajes en tu aplicación de chat, simulando diferentes tipos de mensajes y estados.

## Creación del código "Constants"

Para crear el archivo `constants.dart`, que contiene la definición de las constantes de colores y el valor de padding, sigue estos pasos:

1. Crea un archivo llamado `constants.dart` a la misma altura que el archivo `main.dart`.
2. Añade las siguientes líneas de código:

```dart
// constants.dart

import 'package:flutter/material.dart';

// Constantes de colores temáticos

// Color principal de la aplicación (verde)
const kPrimaryColor = Color(0xFF00BF6D);

// Color secundario de la aplicación (naranja)
const kSecondaryColor = Color(0xFFFE9901);

// Color del contenido en el tema claro (gris oscuro)
const kContentColorLightTheme = Color(0xFF1D1D35);

// Color del contenido en el tema oscuro (blanco roto)
const kContentColorDarkTheme = Color(0xFFF5FCF9);

// Color utilizado para las advertencias (amarillo)
const kWarningColor = Color(0xFFF3BB1C);

// Color de error (rojo vibrante)
const kErrorColor = Color(0xFFF03738);

// Constante de padding predeterminado (espaciado)
const kDefaultPadding = 20.0;
```

### Explicación del código:

1. **Importación de la biblioteca**:
   - `import 'package:flutter/material.dart';`: Se importa la biblioteca de Flutter para tener acceso a los widgets y clases que permiten trabajar con colores y otros elementos de diseño.

2. **Constantes de colores**:
   - **`kPrimaryColor`**: Define el color principal de la aplicación, que es un tono de verde (#00BF6D).
   - **`kSecondaryColor`**: Define el color secundario de la aplicación, un tono de naranja (#FE9901).
   - **`kContentColorLightTheme`**: Define el color del contenido en el tema claro, un tono de gris oscuro (#1D1D35), que mejora la legibilidad en fondos claros.
   - **`kContentColorDarkTheme`**: Define el color del contenido en el tema oscuro, un tono de blanco roto (#F5FCF9), que proporciona buen contraste en fondos oscuros.
   - **`kWarningColor`**: Define el color de advertencia en la aplicación, un tono de amarillo (#F3BB1C), para llamar la atención del usuario en situaciones que requieren precaución.
   - **`kErrorColor`**: Define el color de error, un rojo vibrante (#F03738), utilizado para indicar problemas o errores críticos.

3. **Constante de padding**:
   - **`kDefaultPadding`**: Define un valor de padding predeterminado de 20.0 píxeles, utilizado para márgenes y espaciados en el diseño para mantener una disposición ordenada y uniforme en la interfaz.

### Uso de las constantes:

Puedes utilizar estas constantes en cualquier lugar de tu aplicación para aplicar los colores y el padding. Por ejemplo:

```dart
Container(
  padding: EdgeInsets.all(kDefaultPadding),
  color: kPrimaryColor,
  child: Text(
    'Bienvenido',
    style: TextStyle(
      color: kContentColorLightTheme,
      fontSize: 24,
    ),
  ),
)
```

### Estructura del Proyecto:

- La estructura del proyecto debe verse de la siguiente manera:
  ```
  lib/
  ├── constants.dart
  ├── main.dart
  ├── chat_message.dart
  ├── models/
  └── ...
  ```

Con esto, tendrás un archivo `constants.dart` que centraliza la gestión de colores y valores predeterminados, lo que facilita la coherencia en el diseño de toda la aplicación.

## Creación del código "Theme"

Para crear el archivo `theme.dart`, que configurará los temas claros y oscuros de la aplicación, y asegurará la coherencia visual utilizando las constantes definidas en `constants.dart`, sigue estos pasos:

1. **Crea un archivo llamado `theme.dart`** a la misma altura que los archivos `main.dart` y `constants.dart`.
2. **Añade las siguientes líneas de código** en `theme.dart`:

```dart
// theme.dart

import 'constants.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

// Tema de AppBar personalizado
const appBarTheme = AppBarTheme(
  centerTitle: false,  // Título no centrado
  elevation: 0,        // Sin sombra en el AppBar
);

// Función para el tema claro
ThemeData lightThemeData(BuildContext context) {
  return ThemeData.light().copyWith(
    primaryColor: kPrimaryColor,
    scaffoldBackgroundColor: Colors.white,  // Fondo blanco
    appBarTheme: appBarTheme,  // Tema del AppBar
    iconTheme: const IconThemeData(color: kContentColorLightTheme),  // Color de los íconos en el tema claro
    textTheme: GoogleFonts.interTextTheme(Theme.of(context).textTheme)
        .apply(bodyColor: kContentColorLightTheme),  // Fuente 'Inter' con color adecuado
    colorScheme: const ColorScheme.light(
      primary: kPrimaryColor,
      secondary: kSecondaryColor,
      error: kErrorColor,
    ),
    bottomNavigationBarTheme: BottomNavigationBarThemeData(
      backgroundColor: Colors.white,
      selectedItemColor: kContentColorLightTheme.withOpacity(0.7),
      unselectedItemColor: kContentColorLightTheme.withOpacity(0.32),
      selectedIconTheme: const IconThemeData(color: kPrimaryColor),
      showUnselectedLabels: true,
    ),
  );
}

// Función para el tema oscuro
ThemeData darkThemeData(BuildContext context) {
  return ThemeData.dark().copyWith(
    primaryColor: kPrimaryColor,
    scaffoldBackgroundColor: kContentColorLightTheme,  // Fondo gris oscuro para el tema oscuro
    appBarTheme: appBarTheme.copyWith(backgroundColor: kContentColorLightTheme),  // Personalización del AppBar
    iconTheme: const IconThemeData(color: kContentColorDarkTheme),  // Color de los íconos en el tema oscuro
    textTheme: GoogleFonts.interTextTheme(Theme.of(context).textTheme)
        .apply(bodyColor: kContentColorDarkTheme),  // Fuente 'Inter' con color adecuado
    colorScheme: const ColorScheme.dark().copyWith(
      primary: kPrimaryColor,
      secondary: kSecondaryColor,
      error: kErrorColor,
    ),
    bottomNavigationBarTheme: BottomNavigationBarThemeData(
      backgroundColor: kContentColorLightTheme,
      selectedItemColor: Colors.white70,
      unselectedItemColor: kContentColorDarkTheme.withOpacity(0.32),
      selectedIconTheme: const IconThemeData(color: kPrimaryColor),
      showUnselectedLabels: true,
    ),
  );
}
```

### Descripción del código:

1. **Importaciones**:
   - **`import 'constants.dart';`**: Se importa el archivo de constantes, que contiene los colores y el padding para garantizar la coherencia en el diseño.
   - **`import 'package:flutter/material.dart';`**: Se importa la biblioteca de Flutter para trabajar con los widgets y temas basados en Material Design.
   - **`import 'package:google_fonts/google_fonts.dart';`**: Se importa el paquete `google_fonts` para utilizar la fuente personalizada "Inter" en la aplicación.

2. **Tema del AppBar**:
   - **`appBarTheme`**: Se define un tema básico para el AppBar, sin sombra (`elevation: 0`) y sin centrar el título (`centerTitle: false`).

3. **Función `lightThemeData` (Tema claro)**:
   - Se usa el método `ThemeData.light()` de Flutter para crear el tema claro y se modifican varios parámetros como:
     - **`primaryColor`**: Color principal, definido en `constants.dart`.
     - **`scaffoldBackgroundColor`**: Color de fondo blanco para el `Scaffold`.
     - **`appBarTheme`**: Aplica el tema de AppBar personalizado.
     - **`iconTheme`**: Color de los íconos en el tema claro.
     - **`textTheme`**: Configura la fuente "Inter" con color adecuado para el texto en el tema claro.
     - **`colorScheme`**: Establece los colores primarios, secundarios y de error.
     - **`bottomNavigationBarTheme`**: Personaliza el tema de la barra de navegación inferior.

4. **Función `darkThemeData` (Tema oscuro)**:
   - Similar al tema claro, pero se utilizan colores oscuros para los fondos y los íconos, con los colores de `kContentColorLightTheme` y `kContentColorDarkTheme` para los contrastes.
   - Se personaliza también el color de los íconos y el tema de la barra de navegación inferior.

### Configuración en el archivo `main.dart`:

Una vez que has creado y configurado el archivo `theme.dart`, puedes aplicarlo en tu aplicación Flutter dentro del archivo `main.dart` de la siguiente manera:

```dart
import 'package:flutter/material.dart';
import 'theme.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mi App',
      theme: lightThemeData(context), // Aplicar el tema claro
      darkTheme: darkThemeData(context), // Aplicar el tema oscuro
      themeMode: ThemeMode.system, // El tema se ajusta automáticamente según la preferencia del sistema
      home: HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Bienvenido')),
      body: Center(child: Text('Contenido principal')),
    );
  }
}
```

### Explicación de cómo funciona:

- **`themeMode: ThemeMode.system`**: Esto hace que la aplicación utilice el tema claro u oscuro según la configuración del sistema operativo (iOS o Android) del dispositivo.
- Los temas definidos en `theme.dart` son aplicados a toda la aplicación, manteniendo una interfaz coherente en todos los dispositivos y asegurando que se use la tipografía y los colores correctos.

### Estructura final del proyecto:

Tu estructura de archivos debería quedar de esta manera:

```
lib/
├── constants.dart
├── theme.dart
├── main.dart
└── ...
```

Con este código, tu aplicación tendrá dos temas visuales coherentes y fáciles de mantener, garantizando que se aplique el diseño correcto tanto en el modo claro como en el oscuro.

## Configuración del código pricipal de la aplicación 

El Paso 9 describe cómo configurar el archivo principal de la aplicación en Flutter para gestionar los temas y la pantalla de inicio. A continuación se explica cada sección en detalle:

### 1. **Importaciones**
```dart
import 'screens/welcome/welcome_screen.dart';
import 'theme.dart';
import 'package:flutter/material.dart';
```
- **screens/welcome/welcome_screen.dart**: Importa la pantalla de bienvenida. Aquí se encuentra la lógica y el diseño de la pantalla inicial que el usuario ve al abrir la aplicación.
- **theme.dart**: Importa el archivo donde están definidos los temas de la aplicación (tema claro y oscuro).
- **flutter/material.dart**: Importa la biblioteca de Material Design de Flutter, proporcionando acceso a los widgets y estilos predeterminados de Flutter.

### 2. **Función principal**
```dart
void main() {
  runApp(const MyApp());
}
```
- **main()**: Es la función que se ejecuta al iniciar la aplicación. Dentro de ella, `runApp()` es llamado con el widget `MyApp`, que inicia la aplicación y gestiona la configuración de temas y la pantalla de inicio.

### 3. **Clase MyApp**
```dart
class MyApp extends StatelessWidget {
  const MyApp({super.key});
}
```
- **MyApp**: Es un widget sin estado (StatelessWidget) que define la estructura principal de la aplicación. Un `StatelessWidget` se utiliza cuando la interfaz no cambia de manera dinámica después de ser construida.
- **constructor**: `const MyApp({super.key})` inicializa la clase `MyApp`, y se pasa la clave `super.key` para identificar de manera única este widget dentro del árbol de widgets.

### 4. **Método Build**
```dart
@override
Widget build(BuildContext context) {
```
- **build()**: Este método es responsable de construir el widget de la aplicación. En este caso, se devuelve un widget `MaterialApp`, que gestiona la estructura de la aplicación y la apariencia visual.

### 5. **Configuración de MaterialApp**
```dart
return MaterialApp(
  title: 'The Flutter Way',
  debugShowCheckedModeBanner: false,
  theme: lightThemeData(context),
  darkTheme: darkThemeData(context),
  themeMode: ThemeMode.light,
  home: const WelcomeScreen(),
);
```
- **title**: Establece el título de la aplicación, que se mostrará en la barra de tareas de dispositivos que lo soporten.
- **debugShowCheckedModeBanner**: Establece `false` para ocultar la etiqueta de depuración que aparece en el modo de desarrollo.
- **theme**: Se aplica el tema claro usando la función `lightThemeData(context)` definida en el archivo `theme.dart`.
- **darkTheme**: Se aplica el tema oscuro usando la función `darkThemeData(context)` también definida en `theme.dart`.
- **themeMode**: Establece el modo de tema predeterminado. En este caso, se usa `ThemeMode.light` para indicar que el tema claro será el predeterminado.
- **home**: Define la pantalla de inicio, que es la `WelcomeScreen`. Esta pantalla se mostrará al abrir la aplicación.

### Resumen
Este archivo principal se encarga de inicializar la aplicación, aplicar los temas y mostrar la pantalla de bienvenida cuando el usuario inicia la app. El uso de temas claros y oscuros proporciona una experiencia consistente y personalizada para el usuario, mientras que la estructura modular permite extender fácilmente la aplicación.

## Creación del código "WelcomeScreen"

### **1. Importaciones**

En esta sección, importamos las bibliotecas y archivos necesarios para el funcionamiento de la pantalla de bienvenida.

```dart
import '../../constants.dart'; 
import '../signinOrSignUp/signin_or_signup_screen.dart';
import 'package:flutter/material.dart';
```

#### Descripción:
- **`../../constants.dart`**: Importa las constantes definidas en el archivo `constants.dart`, como colores, márgenes, y otros valores reutilizables.
- **`../signinOrSignUp/signin_or_signup_screen.dart`**: Importa la pantalla de inicio de sesión o registro, `SigninOrSignupScreen`, a la que navegaremos cuando el usuario decida continuar.
- **`flutter/material.dart`**: Importa la biblioteca principal de Flutter para utilizar widgets y estilos de diseño basados en Material Design.

---

### **2. Clase `WelcomeScreen`**

La clase `WelcomeScreen` es un widget sin estado (StatelessWidget), lo que significa que no mantiene ningún estado interno y se reconstruye cada vez que se necesita.

```dart
class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({super.key});
}
```

#### Descripción:
- **`WelcomeScreen`**: Esta clase es responsable de construir la interfaz de la pantalla de bienvenida.
- **`super.key`**: Permite identificar el widget en el árbol de widgets, aunque no es esencial para este caso.

---

### **3. Método `build`**

El método `build` se encarga de construir y devolver el diseño de la pantalla de bienvenida. Es el punto de entrada para crear la interfaz de usuario.

```dart
@override
Widget build(BuildContext context) {
  return Scaffold(
    body: SafeArea(
      child: Column(
        children: [
          const Spacer(flex: 2),
          Image.asset("assets/images/welcome_image.png"),
          const Spacer(flex: 3),
          ...
        ],
      ),
    ),
  );
}
```

#### Descripción:
- **`Scaffold`**: Proporciona la estructura básica de la pantalla, con una área para el cuerpo principal.
- **`SafeArea`**: Asegura que el contenido no se superponga a áreas no visibles, como la barra de estado o muescas.
- **`Column`**: Organiza los elementos en una disposición vertical.
- **`Spacer(flex: 2)` y `Spacer(flex: 3)`**: Controlan el espacio entre los elementos, asegurando que la interfaz esté bien distribuida.

---

### **4. Contenido de la `Column`**

Dentro del `Column`, se incluyen varios widgets para construir la pantalla.

#### 1. **Logo o Imagen de Bienvenida**

```dart
Image.asset("assets/images/welcome_image.png")
```

- **`Image.asset`**: Carga y muestra una imagen desde los recursos locales de la aplicación.
- **Ruta**: `"assets/images/welcome_image.png"` es la ubicación de la imagen que se muestra en la pantalla de bienvenida.

#### 2. **Espaciadores**

Los espaciadores controlan la distribución del contenido, dándole un margen adecuado entre los diferentes elementos.

```dart
const Spacer(flex: 2),
const Spacer(flex: 3),
```

- **`Spacer(flex: 2)` y `Spacer(flex: 3)`**: Añaden espacios flexibles, lo que permite distribuir de manera adecuada los elementos en la pantalla.

---

### **5. Texto de Bienvenida**

Aquí se muestra un texto que da la bienvenida al usuario, utilizando un estilo centrado y en negrita.

```dart
Text(
  "Welcome to our freedom \nmessaging app",
  textAlign: TextAlign.center,
  style: Theme.of(context)
      .textTheme
      .headlineSmall!
      .copyWith(fontWeight: FontWeight.bold),
),
```

#### Descripción:
- **`Text`**: Widget para mostrar un texto en la pantalla.
- **`textAlign: TextAlign.center`**: Centra el texto horizontalmente.
- **`style`**: Aplica un estilo de texto, usando `headlineSmall` del tema y modificándolo para que el texto sea en negrita (`fontWeight: FontWeight.bold`).

---

### **6. Descripción Adicional**

Añadimos un texto secundario que describe brevemente el propósito de la aplicación, con un estilo más suave.

```dart
Text(
  "Freedom talk any person of your \nmother language.",
  textAlign: TextAlign.center,
  style: TextStyle(
    color: Theme.of(context)
        .textTheme
        .bodyLarge!
        .color!
        .withOpacity(0.64),
  ),
),
```

#### Descripción:
- **`Text`**: Muestra un texto adicional en la pantalla.
- **`color`**: El color del texto se toma del tema actual de la aplicación, y se reduce su opacidad para darle un efecto más sutil (`withOpacity(0.64)`).

---

### **7. Botón de "Skip"**

Un botón que permite al usuario omitir la pantalla de bienvenida y navegar directamente a la pantalla de inicio de sesión o registro.

```dart
FittedBox(
  child: TextButton(
      onPressed: () => Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => const SigninOrSignupScreen(),
            ),
          ),
      child: Row(
        children: [
          Text(
            "Skip",
            style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                  color: Theme.of(context)
                      .textTheme
                      .bodyLarge!
                      .color!
                      .withOpacity(0.8),
                ),
          ),
          const SizedBox(width: kDefaultPadding / 4),
          Icon(
            Icons.arrow_forward_ios,
            size: 16,
            color: Theme.of(context)
                .textTheme
                .bodyLarge!
                .color!
                .withOpacity(0.8),
          )
        ],
      ))),
```

#### Descripción:
- **`FittedBox`**: Ajusta el tamaño del `TextButton` para que se ajuste a su contenido.
- **`TextButton`**: Botón que, cuando se presiona, navega a la pantalla de inicio de sesión o registro (`SigninOrSignupScreen`).
- **`Row`**: Organiza horizontalmente el texto "Skip" y el ícono de flecha.
- **`Text`**: Muestra el texto "Skip" con un estilo modificado.
- **`SizedBox`**: Añade espacio horizontal entre el texto y el ícono de la flecha.
- **`Icon`**: Muestra un ícono de flecha hacia adelante con un color personalizado.

---

### **Código Completo:**

```dart
import '../../constants.dart'; 
import '../signinOrSignUp/signin_or_signup_screen.dart';
import 'package:flutter/material.dart';

class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Column(
          children: [
            const Spacer(flex: 2),
            Image.asset("assets/images/welcome_image.png"),
            const Spacer(flex: 3),

            // Texto de bienvenida
            Text(
              "Welcome to our freedom \nmessaging app",
              textAlign: TextAlign.center,
              style: Theme.of(context)
                  .textTheme
                  .headlineSmall!
                  .copyWith(fontWeight: FontWeight.bold),
            ),

            // Descripción adicional
            Text(
              "Freedom talk any person of your \nmother language.",
              textAlign: TextAlign.center,
              style: TextStyle(
                color: Theme.of(context)
                    .textTheme
                    .bodyLarge!
                    .color!
                    .withOpacity(0.64),
              ),
            ),

            const Spacer(flex: 3),

            // Botón Skip
            FittedBox(
              child: TextButton(
                onPressed: () => Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => const SigninOrSignupScreen(),
                  ),
                ),
                child: Row(
                  children: [
                    Text(
                      "Skip",
                      style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                            color: Theme.of(context)
                                .textTheme
                                .bodyLarge!
                                .color!
                                .withOpacity(0.8),
                          ),
                    ),
                    const SizedBox(width: kDefaultPadding / 4),
                    Icon(
                      Icons.arrow_forward_ios,
                      size: 16,
                      color: Theme.of(context)
                          .textTheme
                          .bodyLarge!
                          .color!
                          .withOpacity(0.8),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```

---

#### Resumen de la Estructura:

1. **Importaciones**: Incluimos las bibliotecas y pantallas necesarias.
2. **Clase `WelcomeScreen`**: Widget sin estado para la pantalla de bienvenida.
3. **Método `build`**: Construcción de la UI.
4. **Estructura de la pantalla**: Utiliza `Scaffold`, `SafeArea`, y `Column` para organizar el contenido.
5. **Texto de bienvenida**: Un texto centrado que da la bienvenida al usuario.
6. **Botón de omisión ("Skip")**: Permite al usuario saltarse la pantalla de bienvenida y acceder directamente a la pantalla de inicio

## Creación del código "SignInOrSignUpScreen"

### 1. **Importaciones**

Primero, importamos las bibliotecas necesarias para que la pantalla funcione correctamente.

```dart
import 'package:flutter/material.dart'; // Biblioteca principal de Flutter
import '../../components/primary_button.dart'; // Widget personalizado para los botones
import '../../constants.dart'; // Constantes como colores y padding
import '../chats/chats_screen.dart'; // Pantalla de chats para la navegación
```

### Descripción:
- **`Material.dart`**: Importa los widgets y temas básicos de Flutter.
- **`primary_button.dart`**: Es el archivo que contiene un widget personalizado que creamos para los botones.
- **`constants.dart`**: Aquí guardamos las constantes comunes, como colores y márgenes.
- **`chats_screen.dart`**: Pantalla a la que navegamos después de hacer login.

---

### 2. **Definición de la Clase `SigninOrSignupScreen`**

Ahora definimos nuestra clase principal que extiende `StatelessWidget`, ya que no necesita mantener un estado.

```dart
class SigninOrSignupScreen extends StatelessWidget {
  const SigninOrSignupScreen({super.key});
```

#### Descripción:
- **`SigninOrSignupScreen`**: Es un `StatelessWidget` que genera la pantalla de inicio de sesión o registro.
- **`super.key`**: Se usa para identificar el widget en el árbol de widgets, aunque no es obligatorio en este caso.

---

### 3. **Método `build`**

El método `build` se encarga de construir y devolver la interfaz visual de la pantalla. Aquí es donde definimos el diseño.

```dart
@override
Widget build(BuildContext context) {
  return Scaffold(
    body: SafeArea(
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: kDefaultPadding),
        child: Column(
          children: [
            const Spacer(flex: 2),
            // Contenido aquí
          ],
        ),
      ),
    ),
  );
}
```

#### Descripción:
- **`Scaffold`**: Proporciona la estructura básica de la pantalla.
- **`SafeArea`**: Evita que el contenido se superponga a las áreas no visibles del dispositivo (por ejemplo, la barra de estado).
- **`Padding`**: Añade un padding uniforme a ambos lados de la pantalla, usando `kDefaultPadding` de `constants.dart`.
- **`Column`**: Organiza los widgets de forma vertical.
- **`Spacer`**: Se usa para distribuir el espacio entre los elementos en la pantalla, aquí se usa para separar los elementos de forma adecuada.

---

### 4. **Logo de la Aplicación**

Añadimos el logo de la aplicación, ajustando el tamaño según el brillo del dispositivo (modo claro u oscuro).

```dart
Image.asset(
  MediaQuery.of(context).platformBrightness == Brightness.light
      ? "assets/images/Logo_light.png"
      : "assets/images/Logo_dark.png",
  height: 146,
),
```

#### Descripción:
- **`Image.asset`**: Carga una imagen desde los recursos de la aplicación.
- **`MediaQuery.of(context).platformBrightness`**: Verifica si el dispositivo está en modo claro o oscuro.
- **`height: 146`**: Establece la altura del logo.

---

### 5. **Botón "Sign In"**

El primer botón es para iniciar sesión. Al presionarlo, navega a la pantalla de chats.

```dart
PrimaryButton(
  text: "Sign In",
  press: () => Navigator.push(
    context,
    MaterialPageRoute(
      builder: (context) => const ChatsScreen(),
    ),
  ),
),
```

#### Descripción:
- **`PrimaryButton`**: Botón personalizado definido en el archivo `primary_button.dart`.
- **`text`**: El texto que aparece en el botón ("Sign In").
- **`press`**: La acción a ejecutar cuando se presiona el botón. En este caso, navega a `ChatsScreen` usando `Navigator.push`.

---

### 6. **Espaciado entre Botones**

Añadimos un espaciado entre el botón de inicio de sesión y el de registro.

```dart
const SizedBox(height: kDefaultPadding * 1.5),
```

#### Descripción:
- **`SizedBox`**: Añade un espacio de altura entre los elementos. En este caso, multiplicamos `kDefaultPadding` por 1.5 para un espaciado adecuado.

---

### 7. **Botón "Sign Up"**

El segundo botón es para registrarse. En este caso, no tiene una acción asociada, pero puedes agregarla más adelante.

```dart
PrimaryButton(
  color: Theme.of(context).colorScheme.secondary,
  text: "Sign Up",
  press: () {
    // Aquí puedes agregar la lógica para el registro
  },
),
```

#### Descripción:
- **`PrimaryButton`**: El mismo botón personalizado que el anterior.
- **`color`**: Cambia el color del botón a un color secundario del tema actual usando `Theme.of(context).colorScheme.secondary`.
- **`press`**: Callback vacío para el momento en que se presiona el botón, donde puedes agregar la lógica de registro más adelante.

---

### 8. **Espaciador Final**

Finalmente, añadimos más espacio flexible para equilibrar la pantalla.

```dart
const Spacer(flex: 2),
```

#### Descripción:
- **`Spacer`**: Añade espacio flexible. Aquí usamos `flex: 2` para asegurar que el contenido esté bien distribuido en la pantalla.


#### Resumen de la Estructura:

1. **Importaciones**: Cargamos las dependencias necesarias.
2. **Clase Principal**: Definimos `SigninOrSignupScreen` como un widget sin estado.
3. **Método `build`**: Aquí construimos toda la UI.
4. **Logo**: Usamos un logo que cambia según el brillo del dispositivo.
5. **Botón "Sign In"**: Con un `Navigator.push` para ir a la pantalla de chats.
6. **Espaciado**: Usamos `Spacer` y `SizedBox` para crear un diseño limpio.
7. **Botón "Sign Up"**: Listo para implementar la lógica de registro más tarde.

Este enfoque modular y bien estructurado facilita el mantenimiento y la expansión de la pantalla, agregando nuevas funcionalidades en el futuro.

## Creación del código "ChatScreen"

### 1. **Importaciones**

```dart
import '../../constants.dart';
import 'package:flutter/material.dart';
import 'components/body.dart';
```

- **`../../constants.dart`**: Importa las constantes de diseño, como colores y padding.
- **`package:flutter/material.dart`**: Importa la biblioteca de Flutter para usar widgets y estilos basados en Material Design.
- **`components/body.dart`**: Importa el widget `Body`, que contiene el contenido principal de la pantalla.

### 2. **Clase `ChatsScreen`**

```dart
class ChatsScreen extends StatefulWidget {
  const ChatsScreen({super.key});

  @override
  State<ChatsScreen> createState() => _ChatsScreenState();
}
```

- **`ChatsScreen`**: Un widget con estado (StatefulWidget) que permite que su interfaz cambie dinámicamente.
- **`createState`**: Crea el estado mutable para `ChatsScreen`, es decir, el objeto `_ChatsScreenState`.

### 3. **Clase `_ChatsScreenState`**

```dart
class _ChatsScreenState extends State<ChatsScreen> {
  int _selectedIndex = 1;
}
```

- **`_ChatsScreenState`**: Define el estado de la pantalla de chats.
- **`_selectedIndex`**: Variable para almacenar el índice de la barra de navegación inferior, que inicialmente está en la posición 1 (Chats).

### 4. **Método `build`**

```dart
@override
Widget build(BuildContext context) {
  return Scaffold(
    appBar: buildAppBar(),
    body: const Body(),
    floatingActionButton: FloatingActionButton(
      onPressed: () {},
      backgroundColor: kPrimaryColor,
      child: const Icon(
        Icons.person_add_alt_1,
        color: Colors.white,
      ),
    ),
    bottomNavigationBar: buildBottomNavigationBar(),
  );
}
```

- **`build`**: Este método construye el diseño de la pantalla de chats.
- **`Scaffold`**: Estructura básica para la pantalla con:
  - **`appBar`**: Barra de aplicación personalizada (`buildAppBar()`).
  - **`body`**: Contenido principal de la pantalla (widget `Body`).
  - **`floatingActionButton`**: Botón flotante para agregar un nuevo contacto.
  - **`bottomNavigationBar`**: Barra de navegación inferior (widget `buildBottomNavigationBar()`).

### 5. **Método `buildAppBar`**

```dart
AppBar buildAppBar() {
  return AppBar(
    backgroundColor: kPrimaryColor,
    automaticallyImplyLeading: false,
    title: const Text("Chats"),
    actions: [
      IconButton(
        icon: const Icon(Icons.search),
        onPressed: () {},
      ),
    ],
  );
}
```

- **`AppBar`**: Barra de aplicación con un fondo de color definido por `kPrimaryColor`.
  - **`automaticallyImplyLeading: false`**: Oculta el botón de retroceso predeterminado.
  - **`title`**: Muestra el título "Chats".
  - **`actions`**: Añade un botón de búsqueda en la parte derecha.

### 6. **Método `buildBottomNavigationBar`**

```dart
BottomNavigationBar buildBottomNavigationBar() {
  return BottomNavigationBar(
    type: BottomNavigationBarType.fixed,
    currentIndex: _selectedIndex,
    onTap: (value) {
      setState(() {
        _selectedIndex = value;
      });
    },
    items: const [
      BottomNavigationBarItem(icon: Icon(Icons.messenger), label: "Chats"),
      BottomNavigationBarItem(icon: Icon(Icons.people), label: "People"),
      BottomNavigationBarItem(icon: Icon(Icons.call), label: "Calls"),
      BottomNavigationBarItem(
        icon: CircleAvatar(
          radius: 14,
          backgroundImage: AssetImage("assets/images/user_2.png"),
        ),
        label: "Profile",
      ),
    ],
  );
}
```

- **`BottomNavigationBar`**: Barra de navegación inferior con cuatro ítems:
  - **`currentIndex`**: Controla el ítem seleccionado.
  - **`onTap`**: Al hacer clic en un ítem, actualiza el índice seleccionado y reconstruye la pantalla usando `setState`.
  - **`items`**: Los ítems de navegación son:
    - **`Chats`**: Ícono de mensajero.
    - **`People`**: Ícono de personas.
    - **`Calls`**: Ícono de llamadas.
    - **`Profile`**: Un ícono de avatar circular con una imagen para el perfil.

#### Resumen

La pantalla **ChatsScreen** presenta:
- Una **AppBar** con el título "Chats" y un ícono de búsqueda.
- Un **FloatingActionButton** para agregar un nuevo contacto.
- Una **BottomNavigationBar** con cuatro opciones: Chats, People, Calls y Profile.
  
Este diseño ofrece una interfaz de usuario fluida, permitiendo al usuario navegar entre las diferentes secciones de la aplicación de mensajería.

## Creación del código "Body"

### Paso 1: Importaciones
Primero, importa los archivos y componentes necesarios. Asegúrate de que todos los archivos y carpetas estén organizados de acuerdo con tu estructura de proyecto.

```dart
import '../../../components/filled_outline_button.dart';
import '../../../constants.dart';
import '../../../models/chat.dart';
import '../../messages/message_screen.dart';
import 'package:flutter/material.dart';
import 'chat_card.dart';
```

### Paso 2: Definición de la clase `Body`
Define la clase `Body` como un `StatelessWidget` ya que no mantiene un estado mutable, solo construye la interfaz de usuario basada en los datos proporcionados.

```dart
class Body extends StatelessWidget {
  const Body({super.key});
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        // Aquí se incluirán los widgets del encabezado y la lista de chats
      ],
    );
  }
}
```

### Paso 3: Encabezado con los botones de filtro
El encabezado estará compuesto por un `Container` que tiene un fondo de color primario (`kPrimaryColor`) y contendrá dos botones de filtro en una fila (`Row`). Usa el widget `FillOutlineButton` para los botones de filtro, donde el primer botón es para "Recent Message" y el segundo para "Active".

```dart
Container(
  padding: const EdgeInsets.fromLTRB(
    kDefaultPadding, 0, kDefaultPadding, kDefaultPadding),
  color: kPrimaryColor,
  child: Row(
    children: [
      FillOutlineButton(press: () {}, text: "Recent Message"),
      const SizedBox(width: kDefaultPadding),
      FillOutlineButton(
        press: () {},
        text: "Active",
        isFilled: false,
      ),
    ],
  ),
),
```

### Paso 4: Lista de chats
La lista de chats se generará de manera dinámica utilizando `ListView.builder`. Esto te permite construir una lista de chats a partir de los datos proporcionados en `chatsData`. Cada ítem de la lista se representará mediante el widget `ChatCard`, y al hacer clic sobre un chat, se navegará a la pantalla de mensajes `MessagesScreen`.

```dart
Expanded(
  child: ListView.builder(
    itemCount: chatsData.length,
    itemBuilder: (context, index) => ChatCard(
      chat: chatsData[index],
      press: () => Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => const MessagesScreen(),
        ),
      ),
    ),
  ),
),
```

### Estructura final del `body.dart`
El archivo completo debería tener la siguiente estructura:

```dart
import '../../../components/filled_outline_button.dart';
import '../../../constants.dart';
import '../../../models/chat.dart';
import '../../messages/message_screen.dart';
import 'package:flutter/material.dart';
import 'chat_card.dart';

class Body extends StatelessWidget {
  const Body({super.key});
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        // Encabezado con botones de filtro
        Container(
          padding: const EdgeInsets.fromLTRB(
            kDefaultPadding, 0, kDefaultPadding, kDefaultPadding),
          color: kPrimaryColor,
          child: Row(
            children: [
              FillOutlineButton(press: () {}, text: "Recent Message"),
              const SizedBox(width: kDefaultPadding),
              FillOutlineButton(
                press: () {},
                text: "Active",
                isFilled: false,
              ),
            ],
          ),
        ),
        
        // Lista de chats
        Expanded(
          child: ListView.builder(
            itemCount: chatsData.length,
            itemBuilder: (context, index) => ChatCard(
              chat: chatsData[index],
              press: () => Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => const MessagesScreen(),
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }
}
```

### Explicación adicional:
- **FillOutlineButton**: Es un botón personalizado que probablemente se encarga de la visualización del estilo "relleno" o "contorno" según el parámetro `isFilled`.
- **ListView.builder**: Es ideal para listas dinámicas donde los ítems se generan bajo demanda, lo que mejora el rendimiento cuando se tienen muchos elementos.
- **Navigator.push**: Permite la navegación hacia la pantalla de mensajes (`MessagesScreen`) cuando se selecciona un chat.

Este archivo `body.dart` será fundamental para la visualización y organización de la pantalla de chats en tu aplicación Flutter.

## Creación del código "ChatCard"

### **Guía para Crear un Widget ChatCard**

Este manual te guiará paso a paso para crear un widget en Flutter llamado `ChatCard`, que es una tarjeta que muestra información sobre un chat, como el nombre del contacto, la imagen del avatar, el último mensaje, el estado de actividad y la hora del último mensaje.

---

### **Paso 1: Importación de Dependencias**

Lo primero que debes hacer es importar las dependencias necesarias. Añade el siguiente código al inicio de tu archivo Dart:

```dart
import '../../../models/chat.dart';
import 'package:flutter/material.dart';
import '../../../constants.dart';
```

**Explicación:**
- **chat.dart**: Aquí importarás el modelo de datos que contiene la información sobre el chat (nombre, imagen, último mensaje, etc.).
- **Material Design**: La biblioteca principal de Flutter para los widgets de interfaz de usuario.
- **constants.dart**: Aquí se importan constantes, como los valores de padding y colores, para mantener el diseño uniforme en toda la aplicación.

---

### **Paso 2: Definición de la Clase `ChatCard`**

Crea una nueva clase llamada `ChatCard` que extienda de `StatelessWidget`. Esto significa que el widget no tendrá un estado cambiante.

```dart
class ChatCard extends StatelessWidget {
  const ChatCard({
    super.key,
    required this.chat,
    required this.press,
  });

  final Chat chat;  // Instancia de la clase Chat, contiene los datos del chat
  final VoidCallback press;  // Función que se ejecuta cuando la tarjeta es presionada
}
```

**Explicación:**
- La clase `ChatCard` es un widget sin estado (`StatelessWidget`) porque no necesita gestionar datos que cambian con el tiempo.
- **chat**: Recibe una instancia del modelo `Chat` que contiene los datos de ese chat (nombre, mensaje, imagen, etc.).
- **press**: Es una función de callback que se ejecuta cuando se presiona la tarjeta de chat.

---

### **Paso 3: Construcción del Widget**

El siguiente paso es crear el método `build`, que es el encargado de construir la interfaz visual del widget.

```dart
@override
Widget build(BuildContext context) {
  return InkWell(
    onTap: press,  // Ejecuta la función cuando la tarjeta es presionada
    child: Padding(
      padding: const EdgeInsets.symmetric(
          horizontal: kDefaultPadding, vertical: kDefaultPadding * 0.75),
      child: Row(
        children: [
          // Más contenido aquí
        ],
      ),
    ),
  );
}
```

**Explicación:**
- **InkWell**: Este widget agrega un efecto de "onda" al tocar la tarjeta, indicando que es interactiva. La función `press` se ejecuta cuando se toca el widget.
- **Padding**: Se agrega un relleno alrededor del contenido dentro de la tarjeta, usando la constante `kDefaultPadding`.
- **Row**: Utiliza un `Row` para organizar horizontalmente los elementos de la tarjeta (avatar, nombre, último mensaje, etc.).

---

### **Paso 4: Agregar el Avatar y el Indicador de Estado**

Dentro de la `Row`, añade un `Stack` para superponer el avatar y un indicador de actividad (si el contacto está activo).

```dart
Stack(
  children: [
    CircleAvatar(
      radius: 24,
      backgroundImage: AssetImage(chat.image), // Imagen del contacto
    ),
    if (chat.isActive)  // Muestra el estado de actividad solo si el contacto está activo
      Positioned(
        right: 0,
        bottom: 0,
        child: Container(
          height: 16,
          width: 16,
          decoration: BoxDecoration(
            color: kPrimaryColor,  // Color del indicador de actividad
            shape: BoxShape.circle,
            border: Border.all(
              color: Theme.of(context).scaffoldBackgroundColor,  // Color del borde
              width: 3,
            ),
          ),
        ),
      )
  ],
),
```

**Explicación:**
- **Stack**: Utiliza un `Stack` para poder superponer el avatar y el indicador de actividad.
- **CircleAvatar**: Este widget muestra una imagen circular (el avatar del contacto).
- **Positioned**: Se usa para colocar el indicador de actividad en la esquina inferior derecha del avatar.

---

### **Paso 5: Mostrar Información del Chat**

A continuación, dentro de la `Row`, agrega la información del chat, como el nombre y el último mensaje.

```dart
Expanded(
  child: Padding(
    padding: const EdgeInsets.symmetric(horizontal: kDefaultPadding),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          chat.name,  // Nombre del contacto
          style: const TextStyle(
              fontSize: 16, fontWeight: FontWeight.w500),
        ),
        const SizedBox(height: 8),
        Opacity(
          opacity: 0.64,  // Baja la opacidad del último mensaje
          child: Text(
            chat.lastMessage,  // Último mensaje
            maxLines: 1,
            overflow: TextOverflow.ellipsis,  // Evita que el mensaje se desborde
          ),
        ),
      ],
    ),
  ),
),
```

**Explicación:**
- **Expanded**: Asegura que el espacio disponible en la `Row` se distribuya correctamente entre los widgets hijos.
- **Column**: Organiza los elementos de forma vertical (nombre y último mensaje).
- **Opacity**: Reduce la opacidad del último mensaje para que sea menos destacado que el nombre del contacto.

---

### **Paso 6: Mostrar la Hora del Último Mensaje**

Finalmente, muestra la hora del último mensaje en un `Text`.

```dart
Opacity(
  opacity: 0.64,  // Baja la opacidad de la hora
  child: Text(chat.time),  // Muestra la hora del último mensaje
),
```

**Explicación:**
- **Opacity**: Al igual que con el mensaje, se reduce la opacidad para que la hora no sea tan prominente.
- **Text**: Muestra la hora del último mensaje.

---

### **Código Completo**

Aquí está el código completo que debes agregar a tu archivo Dart:

```dart
import '../../../models/chat.dart';
import 'package:flutter/material.dart';
import '../../../constants.dart';

class ChatCard extends StatelessWidget {
  const ChatCard({
    super.key,
    required this.chat,
    required this.press,
  });

  final Chat chat;
  final VoidCallback press;

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: press,
      child: Padding(
        padding: const EdgeInsets.symmetric(
            horizontal: kDefaultPadding, vertical: kDefaultPadding * 0.75),
        child: Row(
          children: [
            // Avatar y estado de actividad
            Stack(
              children: [
                CircleAvatar(
                  radius: 24,
                  backgroundImage: AssetImage(chat.image),
                ),
                if (chat.isActive)
                  Positioned(
                    right: 0,
                    bottom: 0,
                    child: Container(
                      height: 16,
                      width: 16,
                      decoration: BoxDecoration(
                        color: kPrimaryColor,
                        shape: BoxShape.circle,
                        border: Border.all(
                          color: Theme.of(context).scaffoldBackgroundColor,
                          width: 3,
                        ),
                      ),
                    ),
                  ),
              ],
            ),
            const SizedBox(width: kDefaultPadding),
            // Información del chat
            Expanded(
              child: Padding(
                padding: const EdgeInsets.symmetric(horizontal: kDefaultPadding),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      chat.name,
                      style: const TextStyle(
                          fontSize: 16, fontWeight: FontWeight.w500),
                    ),
                    const SizedBox(height: 8),
                    Opacity(
                      opacity: 0.64,
                      child: Text(
                        chat.lastMessage,
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                      ),
                    ),
                  ],
                ),
              ),
            ),
            // Hora del último mensaje
            Opacity(
              opacity: 0.64,
              child: Text(chat.time),
            ),
          ],
        ),
      ),
    );
  }
}
```

---

### **Resumen de Pasos**
1. **Importa las dependencias necesarias**.
2. **Define la clase `ChatCard`** extendiendo `StatelessWidget`.
3. **Crea el método `build`** para construir la interfaz visual del widget.
4. **Agrega el avatar y el estado de actividad** usando un `Stack`.
5. **Muestra la información del chat** (nombre y último mensaje).
6. **Agrega la hora del último mensaje**.

---

Siguiendo esta guía, puedes crear el widget `ChatCard` de manera fácil y entender cómo se organiza la información del chat en una tarjeta interactiva.

## Creación del código "MessageScreen"

Este archivo define la pantalla de mensajes (`MessagesScreen`), que es un widget sin estado (`StatelessWidget`). La pantalla muestra una barra de aplicación personalizada con información sobre el usuario y opciones para realizar llamadas y videollamadas.

### 1. Información

```dart
import 'package:flutter/material.dart'; // Importa la biblioteca de Material Design de Flutter
import '../../constants.dart'; // Importa las constantes de diseño como colores y padding
import 'components/body.dart'; // Importa el widget Body que define el contenido principal de la pantalla
```

- **Material Design**: Se usa para construir la interfaz de usuario con widgets estilizados.
- **constants.dart**: Importa constantes como colores y padding para mantener un diseño uniforme.
- **Body**: Importa el widget `Body` que contiene el contenido principal de la pantalla de mensajes.

### 2. Clase **MessagesScreen**

```dart
class MessagesScreen extends StatelessWidget {
  const MessagesScreen({super.key});
```

- **MessagesScreen**: Es un widget sin estado (`StatelessWidget`) que define la estructura de la pantalla de mensajes.
- **Constructor**: `const MessagesScreen` inicializa la clase. `super.key` se usa para identificar el widget en el árbol de widgets.

### 3. Método **Build**

```dart
@override
Widget build(BuildContext context) {
```

- **Descripción**: Este método construye y devuelve el diseño de la pantalla.

### 4. Estructura del **Scaffold**

```dart
return Scaffold(
  appBar: buildAppBar(), // Llama a la función buildAppBar para construir el AppBar
  body: const Body(), // Muestra el contenido principal de la pantalla usando el widget Body
);
```

- **Scaffold**: Proporciona la estructura básica de la pantalla, con una barra de aplicación (`AppBar`) y un cuerpo (`Body`).
- **appBar**: Llama a la función `buildAppBar` para crear una barra de aplicación personalizada.
- **body**: Usa el widget `Body` para mostrar el contenido principal de la pantalla de mensajes.

### 5. Función **buildAppBar**

```dart
AppBar buildAppBar() {
```

- **Descripción**: Construye y devuelve un `AppBar` personalizado con un botón de retroceso, un avatar, información del usuario, y botones de llamada y videollamada.

### 6. Configuración del **AppBar**

```dart
return AppBar(
  automaticallyImplyLeading: false, // Desactiva el botón de retroceso predeterminado
  title: const Row(
    children: [
      BackButton(), // Botón de retroceso
      CircleAvatar(
        backgroundImage: AssetImage("assets/images/user_2.png"), // Imagen de avatar del usuario
      ),
      SizedBox(width: kDefaultPadding * 0.75), // Espaciado horizontal
      Column(
        crossAxisAlignment: CrossAxisAlignment.start, // Alinea el contenido al inicio
        children: [
          Text(
            "Kristin Watson", // Nombre del usuario
            style: TextStyle(fontSize: 16), // Estilo de texto con tamaño de fuente 16
          ),
          Text(
            "Active 3m ago", // Estado de actividad del usuario
            style: TextStyle(fontSize: 12), // Estilo de texto con tamaño de fuente 12
          )
        ],
      )
    ],
  ),
  actions: [
    IconButton(
      icon: const Icon(Icons.local_phone), // Ícono de teléfono
      onPressed: () {}, // Acción vacía para el botón de llamada
    ),
    IconButton(
      icon: const Icon(Icons.videocam), // Ícono de cámara de video
      onPressed: () {}, // Acción vacía para el botón de videollamada
    ),
    const SizedBox(width: kDefaultPadding / 2), // Espaciado adicional a la derecha
  ],
);
```

- **automaticallyImplyLeading: false**: Desactiva el botón de retroceso predeterminado del `AppBar`.
- **title**: Contiene una `Row` que organiza los widgets horizontalmente:
  - **BackButton**: Botón de retroceso que permite volver a la pantalla anterior.
  - **CircleAvatar**: Muestra la imagen del usuario como un avatar circular.
  - **SizedBox**: Añade un espacio horizontal entre el avatar y la información del usuario.
  - **Column**: Organiza el nombre y el estado del usuario verticalmente.
    - **Text ("Kristin Watson")**: Muestra el nombre del usuario con un tamaño de fuente de 16.
    - **Text ("Active 3m ago")**: Muestra el estado de actividad del usuario con un tamaño de fuente de 12.
- **actions**: Define los iconos de llamada y videollamada:
  - **IconButton (Icons.local_phone)**: Botón con un ícono de teléfono para realizar una llamada.
  - **IconButton (Icons.videocam)**: Botón con un ícono de cámara de video para iniciar una videollamada.
  - **SizedBox**: Añade un espacio adicional al final del `AppBar`.

Este código configura la interfaz básica de la pantalla de mensajes, con un diseño limpio y opciones de comunicación con el usuario, como llamada y videollamada, junto con una visualización del estado y avatar del usuario.

## Creación del código del "Body para MessageScreen"

Paso 17.- Creación del código del **Body** para **MessageScreen**

Este archivo define el widget **Body**, que es un componente sin estado (`StatelessWidget`) utilizado para estructurar la pantalla principal de mensajes en la aplicación. El widget muestra una lista de mensajes y un campo de entrada para que los usuarios puedan enviar nuevos mensajes.

### 1. Importación

```dart
import 'package:flutter/material.dart'; 
import '../../../constants.dart'; 
import '../../../models/chat_message.dart'; 
import 'chat_input_field.dart'; 
import 'message.dart'; 
```

- **Material Design**: Se utiliza para construir la interfaz de usuario con widgets estilizados.
- **constants.dart**: Importa constantes que ayudan a mantener un diseño uniforme en toda la aplicación.
- **chat_message.dart**: Importa el modelo `ChatMessage` que contiene la información de cada mensaje.
- **chat_input_field.dart**: Importa el widget que proporciona un campo de entrada para escribir y enviar mensajes.
- **message.dart**: Importa el widget que muestra el contenido de cada mensaje en la lista.

### 2. Clase **Body**

```dart
class Body extends StatelessWidget {
  const Body({super.key});
```

- **Body**: Es un widget sin estado (`StatelessWidget`) que define la estructura principal de la pantalla de mensajes.
- **Constructor**: `const Body({super.key})` inicializa el widget. La clave (`super.key`) se utiliza para identificar el widget en el árbol de widgets.

### 3. Método **Build**

```dart
@override
Widget build(BuildContext context) {
```

- **Descripción**: Este método construye y devuelve el diseño de la pantalla de mensajes.

### 4. Estructura de **Column**

```dart
return Column(
  children: [
    ...
  ],
);
```

- **Column**: Organiza los widgets en una disposición vertical. En este caso, incluye una lista de mensajes y un campo de entrada para mensajes.

### 5. Lista de mensajes

```dart
Expanded(
  // Expande el widget hijo para llenar el espacio disponible
  child: Padding(
    padding: const EdgeInsets.symmetric(horizontal: kDefaultPadding), // Padding horizontal
    child: ListView.builder(
      itemCount: demeChatMessages.length, // Número de elementos en la lista (basado en la lista de mensajes de ejemplo)
      itemBuilder: (context, index) =>
          Message(message: demeChatMessages[index]), // Construye un widget Message para cada mensaje en la lista
    ),
  ),
),
```

- **Expanded**: Expande el `ListView` para llenar todo el espacio disponible dentro de la columna.
- **Padding**: Añade un padding horizontal a la lista de mensajes usando `kDefaultPadding` para mantener el diseño uniforme.
- **ListView.builder**: Genera dinámicamente una lista de mensajes:
  - **itemCount**: Define el número de elementos en la lista, basado en `demeChatMessages`.
  - **itemBuilder**: Función que construye un widget `Message` para cada elemento de la lista de mensajes. `Message` es un widget personalizado que muestra el contenido de cada mensaje.

### 6. Campo de entrada de mensajes

```dart
const ChatInputField(),
```

- **ChatInputField**: Un widget que proporciona un campo de entrada para que el usuario escriba y envíe mensajes. Este widget se coloca en la parte inferior de la pantalla.

Este código organiza y estructura la pantalla de mensajes, mostrando la lista de mensajes en la parte superior y un campo de entrada para nuevos mensajes en la parte inferior. La funcionalidad de la lista de mensajes está completamente manejada a través del `ListView.builder`, lo que permite una carga eficiente de los mensajes, mientras que el campo de entrada permite interactuar con la aplicación al enviar mensajes.

## Creación del código "AudioMessage"

Este archivo define el widget **AudioMessage**, que es un componente sin estado (`StatelessWidget`) que representa un mensaje de audio en una conversación de chat. El widget muestra un ícono de reproducción, una línea indicativa de progreso del audio y la duración del audio.

### 1. Importaciones

```dart
import '../../../models/chat_message.dart';
import 'package:flutter/material.dart'; 
import '../../../constants.dart'; 
```

- **chat_message.dart**: Se usa para acceder a las propiedades de los mensajes, como `isSender`.
- **Material Design**: Se utiliza para construir la interfaz de usuario con widgets estilizados.
- **constants.dart**: Importa las constantes como `kPrimaryColor` y `kDefaultPadding` para mantener la consistencia de diseño.

### 2. Clase **AudioMessage**

```dart
class AudioMessage extends StatelessWidget {
  final ChatMessage? message; 

  const AudioMessage({super.key, this.message});
```

- **AudioMessage**: Es un widget sin estado (`StatelessWidget`) que muestra un mensaje de audio con un diseño específico.
- **message**: Propiedad de tipo `ChatMessage` que contiene la información del mensaje. Es opcional.

### 3. Método **Build**

```dart
@override
Widget build(BuildContext context) {
```

- **Descripción**: Este método construye y devuelve el diseño del mensaje de audio.

### 4. Estructura del **Container**

```dart
return Container(
  width: MediaQuery.of(context).size.width * 0.55, 
  padding: const EdgeInsets.symmetric(
    horizontal: kDefaultPadding * 0.75, 
    vertical: kDefaultPadding / 2.5, 
  ),
  decoration: BoxDecoration(
    borderRadius: BorderRadius.circular(30), 
    color: kPrimaryColor.withOpacity(message!.isSender ? 1 : 0.1), 
  ),
```

- **Container**: Crea un contenedor con un ancho del 55% de la pantalla y un padding simétrico.
- **MediaQuery**: Se usa para obtener el ancho de la pantalla y ajustar el tamaño del contenedor.
- **Padding**: Define el espacio interno dentro del contenedor, utilizando valores constantes.
- **Decoration**: Aplica bordes redondeados y un color de fondo que varía según si el usuario es el remitente (`isSender`).

### 5. Fila de contenido (`Row`)

```dart
child: Row(
  children: [
    Icon(
      Icons.play_arrow, // Ícono de reproducción
      color: message!.isSender ? Colors.white : kPrimaryColor, // Color del ícono según el remitente
    ),
```

- **Row**: Organiza los elementos en una fila horizontal.
- **Icon**: Muestra un ícono de reproducción. El color del ícono cambia según si el mensaje fue enviado por el usuario (`isSender`).

### 6. Indicador de progreso de audio

```dart
Expanded(
  child: Padding(
    padding: const EdgeInsets.symmetric(horizontal: kDefaultPadding / 2), // Padding interno
    child: Stack(
      clipBehavior: Clip.none, // Permite que los elementos desborden el contenedor
      alignment: Alignment.center, // Alinea los elementos al centro
      children: [
        Container(
          width: double.infinity, // Ancho completo del contenedor
          height: 2, // Altura de la línea
          color: message!.isSender
              ? Colors.white
              : kPrimaryColor.withOpacity(0.4), // Color de la línea según el remitente
        ),
        Positioned(
          left: 0, // Posiciona el círculo al inicio de la línea
          child: Container(
            height: 8, // Altura del círculo
            width: 8, // Ancho del círculo
            decoration: BoxDecoration(
              color: message!.isSender ? Colors.white : kPrimaryColor, // Color del círculo según el remitente
              shape: BoxShape.circle, // Forma circular
            ),
          ),
        ),
      ],
    ),
  ),
),
```

- **Expanded**: Expande el espacio restante en la fila para el indicador de progreso.
- **Padding**: Añade espacio horizontal dentro del indicador.
- **Stack**: Superpone el contenedor de la línea de progreso y el círculo de inicio.
- **Container**: Crea la línea de progreso con un ancho completo y una altura de 2 píxeles.
- **Positioned**: Posiciona el círculo en el inicio de la línea.
- **BoxDecoration**: Aplica un color y una forma circular al círculo.

### 7. Duración del audio

```dart
Text(
  "0.37", // Duración del audio (en segundos)
  style: TextStyle(
    fontSize: 12, // Tamaño de la fuente
    color: message!.isSender ? Colors.white : null, // Color del texto según el remitente
  ),
),
```

- **Text**: Muestra la duración del audio (en este caso, "0.37" segundos).
- **style**: Aplica un tamaño de fuente de 12 y un color que varía según el remitente del mensaje.

---

### Resumen:

El widget **AudioMessage** es un componente que visualiza un mensaje de audio en una conversación de chat. Incluye:
1. Un **ícono de reproducción** que cambia de color dependiendo de si el mensaje fue enviado por el usuario o recibido.
2. Un **indicador de progreso** que muestra la barra de progreso del audio y un círculo al principio, indicando la reproducción.
3. La **duración del audio** se muestra al final del mensaje. 

Este diseño permite que el usuario vea de manera clara y estilizada los mensajes de audio, con un control visual de la reproducción y la duración.

## Creación del código "ChatInputField"

### 1. **Importaciones**

```dart
import 'package:flutter/material.dart';
import '../../../constants.dart';
```
- **Material Design**: Se importa para usar los widgets y estilos predefinidos de Flutter como `Icon`, `TextField`, y `Container`.
- **constants.dart**: Este archivo contiene constantes de diseño, como colores y valores de padding que aseguran consistencia en el diseño.

### 2. **Clase ChatInputField**

```dart
class ChatInputField extends StatelessWidget {
  const ChatInputField({
    super.key,
  });
```
- `ChatInputField`: Es un widget sin estado (`StatelessWidget`) que maneja la interfaz para ingresar mensajes en la parte inferior de la pantalla de chat.
- El constructor utiliza `super.key` para identificar el widget de manera única en el árbol de widgets.

### 3. **Método `build`**

```dart
@override
Widget build(BuildContext context) {
```
- Este método construye y devuelve la interfaz del widget, en este caso, el campo de entrada de texto y los íconos asociados.

### 4. **Estructura del `Container`**

```dart
return Container(
  padding: const EdgeInsets.symmetric(
    horizontal: kDefaultPadding,
    vertical: kDefaultPadding / 2,
  ),
  decoration: BoxDecoration(
    color: Theme.of(context).scaffoldBackgroundColor,
    boxShadow: [
      BoxShadow(
        offset: const Offset(0, 4),
        blurRadius: 32,
        color: const Color(0xFF087949).withOpacity(0.08),
      ),
    ],
  ),
```
- **Container**: El widget principal que contiene el campo de entrada de texto.
- `padding`: Se aplica un padding horizontal y vertical para asegurar que el contenido no toque los bordes.
- `decoration`: Configura el color de fondo del contenedor (igual al color de fondo del Scaffold) y una sombra sutil debajo del contenedor para darle un efecto de elevación.

### 5. **`SafeArea` y `Row` Principal**

```dart
child: SafeArea(
  child: Row(
    children: [
      const Icon(Icons.mic, color: kPrimaryColor),
      const SizedBox(width: kDefaultPadding),
      Expanded(
        child: Container(
          ...
        ),
      ),
    ],
  ),
),
```
- **SafeArea**: Asegura que el contenido no se superponga a áreas críticas como la barra de estado o las muescas en el dispositivo.
- **Row**: Se utiliza para organizar los widgets horizontalmente.
- **Icon (micrófono)**: Muestra un ícono de micrófono para grabar un mensaje de voz.
- **SizedBox**: Añade espacio entre el ícono del micrófono y el contenedor donde se encuentra el campo de texto.
- **Expanded**: Se utiliza para que el contenedor del campo de texto ocupe el espacio restante disponible.

### 6. **Campo de Entrada de Texto**

```dart
Container(
  padding: const EdgeInsets.symmetric(
    horizontal: kDefaultPadding * 0.75,
  ),
  decoration: BoxDecoration(
    color: kPrimaryColor.withOpacity(0.05),
    borderRadius: BorderRadius.circular(40),
  ),
  child: Row(
    children: [
      Icon(
        Icons.sentiment_satisfied_alt_outlined,
        color: Theme.of(context).textTheme.bodyLarge!.color!.withOpacity(0.64),
      ),
      const SizedBox(width: kDefaultPadding / 4),
      const Expanded(
        child: TextField(
          decoration: InputDecoration(
            hintText: "Type message",
            border: InputBorder.none,
          ),
        ),
      ),
      Icon(
        Icons.attach_file,
        color: Theme.of(context).textTheme.bodyLarge!.color!.withOpacity(0.64),
      ),
      const SizedBox(width: kDefaultPadding / 4),
      Icon(
        Icons.camera_alt_outlined,
        color: Theme.of(context).textTheme.bodyLarge!.color!.withOpacity(0.64),
      ),
    ],
  ),
),
```
- **Container**: Este contenedor contiene el campo de texto con un fondo tenue y bordes redondeados.
- **Padding**: Añade un espacio interno para que el texto no toque los bordes del contenedor.
- **Decoration**: El fondo tiene una opacidad baja y bordes redondeados.
- **Row**: Organiza los widgets en una fila, que incluye:
  - **Icon (emoji)**: Muestra un ícono de emoji con opacidad en el color.
  - **SizedBox**: Espaciado entre íconos.
  - **TextField**: Campo de texto donde el usuario puede escribir un mensaje. El texto de sugerencia es "Type message".
  - **Icon (adjuntar archivo)**: Ícono para adjuntar archivos, con un color opaco.
  - **Icon (cámara)**: Ícono de cámara para adjuntar imágenes o videos.

### Resumen

El widget `ChatInputField` es una parte fundamental de la interfaz de chat, proporcionando una experiencia de entrada de mensajes cómoda y con varios íconos funcionales, como micrófono, emojis, adjuntar archivos y cámara. La estructura es flexible y adaptable a diferentes tamaños de pantalla, gracias al uso de widgets como `Expanded` y `SafeArea`.

## Creación del código "Message"

El código que defines para los widgets `Message` y `MessageStatusDot` es clave para mostrar los mensajes en un chat con diferentes tipos (texto, audio, video) y sus respectivos estados (enviado, visto, no enviado). A continuación se detallan las partes más importantes del código y su funcionalidad:

### 1. **Importaciones**

```dart
import '../../../models/chat_message.dart'; 
import 'package:flutter/material.dart'; 
import '../../../constants.dart'; 
import 'audio_message.dart'; 
import 'text_message.dart'; 
import 'video_message.dart'; 
```

- **`chat_message.dart`**: Define el modelo `ChatMessage`, que contiene las propiedades de un mensaje.
- **`audio_message.dart`**, **`text_message.dart`**, **`video_message.dart`**: Widgets que representan los diferentes tipos de mensajes (audio, texto, video).
- **`constants.dart`**: Contiene valores constantes para un diseño consistente (colores, padding, etc.).

### 2. **Clase `Message`**

```dart
class Message extends StatelessWidget {
  const Message({
    super.key,
    required this.message, // Mensaje de tipo ChatMessage que se pasará al widget
  });

  final ChatMessage message;
```

- `Message`: Un widget sin estado (StatelessWidget) que muestra un mensaje en la pantalla de chat.
- `message`: Recibe un objeto de tipo `ChatMessage` que contiene los detalles del mensaje, como el tipo y el estado.

### 3. **Método `build`**

```dart
@override
Widget build(BuildContext context) {
  return Padding(
    padding: const EdgeInsets.only(top: kDefaultPadding),
    child: Row(
      mainAxisAlignment: message.isSender
          ? MainAxisAlignment.end // Alinea a la derecha si el mensaje es enviado por el usuario
          : MainAxisAlignment.start, // Alinea a la izquierda si el mensaje es recibido
      children: [
        if (!message.isSender) ...[
          const CircleAvatar(
            radius: 12,
            backgroundImage: AssetImage("assets/images/user_2.png"), // Imagen del avatar
          ),
          const SizedBox(width: kDefaultPadding / 2),
        ],
        messageContaint(message),
        if (message.isSender)
          MessageStatusDot(status: message.messageStatus)
      ],
    ),
  );
}
```

- **Padding**: Agrega un espacio superior al mensaje.
- **Row**: Organiza el contenido del mensaje en una fila horizontal. Alinea el mensaje a la derecha si es enviado por el usuario (`message.isSender`) o a la izquierda si es recibido.
- **CircleAvatar**: Muestra el avatar del remitente solo si el mensaje no es del usuario actual.
- **messageContaint**: Llama a una función para determinar el tipo de mensaje y mostrar el widget correspondiente (Texto, Audio, Video).
- **MessageStatusDot**: Muestra el estado del mensaje si es enviado por el usuario.

### 4. **Función `messageContaint`**

```dart
Widget messageContaint(ChatMessage message) {
  switch (message.messageType) {
    case ChatMessageType.text:
      return TextMessage(message: message); // Mensaje de texto
    case ChatMessageType.audio:
      return AudioMessage(message: message); // Mensaje de audio
    case ChatMessageType.video:
      return const VideoMessage(); // Mensaje de video
    default:
      return const SizedBox(); // Espacio vacío si no hay contenido
  }
}
```

- **messageContaint**: Devuelve el tipo de widget adecuado basado en el tipo de mensaje (`text`, `audio`, `video`).

### 5. **Clase `MessageStatusDot`**

```dart
class MessageStatusDot extends StatelessWidget {
  final MessageStatus? status;

  const MessageStatusDot({super.key, this.status});
```

- **MessageStatusDot**: Es un widget sin estado que muestra un punto con un color que refleja el estado del mensaje (enviado, visto, no enviado).

### 6. **Método `build` de `MessageStatusDot`**

```dart
@override
Widget build(BuildContext context) {
  return Container(
    margin: const EdgeInsets.only(left: kDefaultPadding / 2),
    height: 12,
    width: 12,
    decoration: BoxDecoration(
      color: dotColor(status!),
      shape: BoxShape.circle,
    ),
    child: Icon(
      status == MessageStatus.notSent ? Icons.close : Icons.done,
      size: 8,
      color: Theme.of(context).scaffoldBackgroundColor,
    ),
  );
}
```

- **Container**: Crea un contenedor circular que representa el estado del mensaje.
- **dotColor**: Determina el color del punto según el estado del mensaje.
- **Icon**: Muestra un ícono basado en el estado del mensaje. Si no se envió, muestra un ícono de "cerrar"; si se envió, muestra un ícono de "hecho".

### 7. **Función `dotColor`**

```dart
Color dotColor(MessageStatus status) {
  switch (status) {
    case MessageStatus.notSent:
      return kErrorColor; // Rojo si no se envió
    case MessageStatus.notView:
      return Theme.of(context).textTheme.bodyLarge!.color!.withOpacity(0.1); // Opaco si no ha sido visto
    case MessageStatus.viewed:
      return kPrimaryColor; // Primario si fue visto
    default:
      return Colors.transparent; // Transparente si no hay estado
  }
}
```

- **dotColor**: Devuelve un color basado en el estado del mensaje.
  - **Rojo** si no se envió.
  - **Opaco** si no ha sido visto.
  - **Color primario** si fue visto.

### Conclusión

Este diseño modular permite manejar diferentes tipos de mensajes (texto, audio, video) y muestra el estado de cada mensaje mediante un pequeño punto indicador, lo que hace que la aplicación sea más interactiva y fácil de usar.

## Creación del código "TextMessage"

Este archivo define el widget `TextMessage`, que es un componente sin estado (StatelessWidget). Se encarga de mostrar un mensaje de texto en la pantalla de chat con un diseño que varía según si el mensaje es enviado por el usuario o recibido.

#### 1. **Importaciones**

```dart
import 'package:flutter/material.dart';
import '../../../constants.dart';
import '../../../models/chat_message.dart';
```

- **Material Design**: Se importa la biblioteca principal de Flutter para construir la interfaz de usuario.
- **constants.dart**: Se importan las constantes de diseño, como colores y valores de padding, para asegurar una apariencia uniforme en la interfaz.
- **chat_message.dart**: Se importa el modelo `ChatMessage`, que contiene la información del mensaje, como el texto y el estado de si fue enviado por el usuario.

#### 2. **Clase `TextMessage`**

```dart
class TextMessage extends StatelessWidget {
  const TextMessage({
    super.key,
    this.message,
  });

  final ChatMessage? message;
```

- **`TextMessage`**: Es un widget sin estado (StatelessWidget) que muestra un mensaje de texto en la pantalla de chat.
- **`message`**: Es una propiedad de tipo `ChatMessage` que contiene los datos del mensaje, como el texto del mensaje y el estado de si fue enviado por el usuario.

#### 3. **Método `build`**

```dart
@override
Widget build(BuildContext context) {
```

- **`build`**: Este método construye y devuelve el diseño del mensaje de texto.

#### 4. **Estructura del `Container`**

```dart
return Container(
  padding: const EdgeInsets.symmetric(
    horizontal: kDefaultPadding * 0.75,
    vertical: kDefaultPadding / 2,
  ),
  decoration: BoxDecoration(
    color: kPrimaryColor.withOpacity(message!.isSender ? 1 : 0.1),
    borderRadius: BorderRadius.circular(30),
  ),
```

- **`Container`**: Crea un contenedor alrededor del texto del mensaje para aplicar padding y decoración.
- **`padding`**: Añade espacio interno horizontal y vertical alrededor del texto, utilizando constantes para asegurar una apariencia consistente.
- **`decoration`**: Aplica un fondo y bordes redondeados al contenedor.
  - **`color`**: Define el color de fondo del contenedor. Si el mensaje es enviado por el usuario (`isSender` es `true`), el color es sólido (`kPrimaryColor`). Si es recibido, el color tiene una opacidad baja (`0.1`).
  - **`borderRadius`**: Redondea los bordes del contenedor con un radio de 30 píxeles, dando un aspecto más suave.

#### 5. **Texto del mensaje**

```dart
child: Text(
  message!.text,
  style: TextStyle(
    color: message!.isSender
        ? Colors.white
        : Theme.of(context).textTheme.bodyLarge!.color,
  ),
),
```

- **`Text`**: Muestra el contenido del mensaje de texto.
- **`style`**: Aplica un estilo al texto.
  - **`color`**: Si el mensaje es enviado por el usuario (`isSender` es `true`), el color del texto es blanco (`Colors.white`). Si es recibido, el color se ajusta según el tema actual de la aplicación, usando `Theme.of(context).textTheme.bodyLarge!.color`.

### Resumen

El widget `TextMessage` muestra un mensaje de texto con un diseño flexible. Su apariencia varía dependiendo de si el mensaje es enviado o recibido. Los mensajes enviados se muestran con un fondo sólido y texto blanco, mientras que los mensajes recibidos tienen un fondo translúcido y el texto con el color predeterminado del tema de la aplicación.

## Creación del código "VideoMessage"
Este archivo define el widget `VideoMessage`, que es un componente sin estado (StatelessWidget). Se utiliza para representar un mensaje de video en la pantalla de chat. Este widget muestra una imagen de marcador de posición del video con un botón de reproducción en el centro.

#### 1. **Importaciones**

```dart
import 'package:flutter/material.dart';
import '../../../constants.dart';
```

- **Material Design**: Se importa la biblioteca principal de Flutter para usar los widgets y herramientas de diseño.
- **constants.dart**: Se importa este archivo para acceder a las constantes de la aplicación, como `kPrimaryColor`, asegurando consistencia en los colores y el diseño.

#### 2. **Clase `VideoMessage`**

```dart
class VideoMessage extends StatelessWidget {
  const VideoMessage({super.key});
```

- **`VideoMessage`**: Es un widget sin estado (StatelessWidget) que muestra un mensaje de video con una imagen de fondo y un botón de reproducción.
- **Constructor**: El constructor `const VideoMessage({super.key})` inicializa el widget. La clave (`super.key`) se utiliza para identificar el widget en el árbol de widgets, lo que puede ser útil para optimizar el rendimiento.

#### 3. **Método `build`**

```dart
@override
Widget build(BuildContext context) {
```

- **`build`**: Este método construye y devuelve el diseño del mensaje de video.

#### 4. **Estructura del `SizedBox`**

```dart
return SizedBox(
  width: MediaQuery.of(context).size.width * 0.45,
  child: AspectRatio(
    aspectRatio: 1.6,
    child: Stack(
      alignment: Alignment.center,
      children: [
        ...
      ],
    ),
  ),
);
```

- **`SizedBox`**: Se usa para establecer un tamaño específico para el widget. El ancho se ajusta al 45% del ancho total de la pantalla usando `MediaQuery`, lo que asegura que el widget tenga un tamaño relativo con respecto al tamaño de la pantalla.
- **`MediaQuery`**: Utiliza `MediaQuery.of(context).size.width` para obtener el ancho de la pantalla, permitiendo que el `SizedBox` ajuste su tamaño proporcionalmente.
- **`AspectRatio`**: Se encarga de mantener la relación de aspecto del video en 1.6. Esto asegura que el contenedor del video tenga una proporción adecuada, lo que es importante para la presentación correcta del video.
- **`Stack`**: Permite apilar varios widgets uno encima del otro, y los elementos se alinean en el centro. Es ideal para colocar la imagen de fondo y el botón de reproducción uno sobre otro.

#### 5. **Imagen de fondo del video**

```dart
ClipRRect(
  borderRadius: BorderRadius.circular(8),
  child: Image.asset("assets/images/videovi.png"),
),
```

- **`ClipRRect`**: Este widget recorta la imagen de fondo del video, aplicando bordes redondeados con un radio de 8 píxeles. Esto da un toque estético al diseño, suavizando las esquinas de la imagen.
- **`Image.asset`**: Carga una imagen desde los recursos de la aplicación. En este caso, se usa una imagen de marcador de posición (`"assets/images/videovi.png"`) que representa el video. Esta imagen será visible hasta que el usuario reproduzca el video real.

#### 6. **Botón de reproducción**

```dart
Container(
  height: 25,
  width: 25,
  decoration: const BoxDecoration(
    color: kPrimaryColor,
    shape: BoxShape.circle,
  ),
  child: const Icon(
    Icons.play_arrow,
    size: 16,
    color: Colors.white,
  ),
),
```

- **`Container`**: Este widget crea un contenedor circular que actúa como un botón de reproducción. El contenedor tiene un tamaño fijo de 25 píxeles de altura y 25 píxeles de ancho.
- **`BoxDecoration`**: Define la apariencia visual del contenedor, configurando el color de fondo como `kPrimaryColor` y asegurando que tenga una forma circular (`BoxShape.circle`).
- **`Icon`**: Dentro del contenedor se muestra un ícono de reproducción (`Icons.play_arrow`). El ícono tiene un tamaño de 16 píxeles y un color blanco, lo que lo hace visible y destacado sobre el fondo.

### Resumen

El widget `VideoMessage` está diseñado para mostrar un mensaje de video en el chat, utilizando una imagen de marcador de posición y un botón de reproducción centrado. La imagen de marcador de posición es recortada con bordes redondeados, mientras que el botón de reproducción es circular y tiene un ícono de reproducción en su interior. La estructura del widget está cuidadosamente diseñada para adaptarse al tamaño de la pantalla y mantener una relación de aspecto adecuada para los videos.


