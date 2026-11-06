# Computer Health Monitoring and Automated Backup System

A Python-based Windows utility developed as a Networking and Cloud Computing project. It helps a user check basic computer resource usage and create ZIP backups of important folders.

## Features

- Checks disk usage for the configured `C:` drive.
- Displays RAM usage and available memory.
- Measures CPU usage.
- Classifies resource usage using configurable health thresholds:
  - **Normal:** below 80%
  - **Warning:** 80% to below 90%
  - **Critical:** 90% or above
- Creates timestamped ZIP backups of a selected folder.
- Displays backup history.
- Saves system reports.

## Technologies Used

- Python 3
- `psutil`
- Python standard libraries: `os`, `shutil`, and `datetime`
- Windows
- Visual Studio Code

## Project Structure

```text
ComputerHealthProject/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── Backups/
├── Reports/
├── Logs/
└── Documentation/
    ├── Computer_Health_Monitoring_Project_Report_10_Pages.docx
    └── Computer_Health_Monitoring_Project_Presentation_10_Slides.pptx
```

## Requirements

- Windows computer
- Python 3 installed
- pip package installer

Install the required library:

```powershell
pip install -r requirements.txt
```

## How to Run

Open PowerShell or the VS Code terminal, move into the project folder, and run:

```powershell
python main.py
```

Follow the menu displayed by the program to check system resources, create a backup, view backup history, or save a report.

## Important Notes

- This version monitors the local computer; it is not yet a remote or multi-computer network monitoring system.
- Disk monitoring is configured for the `C:` drive in the current implementation.
- Monitoring is performed when the user selects the relevant menu option.
- Do not commit personal backup archives, private system reports, passwords, or other sensitive information to a public repository.
- Keep an additional copy of important backups on a separate drive or secure storage location.

## Future Enhancements

- Monitor multiple computers over a network.
- Schedule automatic backups.
- Add desktop or email alerts.
- Build a graphical dashboard.
- Store monitoring reports centrally.

## Project Documentation

The `Documentation` folder contains the project report and 10-slide presentation.
