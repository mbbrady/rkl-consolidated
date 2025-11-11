# Cron Configuration for Weekly Brief Generation

## Installation on Betty Head Node (serv)

### 1. SSH to head node
```bash
ssh mike-serv@192.168.1.10
```

### 2. Edit crontab
```bash
crontab -e
```

### 3. Add weekly job
```cron
# RKL Secure Reasoning Brief - Weekly Generation
# Runs every Monday at 9:00 AM
0 9 * * 1 /home/mike/project/rkl-consolidated/secure-reasoning-brief/scripts/run_weekly.sh >> /home/mike/project/rkl-consolidated/secure-reasoning-brief/data/logs/cron.log 2>&1
```

### 4. Verify cron job
```bash
crontab -l | grep "Secure Reasoning"
```

---

## Alternative: Systemd Timer (More Modern)

### 1. Create service file
```bash
sudo nano /etc/systemd/system/rkl-brief.service
```

Content:
```ini
[Unit]
Description=RKL Secure Reasoning Brief Generation
After=network.target ollama.service

[Service]
Type=oneshot
User=mike-serv
WorkingDirectory=/home/mike/project/rkl-consolidated/secure-reasoning-brief
ExecStart=/home/mike/project/rkl-consolidated/secure-reasoning-brief/scripts/run_weekly.sh
StandardOutput=append:/home/mike/project/rkl-consolidated/secure-reasoning-brief/data/logs/systemd.log
StandardError=append:/home/mike/project/rkl-consolidated/secure-reasoning-brief/data/logs/systemd.log
```

### 2. Create timer file
```bash
sudo nano /etc/systemd/system/rkl-brief.timer
```

Content:
```ini
[Unit]
Description=RKL Secure Reasoning Brief Weekly Timer
Requires=rkl-brief.service

[Timer]
OnCalendar=Mon *-*-* 09:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

### 3. Enable and start
```bash
sudo systemctl enable rkl-brief.timer
sudo systemctl start rkl-brief.timer
sudo systemctl status rkl-brief.timer
```

### 4. View schedule
```bash
systemctl list-timers | grep rkl
```

---

## Testing

### Manual test
```bash
/home/mike/project/rkl-consolidated/secure-reasoning-brief/scripts/run_weekly.sh
```

### Check logs
```bash
tail -f /home/mike/project/rkl-consolidated/secure-reasoning-brief/data/logs/cron.log
```

---

## Monitoring

### View last run
```bash
ls -lt /home/mike/project/rkl-consolidated/secure-reasoning-brief/data/logs/ | head
```

### Check brief was generated
```bash
ls -lt /home/mike/project/rkl-consolidated/website/content/briefs/ | head
```

### View git commits
```bash
cd /home/mike/project/rkl-consolidated/website
git log --oneline | head
```

---

## Troubleshooting

### Cron not running
```bash
# Check cron service
sudo systemctl status cron

# Check cron logs
sudo journalctl -u cron | tail -20

# Test script manually
bash -x /home/mike/project/rkl-consolidated/secure-reasoning-brief/scripts/run_weekly.sh
```

### Script fails
```bash
# Check Python environment
source /home/mike/project/rkl-consolidated/secure-reasoning-brief/venv/bin/activate
python --version
pip list

# Check Ollama
curl http://192.168.1.10:11434/api/tags

# Check disk space
df -h
```

### No brief generated
```bash
# Check intermediate files
ls -la /home/mike/project/rkl-consolidated/secure-reasoning-brief/data/intermediate/

# Check error logs
cat /home/mike/project/rkl-consolidated/secure-reasoning-brief/data/logs/cron.log
```

---

## Configuration

Edit schedule in crontab or systemd timer file:

```
# Every Monday at 9 AM
0 9 * * 1

# Every day at 6 AM
0 6 * * *

# Every hour
0 * * * *

# Every 30 minutes
*/30 * * * *
```

---

## Disabling

### Cron
```bash
crontab -e
# Comment out or delete the line
```

### Systemd
```bash
sudo systemctl stop rkl-brief.timer
sudo systemctl disable rkl-brief.timer
```
