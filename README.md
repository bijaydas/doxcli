<p align="center"><a href="https://github.com/bijaydas/doxcli" target="_blank"><img src="https://raw.githubusercontent.com/bijaydas/doxcli/v2.x/images/logo.png"></a></p>

## About DocCli

DoxCli is a cli tool which helps to do day to day jobs.

## Features

1. Check if domain is available using GoDaddy API.
2. More features are coming soon...

## Installation

1. As this project is in Alpha mode, it is recommended to install it in `virtual env`.

    ```shell
    python3 -m venv name-your-venv
    
    source path-to-your-venv/bin/activate
    
    pip install doxcli
    ```

2. Create the config file in `~/.config/doxcli/config.yaml`
3. And add your GoDaddy API credentials.
    ```yaml
   godaddy:
      api_key: api-key
      api_secret: api-secret
   ```

## How to use

After the confi file has setup, you can run the following command to check if any domain is available.

```bazaar
dox godaddy --name bijaydas.com
```
<br />

**Output screenshot**

<p align="center"><img src="https://raw.githubusercontent.com/bijaydas/doxcli/v2.x/images/godaddy-output.png" /></p>

## Contributing

Thank you for considering contributing to the DocCli!

## License

The Laravel framework is open-sourced software licensed under the [MIT license](LICENSE.md).
