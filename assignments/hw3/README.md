# [Homework 3](https://github.com/hanggrian/IIT-CS587/blob/assets/assignments/hw3.pdf): Setup

This document provides instructions for setting up the GenAI to automate the
defect removal effectiveness analysis.

## Pre-requisites

![Pre-requisites](https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw3/figure1_1.svg)

Install Python 3.10 or later and Jupyter Notebook or Lab. Optionally, Jupyter
packages can be installed in a virtual environment with PIP.

<table>
  <thead>
    <tr>
      <th>OS</th>
      <th>Command</th>
      <th>Note</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Debian</td>
      <td>
        <pre><code class="lang-sh">sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10 jupyter</code></pre>
      </td>
      <td>
        Add user repository to install older Python versions. Only Jupyter
        Notebook is available in the official repository.
      </td>
    </tr>
    <tr>
      <td>Red Hat</td>
      <td>
        <pre><code class="lang-sh">sudo dnf install python</code></pre>
      </td>
      <td>
        Jupyter is not available in official repository.
      </td>
    </tr>
    <tr>
      <td>Arch Linux</td>
      <td>
        <pre><code class="lang-sh">yay -S python310 jupyterlab</code></pre>
      </td>
      <td>
        Install with an AUR helper, like
        <a href="https://github.com/Jguer/yay/">yay</a>.
      </td>
    </tr>
    <tr>
      <td>macOS</td>
      <td>
        <pre><code class="lang-sh">brew install python@3.10 jupyterlab</code></pre>
      </td>
      <td>
        <a href="https://brew.sh/">Homebrew</a> package manager is required.
      </td>
    </tr>
    <tr>
      <td>Windows</td>
      <td>
        <pre><code class="lang-sh">winget install Python.Python.3.10 ProjectJupyter.JupyterLab</code></pre>
      </td>
      <td>
        <a href="https://learn.microsoft.com/en-us/windows/package-manager/winget/">WinGet</a>
        comes pre-installed since Windows 10.
      </td>
    </tr>
  </tbody>
</table>

Start a Jupyter instance and keep it running in a terminal session. Depending on
the OS, the instance can also be started as a service.

```sh
jupyter lab
```

> Verify Python installation with:
>
> ```sh
> python --version

## Building

![Building](https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw3/figure1_2.svg)

Create a virtual environment and activate it in the current terminal session.

```sh
python -m venv .venv
source .venv/bin/activate
```

Install the required packages. We are using [uv](https://docs.astral.sh/uv/) in
this example, an unofficial package that is considerably faster than PIP.

```sh
pip install uv
uv pip install -r requirements.txt
```

One of the installed packages is a
[IPython Jupyter kernel](https://ipython.org/), which allows linking the
active virtual environment to the Jupyter instance.

```sh
python -m ipykernel install --user --name=.venv
```

> The building process can be automated with a Python IDE, such as *PyCharm.*

## Integrating

![Integrating](https://github.com/hanggrian/IIT-CS587/raw/assets/assignments/hw3/figure1_3.svg)

To use OpenAI models, we need to generate an API key. The key is sensitive and
should not be shared or committed to a public repository. Preferably, the key
is stored as an environment variable:

OS | Where | Loading time
--- | --- | ---
Any | `~/.env` file | Loaded by the application
UNIX-like | `~/.bash_profile` or `~/.zprofile` file | Every user login
| | `~/.bashrc` or `~/.zshrc` file | Every terminal startup
Windows | `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment` registry | Every system boot
| | `HKEY_CURRENT_USER\Environment` registry | Every user login

