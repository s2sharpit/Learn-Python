user_input: str = input("Command:")
p_command: list[str] = user_input.split()

print(p_command)

match p_command:
    case ['find', *images]:
        print(f"Finding: {images}")
    case ['download', *images]:
        print(f'Downloading: {images}')
    case ['cancel' | 'delete', *images] if len(images) > 1:
        print(f'Deleting: {images}')
    case _:
        print('Command not recognised...')