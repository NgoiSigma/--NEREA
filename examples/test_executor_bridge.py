from core.executor_bridge import ExecutorBridge

bridge = ExecutorBridge()

# Регистрируем внешнюю точку (например, Telegram Webhook)
bridge.register_endpoint("telegram_notify", "https://your.bot/api/notify")

# Добавляем shell-команду
bridge.register_command("list_dir", "ls -la")

print(bridge.execute_command("list_dir"))
print(bridge.call_endpoint("telegram_notify", {"message": "FDL активирован"}))
