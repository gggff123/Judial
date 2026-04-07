import os
import urllib.request
url='https://huggingface.co/bartowski/Llama-3.2-1B-Instruct-GGUF/resolve/main/Llama-3.2-1B-Instruct-Q4_K_S.gguf'
file='Llama-3.2-1B-Instruct-Q4_K_S.gguf'
def download(url, path):
    def progress(block_num, block_size, total_size):
        downloaded = block_num * block_size
        percent = downloaded / total_size * 100
        print(f"\rDownloading... {percent:.2f}%", end="")

    urllib.request.urlretrieve(url, path, reporthook=progress)
    print("\nDone!")

if not os.path.exists(file):
    print('Model Not found')
    download(url, file)
else:
    print("Model loaded")
    
    #Imports 
    from rich.console import Console
    from rich.panel import Panel
    from rich.spinner import Spinner
    from rich.prompt import Prompt
    from llm import chat
    #init console
    console=Console()
    # cli banner
    banner=r"""
        █████                █████  ███            ████ 
        ░░███                ░░███  ░░░            ░░███ 
        ░███  █████ ████  ███████  ████   ██████   ░███ 
        ░███ ░░███ ░███  ███░░███ ░░███  ░░░░░███  ░███ 
        ░███  ░███ ░███ ░███ ░███  ░███   ███████  ░███ 
    ███   ░███  ░███ ░███ ░███ ░███  ░███  ███░░███  ░███ 
    ░░████████   ░░████████░░████████ █████░░████████ █████
    ░░░░░░░░     ░░░░░░░░  ░░░░░░░░ ░░░░░  ░░░░░░░░ ░░░░░ 
                                                                                                            
    """
    console.print(banner)
    #welcome message
    console.print(Panel('Hello Welcome to judial , Enter input to get started'),style='white on blue')
    while True:
        user_input = Prompt.ask("> ")
        if user_input == '/quit' or user_input == '/exit':
            console.print('[green]Exited Successfully')
            break
        else:
            with console.status('[orange]Generating',spinner='star',speed=1):
                output=chat(user_input)
                console.print(Panel(output),style='green')
            
