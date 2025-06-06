import platform

async def execute_action(command: str):
    print(f"[EXECUTING ACTION]: {command}")
    if "turn on light" in command.lower():
        return await control_gpio("on")
    elif "turn off light" in command.lower():
        return await control_gpio("off")
    elif "shutdown" in command.lower():
        return "System shutdown command received (simulation)"
    else:
        return f"Simulated response: {command}"

async def control_gpio(action):
    if platform.system() == "Linux":
        try:
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(18, GPIO.OUT)
            GPIO.output(18, GPIO.HIGH if action == "on" else GPIO.LOW)
            return f"GPIO pin set to {'HIGH' if action == 'on' else 'LOW'}"
        except Exception as e:
            return f"GPIO Error: {e}"
    return "GPIO control only available on Raspberry Pi (Linux)"
