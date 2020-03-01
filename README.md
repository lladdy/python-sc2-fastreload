# FastReload-SC2

Example scripts fast reloading SC2 instances in python-sc2.  
This is faster than having to restart each SC2 instance, but could be less stable.

## Setup

Install general requirements

`pip install -r requirements.txt`

Remove the install python-sc2 and rely on the local sc2 module files

`pip uninstall sc2`

## Examples

`./run_single_instance.py` is an example that runs a single SC2 instance with a bot verses the built-in AI.
`./run_multiple_instance.py` is an example that runs 2 SC2 instance - each with it's own bot.
