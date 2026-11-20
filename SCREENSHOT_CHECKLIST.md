# Screenshots to capture

After the passing workflow run appears at the repository's Actions tab, capture genuine GitHub pages:

1. `01_actions_success.png` — workflow summary showing both **Test ML Application** and **Deploy Application** succeeded.
2. `02_actions_test_steps.png` — test job steps, including model accuracy and pytest output.
3. `03_actions_deploy_log.png` — deploy simulation log showing `ML application deployed successfully.`

Optional failure-gate evidence: use a temporary `0.99` assertion and capture `04_actions_failure_gate.png` showing the test job failed and deploy was skipped. Restore the `0.80` assertion and rerun the passing workflow afterward.
