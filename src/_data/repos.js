const { AssetCache } = require('@11ty/eleventy-fetch');
const config = require('./config.json');

module.exports = async function () {
  let asset = new AssetCache(`repos_${config.username}`);

  if (asset.isCacheValid('12h')) {
    const repos = await asset.getCachedValue();
    throwIfLatestRepoIsExcluded(repos);
    return repos;
  }

  const { Octokit } = await import('octokit');

  const octokit = new Octokit();

  const iterator = octokit.paginate.iterator(octokit.rest.repos.listForUser, {
    username: config.username,
    per_page: 50,
    sort: 'pushed',
  });

  const repos = [];

  for await (const page of iterator) {
    for( const repo of page.data) {
      if(repo.private) {
        continue
      }
      repos.push(repo);
    }
  }

	await asset.save(repos, 'json');

  throwIfLatestRepoIsExcluded(repos);

  return repos;
};

function throwIfLatestRepoIsExcluded(repos) {
  if(config.excludedRepos.includes(repos[0].name) || repos[0].name == config.username) {
    throw new Error('No new changes, skipping build');
  }
}
