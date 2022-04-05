<blockquote>
<details>
<summary><strong>Note: </strong><code>not something we can merge</code></summary><br/>

All template repositories (a repo in the github.com/platform-templates organization) are *artifacts* of a central tool that helps our team keep them updated.
The steps described here are the steps taken by that tool to produce those artifact repositories.
This is advantageous, because we are able to describe the exact steps taken to build a working template you can use in your own migrations.

Related to this, the final line above (`git merge --allow-unrelated-histories -X theirs M.m.P`) pulls "upstream" code from the open source project used to build this template.
In some cases, those projects will only have a primary stable branch to pull from, and you will see the command as `git merge --allow-unrelated-histories -X theirs main` for example.
Feel free to copy this command exactly. 

In other cases, we will track a major version of a tag on that upstream repo (i.e. `9.3.X`), and simply pull the latest patch when updates are periodically run. 
If the command above contains a patch version, copy it exactly locally.
If it only contains a major or minor version, take a look at the output of `git fetch --all --depth=2` to find the latest tag version that fits the version listed above and use that instead.

</details>
</blockquote>
