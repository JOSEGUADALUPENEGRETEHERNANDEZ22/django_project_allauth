# Gestión de usuarios con Django Allauth

Repositorio base para la práctica de autenticación en Django 5.2 usando **django-allauth**. Incluye los flujos de registro, inicio de sesión, cierre de sesión, cambio y restablecimiento de contraseña, así como plantillas personalizadas con Tailwind.

## Requisitos previos
- Python 3.10 o superior (el entorno fue probado con Python 3.13).
- Pip actualizado (`python -m pip install --upgrade pip`).
- Entorno virtual creado en la raíz del proyecto (`python -m venv .venv`).

## Puesta en marcha rápida
1. Activar el entorno virtual:
   - PowerShell: `\.venv\Scripts\activate`
2. Instalar dependencias:
   ```bash
   python -m pip install django==5.2.0
   python -m pip install django-allauth==0.61.1
   ```
3. Aplicar migraciones iniciales y crear un superusuario:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Ajustar el sitio por defecto (opcional, recomendado para enlaces de correo):
   ```bash
   python manage.py shell
   >>> from django.contrib.sites.models import Site
   >>> Site.objects.update_or_create(id=1, defaults={"domain": "localhost:8000", "name": "Plataforma"})
   >>> exit()
   ```
5. Ejecutar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```
6. Abrir `http://127.0.0.1:8000/` y probar los flujos descritos abajo.

## Flujos disponibles
- **Registro:** `/accounts/signup/`
- **Inicio de sesión:** `/accounts/login/`
- **Cierre de sesión:** botón "Cerrar sesión" en la barra superior (solo si hay autenticación activa).
- **Cambio de contraseña:** `/accounts/password/change/`
- **Restablecimiento de contraseña:** `/accounts/password/reset/` (el enlace llega a la consola gracias al backend de correo en modo consola).

## Estructura relevante
```
Unidad 4/
├── manage.py
├── django_project_allauth/
│   ├── settings.py         # Configuración de Django y django-allauth
│   └── urls.py             # Rutas principales + include de allauth
└── templates/
    ├── base.html           # Plantilla maestra con navegación y mensajes
    ├── home.html           # Página de bienvenida (ruta `/`)
    └── account/            # Sobrescritura de plantillas de allauth
        ├── login.html
        ├── signup.html
        ├── password_change.html
        ├── password_reset.html
        ├── password_reset_done.html
        ├── password_reset_from_key.html
        └── password_reset_from_key_done.html
```

## Configuración clave de Allauth (`settings.py`)
- `SITE_ID = 1`
- `AUTHENTICATION_BACKENDS` incluye `allauth.account.auth_backends.AuthenticationBackend`.
- Redirecciones: `LOGIN_REDIRECT_URL = "/"` y `LOGOUT_REDIRECT_URL = "/accounts/login/"`.
- Credenciales por correo o usuario: `ACCOUNT_AUTHENTICATION_METHOD = "username_email"`.
- Correo obligatorio y verificación deshabilitada para el laboratorio: `ACCOUNT_EMAIL_REQUIRED = True`, `ACCOUNT_EMAIL_VERIFICATION = "none"`.
- Backend de correo en consola: `EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"`.

## Personalización de plantillas
Las vistas de allauth consumen las plantillas almacenadas en `templates/account/`. Cada formulario aplica una estética uniforme (Tailwind CDN). Se pueden cambiar textos, clases o mensajes editando esos archivos; Django recargará los cambios automáticamente en modo debug.

## Solución de problemas
- **Error `No module named 'accounts'`:** elimina `"accounts"` de `INSTALLED_APPS` o crea la app con `python manage.py startapp accounts` si necesitas lógica propia.
- **Recuperación de contraseña lanza un error SMTP:** confirma que `EMAIL_BACKEND` está configurado como `django.core.mail.backends.console.EmailBackend`. El enlace aparecerá en la terminal donde corre el servidor.
- **Migraciones fallidas por entorno incorrecto:** asegúrate de que `(venv)` aparece en la consola antes de ejecutar comandos y reinstala dependencias si recibes `ModuleNotFoundError`.

## Próximos pasos sugeridos
- Crear pruebas automatizadas para los flujos de autenticación.
- Integrar proveedores sociales (`allauth.socialaccount`) cuando se disponga de credenciales.
- Migrar las plantillas a componentes reutilizables o integrarlas con un build de Tailwind local si se requiere mayor personalización.

Con este README deberías poder replicar el entorno en cuestión de minutos y demostrar el funcionamiento de los flujos solicitados en la práctica.
