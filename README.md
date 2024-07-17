# igendoc-search-ai

## Instruction

Follow this instruction from the root folder

1. Create a VM:

```
python3 -m venv venv
```

2. Activate the VM:

```
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the server:

```
python app.py
```

5. Test the server by hitting this GET endpoint: [hello-api](http://127.0.0.1:5000/v1/hello)

6. To deploy, run:

```
./deploy "commit message"
```

7. Once deployment is done in step 6, ssh to the remote host:

```
ssh -i "path/to/sshkey" root@ai.server.igendoc.com
```

8. In the remote host root level, run:

```
./start.sh
```

9. Test endpoint in production: [hello-api](http://ai.server.igendoc.com:5000/v1/hello)

10. To view server logs, run:

```
docker logs search-ai-server
```

The following logs should show:

```
[2024-07-17 05:59:43 +0000] [1] [INFO] Starting gunicorn 22.0.0
[2024-07-17 05:59:43 +0000] [1] [INFO] Listening at: http://0.0.0.0:5000 (1)
[2024-07-17 05:59:43 +0000] [1] [INFO] Using worker: sync
[2024-07-17 05:59:43 +0000] [7] [INFO] Booting worker with pid: 7
[2024-07-17 05:59:43 +0000] [8] [INFO] Booting worker with pid: 8
[2024-07-17 05:59:43 +0000] [9] [INFO] Booting worker with pid: 9
[2024-07-17 05:59:44 +0000] [10] [INFO] Booting worker with pid: 10
```
