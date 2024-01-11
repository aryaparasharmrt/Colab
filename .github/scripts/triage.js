const { Octokit } = require('@octokit/rest');

const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN,
});

async function triageIssue(issueNumber) {
  try {
    const issue = await octokit.issues.get({
      owner: "aryaparasharmrt",
      repo: "Colab",
      issue_number: issueNumber,
    });

    // Define your triage criteria here
    const keywords = ['bug', 'error', 'issue'];

    const isTriageLabel = issue.data.labels.some(label =>
      keywords.includes(label.name.toLowerCase())
    );

    // Assign a category label based on the triage criteria
    if (isTriageLabel) {
      await octokit.issues.addLabels({
        owner: process.env.GITHUB_REPOSITORY_OWNER,
        repo: process.env.GITHUB_REPOSITORY,
        issue_number: issueNumber,
        labels: ['triaged'],
      });

      console.log(`Issue ${issueNumber} has been triaged.`);
    }
  } catch (error) {
    console.error(`Error triaging issue ${issueNumber}: ${error.message}`);
  }
}

triageIssue(process.env.GITHUB_EVENT.issue.number);
