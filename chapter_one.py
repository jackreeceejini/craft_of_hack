"""
Generally useful code fragments I found in the Google Cirq project.
Google Cirq is a framework for creating quantum cirquits for NISQ systems like Google
Sycamore etc. 
"""

def _human_size(num_bytes: int, mod: int = 0, units=(' bytes', 'KB', 'MB', 'GB', 'TB', 'PB')):
    """Returns a human readable string representation of bytes"""
    return (
        f'{num_bytes}.{mod}{units[0]}'
        if num_bytes < 1024
        else _human_size(num_bytes >> 10, num_bytes % 1024, units[1:])
    )
