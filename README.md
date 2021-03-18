# Custom Minigrid

A rip of the gaagle multigrid implementation. 
We are interested in the adversarial environment, so I just pulled out the
relevant modules and put them into a pip-installable package here. 
Eventually we are going to want to modify the code to enable domain shifts
i.e. change the colours of the grid objects, modify how the observations look,
etc.

# Install

The usual:

```bash
git clone https://github.com/GT-melee/custom-minigrid.git
pip install -e custom_minigrid/
```

Note the `-e` flag just symlinks the package so you can dick with the code
and you don't have to reinstall it every time.

# Examples

Useful scripts and _notebooks_ will be dumped into `./examples`. 

# TODO

- [x] Understand how the adversarial environment works (generation, etc)
- [ ] Use this environment with some baselines to validate performance
- [ ] Modify the env code to support domain shift
- [ ] Modify the env code to generate raw image outputs as observations