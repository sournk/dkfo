# dkfo
File organizer script for Downloads folder

Author: Denis Kislitsyn
Email: denis@kislitsyn.me
  
Script gets one param - src dir path.
Script moves all files and subdirs older than 2 days from src dir into !Archive/%dd subdirs.
Script is useful for Downloads folder. Just add script into your cron task.

## Usage

Check script params:
```
python3 dkfo.py --help
```

Basiс usage for your Downloads folder:
```
python3 dkfo.py --dir="/Users/you_name/Downloads"
```

Don't touch files older than 2 days:
```
python3 dkfo.py --dir="/Users/you_name/Downloads" --file_age_limit=2
```


## Cron settings for MacOs Monterey
```
crontab -e # Edit crontab file in vi. Press i to enter insert mode and :wq to write and quit file 
```

```
* * * * * python3 /Users/sournk/dev/dkfo/dkfo.py /Users/sournk/Downloads
```

```
crontab -l
```

Don't forget to add full disk access permission to cron.
- Go to Setting-Security and Privacy.
- Pick Disk acсess
- Press +
- Press cmd+Shift+G and go to /usr/sbin and choose cron app.

