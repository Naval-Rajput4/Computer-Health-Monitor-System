
import psutil
import os
import shutil
from datetime import datetime


# ==========================================
# PROJECT: COMPUTER HEALTH MONITORING SYSTEM
# ==========================================


# 1. CHECK DISK SPACE
def check_disk():

    disk = psutil.disk_usage("C:\\")

    total = disk.total / (1024 ** 3)
    used = disk.used / (1024 ** 3)
    free = disk.free / (1024 ** 3)

    print("\n========== DISK INFORMATION ==========")

    print(f"Total Disk Space : {total:.2f} GB")
    print(f"Used Disk Space  : {used:.2f} GB")
    print(f"Free Disk Space  : {free:.2f} GB")
    print(f"Disk Usage       : {disk.percent}%")

    if disk.percent >= 90:
        print("Disk Status      : CRITICAL")

    elif disk.percent >= 80:
        print("Disk Status      : WARNING")

    else:
        print("Disk Status      : NORMAL")


# 2. CHECK RAM USAGE
def check_ram():

    ram = psutil.virtual_memory()

    total = ram.total / (1024 ** 3)
    used = ram.used / (1024 ** 3)
    available = ram.available / (1024 ** 3)

    print("\n========== RAM INFORMATION ==========")

    print(f"Total RAM     : {total:.2f} GB")
    print(f"Used RAM      : {used:.2f} GB")
    print(f"Available RAM : {available:.2f} GB")
    print(f"RAM Usage     : {ram.percent}%")

    if ram.percent >= 90:
        print("RAM Status    : CRITICAL")

    elif ram.percent >= 80:
        print("RAM Status    : WARNING")

    else:
        print("RAM Status    : NORMAL")


# 3. CHECK CPU USAGE
def check_cpu():

    cpu = psutil.cpu_percent(interval=1)

    print("\n========== CPU INFORMATION ==========")

    print(f"CPU Usage : {cpu}%")

    if cpu >= 90:
        print("CPU Status : CRITICAL")

    elif cpu >= 80:
        print("CPU Status : WARNING")

    else:
        print("CPU Status : NORMAL")


# 4. CHECK OVERALL SYSTEM HEALTH
def check_health():

    disk = psutil.disk_usage("C:\\")
    ram = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)

    print("\n========== SYSTEM HEALTH ==========")

    print(f"Disk Usage : {disk.percent}%")
    print(f"RAM Usage  : {ram.percent}%")
    print(f"CPU Usage  : {cpu}%")

    if (disk.percent >= 90 or
        ram.percent >= 90 or
        cpu >= 90):

        print("\nOVERALL STATUS: CRITICAL")

    elif (disk.percent >= 80 or
          ram.percent >= 80 or
          cpu >= 80):

        print("\nOVERALL STATUS: WARNING")

    else:
        print("\nOVERALL STATUS: NORMAL")


# 5. CREATE FOLDER BACKUP
def create_backup():

    source = input(
        "\nEnter the folder path you want to backup: "
    ).strip().strip('"')

    if not os.path.isdir(source):
        print("Error: Folder does not exist!")
        return

    backup_folder = r"C:\ComputerHealthProject\Backups"

    os.makedirs(backup_folder, exist_ok=True)

    source = os.path.abspath(source)
    backup_folder = os.path.abspath(backup_folder)

    if os.path.commonpath([source, backup_folder]) == source:
        print("Error: Choose a folder outside the backup folder!")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_name = os.path.join(
        backup_folder,
        "Backup_" + timestamp
    )

    try:

        shutil.make_archive(
            backup_name,
            "zip",
            root_dir=source
        )

        print("\nBackup created successfully!")
        print("Backup location:", backup_name + ".zip")

    except Exception as e:

        print("Backup failed:", e)


# 6. VIEW BACKUP HISTORY
def view_backup_history():

    backup_folder = r"C:\ComputerHealthProject\Backups"

    print("\n========== BACKUP HISTORY ==========")

    if not os.path.exists(backup_folder):
        print("No backup history available.")
        return

    files = [
        file for file in os.listdir(backup_folder)
        if file.endswith(".zip")
    ]

    if not files:
        print("No backups found.")
        return

    for index, file in enumerate(sorted(files), start=1):

        print(f"{index}. {file}")


# 7. SAVE SYSTEM REPORT
def save_report():

    report_folder = r"C:\ComputerHealthProject\Reports"

    os.makedirs(report_folder, exist_ok=True)

    disk = psutil.disk_usage("C:\\")
    ram = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    report_path = os.path.join(
        report_folder,
        f"System_Report_{timestamp}.txt"
    )

    with open(report_path, "w") as report:

        report.write("COMPUTER HEALTH REPORT\n")
        report.write("======================\n\n")

        report.write(f"Date and Time: {datetime.now()}\n\n")

        report.write(f"Disk Usage: {disk.percent}%\n")
        report.write(f"RAM Usage: {ram.percent}%\n")
        report.write(f"CPU Usage: {cpu}%\n")

        report.write(
            "\nDisk Status: " +
            ("CRITICAL" if disk.percent >= 90 else
             "WARNING" if disk.percent >= 80 else "NORMAL")
        )

        report.write(
            "\nRAM Status: " +
            ("CRITICAL" if ram.percent >= 90 else
             "WARNING" if ram.percent >= 80 else "NORMAL")
        )

        report.write(
            "\nCPU Status: " +
            ("CRITICAL" if cpu >= 90 else
             "WARNING" if cpu >= 80 else "NORMAL")
        )

    print("\nSystem report saved successfully!")
    print("Report location:", report_path)


# 8. MAIN MENU
def main():

    while True:

        print("\n")
        print("========================================")
        print("  COMPUTER HEALTH MONITORING SYSTEM")
        print("========================================")

        print("1. Check Disk Space")
        print("2. Check RAM Usage")
        print("3. Check CPU Usage")
        print("4. Check Overall System Health")
        print("5. Create Folder Backup")
        print("6. View Backup History")
        print("7. Save System Report")
        print("8. Exit")

        print("========================================")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            check_disk()

        elif choice == "2":
            check_ram()

        elif choice == "3":
            check_cpu()

        elif choice == "4":
            check_health()

        elif choice == "5":
            create_backup()

        elif choice == "6":
            view_backup_history()

        elif choice == "7":
            save_report()

        elif choice == "8":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# START THE PROJECT
if __name__ == "__main__":
    main()
