class CustomCommand:

    def __init__(self, custom_command_service):
        self.custom_command_service = custom_command_service

    def execute(self, command: str):
        command_data = self.custom_command_service.find_command(
            command
        )

        if command_data is None:
            return None

        return self.custom_command_service.execute(
            command_data
        )
