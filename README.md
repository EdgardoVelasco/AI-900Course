# Funciones que podría usar el instructor
En este documento se muestran algunas muestras de formatos que se pueden usar en el archivo **README.me** que pueden ser de ayuda para el instructor

- [Fragmentos de código](#fragmentos-de-codigo)
- [Listas](#listas)
- [Tablas](#tablas)
- [Insertar imágenes](#imagenes)
- [Alertas](#alertas)

# Fragmentos de codigo


## Bloques de código
Para agregar algún fragmento de código debemos de usar la siguiente sintáxis:


### Python

```python
import datetime

def str2date(sf:str):#"2020-05-08"
    datos=sf.split('-')#['2020', '05', '08']
                #'2020':str->2020:int, '05':str->05:int, '08':str->05:int
    fecha=datetime.date(int(datos[0]), int(datos[1]), int(datos[2]))
    return fecha

sf=input("ingrese la fecha YYYY-MM-DD: ")
fecha=str2date(sf)
print(fecha)
print(type(fecha))
```

### Java
```java
public void cleanup() {
        try {
            if (connection != null)
                connection.close();
        } catch (Exception e) {
            System.out.println("Excepción capturada: ");
            e.printStackTrace();
        }
    }
```


### shell
```shell
#!/bin/sh

CONTADOR=0
until [ $CONTADOR – ge 3]]; do
    echo El contador es $CONTADOR
    CONTADOR=$(($CONTADOR+1))
done
```

### Ruby
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>

```

### Javascript

```javascript
var database=db.getSiblingDB("database")
var collection=database.getCollection("people")

var data=[
    {name:"edgar"},
    {name:"juan"},
    {name:"alicia"}
]

data.forEach(t=>{
    console.log(t)
    var result=collection.insertOne(t)
    console.log(result)
})

```
# Listas

## Lista simple
- elemento 1
- elemento 2
- elemento 3

## Lista números
1. elemento 1
2. elemento 2
3. elemento 3

## Lista anidada
- Elemento principal
    - Elemento interno 1
    - Elemento interno 2
        - elemento 
        - elemento
    - elemento interno 3

## Lista de tareas
- [ ] tarea 1
- [x] tarea 2
- [ ] tarea 3 
- [ ] \(Optional) tarea opcional 

# Tablas

## Tabla simple

| título columna 1  | título columna 2|
| ------------- | ------------- |
| contenido 1  | contenido 2  |
| contenido 3  | contenido 4  |


## Tabla con formato en las columnas

| Command | Description |
| --- | --- |
| `git status` | List all *new or modified* files |
| `git diff` | Show file differences that **haven't been** staged |


## Alinear contenido en tabla
| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |

# Imagenes

Para insertar una imágen se usa la siguiente sintáxis:

```
![descripción de la imagen](url imagen)
```
El url de la imágen puede ser de la siguiente forma:

- Si la imágen esta dentro de la misma rama se usa la siguiente sintaxis:
    ```
     ![description](/assets/images/imagen1.png)
    ```
    - Donde:
        - la ruta */assets/images* esta dentro de la rama donde se encuentra el archivo **README.md**

- Si la imágen esta en otra rama se usa la siguiente sintaxis:
    ```
    ![description](/../name_branch/assets/images/imagen1.png)
    ```
    - Donde: 
        - La ruta */../name_branch/assets/images/* esta dentro de el mismo repositorio pero es una rama diferente. 

- Si la imagén esta en internet se usa la siguiente sintaxis: 
    ``` 
     ![description](https://url/imagen.png)
    ```
- Si se quiere controlar el tamaño de la imágen se debe usar html, de la siguiente forma:
    ``` html
    <img src="url image" width="200" height="200">
     
    ```
    - Donde: 
        - En el html se pueden editar los siguiente elementos: 
            - **url image**:  La ruta de la imágen
            - **width**: Ancho de la imágen en pixeles
            - **height**: Alto de la imágen en pixeles


# Alertas

> [!NOTE]
> útil para agregar alguna nota extra

> [!TIP]
> útil para dar algún tip

> [!IMPORTANT]
> útil para algún recordatorio

> [!WARNING]
> útil para alertar a los alumnos

> [!CAUTION]
> útil para sugerencias y precauciones.
