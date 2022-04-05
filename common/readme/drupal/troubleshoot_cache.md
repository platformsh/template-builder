<details>
<summary><strong>Clearing the cache</strong></summary><br/>

After the environment has finished its deployment, you can investigate issues that occured on startup, `deploy` and `post_deploy` hooks, and generally at runtime using the CLI. Run the command:

```bash
platform ssh
```

If you are running the command outside of a local copy of the project, you will need to include the `-p` (project) and/or `-e` (environment) flags as well. 
Once you have connected to the container, [logs](https://docs.platform.sh/development/logs.html#container-logs) are available within `/var/log/` for you to investigate.

</details>
