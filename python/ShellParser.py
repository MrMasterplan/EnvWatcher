

def GetShellParser(shell_var):
    """Decides which shell environment reader and diff writer to use."""
    if shell_var == "/bin/bash":
        from Bash import BashInteractor
        return BashInteractor
    else:
        raise Exception("Unknown shell.")
    

