# Σ-NEREA / core/executor_bridge.py

import subprocess
import requests

class ExecutorBridge:
    def __init__(self):
        self.endpoints = {}  # Название → URL
        self.commands = {}   # Название → shell-команда

    def register_endpoint(self, name, url):
        self.endpoints[name] = url

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, name):
        command = self.commands.get(name)
        if not command:
            return f"[Ошибка]: Команда '{name}' не найдена."
        try:
            output = subprocess.check_output(command, shell=True, encoding="utf-8")
            return f"[Результат команды '{name}']:\n{output}"
        except subprocess.CalledProcessError as e:
            return f"[Ошибка выполнения]: {e}"

    def call_endpoint(self, name, payload=None):
        url = self.endpoints.get(name)
        if not url:
            return f"[Ошибка]: Endpoint '{name}' не зарегистрирован."
        try:
            response = requests.post(url, json=payload or {})
            return f"[Ответ от '{name}']: {response.status_code} → {response.text}"
        except requests.RequestException as e:
            return f"[Ошибка запроса]: {e}"
