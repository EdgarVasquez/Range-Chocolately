# Steps

1) Intalacion de pyinstaller "pip intall -U pyinstaller" en el CMD
3) Crear carpeta main
4) Pyinstaller main.py --onefile para crear un archivo.
5) Creacion de Choco con nombre determinado este sera el nombre del paquete, del cual automaticamente generara varios archivos, entre ellos el install, uninstall y el modify.
6) Abrir un editor de codigo como "Visual Code" y modificar informaciones como Autores, descripcion y etc esto se debe realizar en el archivo con extension .nunspec.
7) crear carpeta "src"
8) Modificar "Chocolateyinstall" en el apartado "PackageArgs" y eliminar los comentarios.
9) Modificar "ChocolateyUninstall" y poner los argumentos de lugar.
10) Entrar el apartado License.txt y eliminar datos
11) En el apartado Verification Agregar informacion del autor
12) Ejecutar el comando **Choco pack** para que se cree la compilacion del paquete y generara un archivo .nupkg. 
13) En el CMD o PowerShell instalar la version nueva de Choco para asi tenerlo actualizado con la ultima version.
14) En caso de tenerlo local podra ejecutar el siguiente comando: **Choco install range_1098586_1095504.portable.0.0.1.nupkg**
15) Si desea instalarlo desde la web de chocolate una vez haya sido comprobado debe usar: **Choco install range_1098586_1095504.portable --0.0.1**, el 0.0.1 indica la version especificada en el .nunspec
17) Registrase en Community.chocolate.org
##### **Ojo:**
	Debido a que se toma 2 dias de validacion de las versiones, se hara de manera local

12) En la pagina de Community.chocolate.org, hacer la validacion con el ApiKey con el archivo ya creado que queremos subir.
13) La misma pagina le proporcionara la api que va a usar, el comando para setearla es: **Choco Apikey --Key Api_key --source https://push.chocolatey.org/** Siendo la palabra: **Api_key** la ApiKey que te proporcionara chocolate.
14) Hacer un Push para subir el archivo, para lo mismo se debe usar el siguiente comando: **Choco push PackageName.nupgk --source https://push.chocolatey.org/**. En caso de que todo salga bien debe salir un mensaje que se envio correctamente a los servidores de chocolate, al igual que una advertencia la cual dira que sera sometido una revision.
15) Esperar la validacion, estas son 3 pruebas durando la ultima de test un total de 2 dias. 
