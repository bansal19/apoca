# WhatsApp Chat Processor

An automation script that monitors for WhatsApp chat exports received via AirDrop and processes them into a structured format.

## Features

- Automatically detects WhatsApp chat exports in your Downloads folder
- Processes raw chat text files into structured JSON format
- Organizes chats by contact name
- Archives original files to prevent duplicate processing
- Provides clear instructions for exporting chats from iPhone

## Prerequisites

- macOS
- iPhone with WhatsApp installed
- Python 3.6+
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/whatsapp-processor.git
   cd whatsapp-processor
   ```

2. Create a virtual environment and install required Python packages:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage

1. Start the monitoring script:
   ```
   python whatsapp_exporter.py
   ```

2. Follow the on-screen instructions to export chats from your iPhone:
   - Open WhatsApp on your iPhone
   - Go to Settings > Chats > Export Chat
   - Select the chat(s) you want to export
   - Choose "Without Media" for faster exports
   - Select "AirDrop" from the share sheet
   - Select your Mac from the AirDrop options
   - Accept the incoming file on your Mac

3. The script will automatically detect the exported chat files in your Downloads folder and process them into JSON format.

### Custom Configuration

You can customize the behavior by editing the `config.json` file or using command-line arguments:

```
python whatsapp_exporter.py --watch-dir ~/Documents --output-dir ~/WhatsApp/Processed
```

## Output Format

The processed chats are saved as JSON files with the following structure:

```json
{
  "chat_name": "Contact Name",
  "export_date": "2025-04-05T15:30:00",
  "message_count": 123,
  "messages": [
    {
      "date": "4/5/25",
      "time": "15:30:00",
      "sender": "Contact Name",
      "content": "Hello!",
      "media": null
    },
    ...
  ]
}
```

## License

See the [LICENSE](LICENSE) file for details.
