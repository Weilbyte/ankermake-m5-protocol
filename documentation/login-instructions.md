# Login Instructions

To interact with your AnkerMake printer via `ankerctl`, you need to authenticate your AnkerMake account so that the tool can fetch your profile, find your printers, and retrieve the encrypted communication keys.

Instead of needing to use the proprietary desktop slicer to pull your data, `ankerctl` now supports logging in directly using your **Email**, **Password**, and **Country Code**.

## How to Login via Command Line

Open a terminal window in the `ankermake-m5-protocol` directory and simply run:

```sh
python ankerctl.py config login
```

The tool will prompt you for your AnkerMake account credentials:

1. **Email address**: Your AnkerMake email.
2. **Password**: Your AnkerMake password (hidden while typing).
3. **Country (2 digit code)**: The ISO alpha-2 country code where your account is registered (e.g., `US`, `DE`, `GB`). This is required to determine the correct regional AnkerMake server to connect to.

### Solving Captchas

Occasionally, the AnkerMake authentication server will challenge your login request with a visual Captcha. `ankerctl` handles this gracefully:

- If a captcha is required, a temporary HTML file containing the captcha image will automatically open in your default web browser.
- Look at the image, return to your terminal, and type the characters you see to complete the login.

### Direct Login via Arguments

If you want to pass your credentials directly to the script (e.g. for automation, though this stores your password in your shell history), you can provide the arguments inline:

```sh
python ankerctl.py config login [COUNTRY_CODE] [EMAIL] [PASSWORD]
```

Example:
```sh
python ankerctl.py config login US my@email.com my_password123
```

## Verifying Your Login

Once authorized, `ankerctl` will download your configured printers and save an encrypted token locally in its configuration file.

The output will look similar to this:
```sh
[*] Initializing API..
[*] Using region 'US'
[*] Logging in..
[*] Login successful, importing configuration from server..
[*] Initializing API..
[*] Requesting profile data..
[*] Requesting printer list..
[*] Requesting pppp keys..
[*] Adding printer [AK7ABC0123401234]
[*] Finished import
```

At this point, your configuration is saved locally. You can verify it by running:

```sh
python ankerctl.py config show
```

The terminal will print out your stored `user_id`, `auth_token`, and the serial numbers, IP addresses, and keys of all associated AnkerMake printers.

> **Note:** The cached login info contains sensitive details. The `user_id` field in particular allows connection to MQTT servers and essentially acts as a password. Thus, parts of the value are redacted when printed.

You are now ready to launch the webserver or interact with your printer!
