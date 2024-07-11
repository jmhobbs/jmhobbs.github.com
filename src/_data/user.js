const EleventyFetch = require("@11ty/eleventy-fetch");
const config = require('./config.json');

module.exports = async function () {
	let url = `https://api.github.com/users/${config.username}`;

	return EleventyFetch(url, {
		duration: "7d",
		type: "json",
	});
};
