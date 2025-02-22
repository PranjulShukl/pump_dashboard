from django.apps import AppConfig
import threading


class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_app'

    def ready(self):
        # Importing inside the ready method to avoid circular import issues
        from my_app.management.commands.mqtt_listener import Command

        # Start the MQTT listener in a separate thread to prevent blocking the server
        def start_listener():
            Command().handle()

        # Using a thread to start the listener without blocking the server
        listener_thread = threading.Thread(target=start_listener, daemon=True)
        listener_thread.start()

